---
name: Generación de Documentos Word (python-docx)
description: Directrices de formato, paginación, tablas y estilos corporativos al generar archivos Word (.docx) con python-docx en Python.
enabled: true
---

---
name: docx
description: "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', '.dotx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx or .dotx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation."
license: Proprietary. LICENSE.txt has complete terms
---

# Generación Profesional de Documentos Word (.docx) por JSON

Para garantizar la máxima fiabilidad, diseño profesional y personalización estética del documento de Word, Atlas utiliza un compilador intermedio que toma una especificación estructurada en **JSON** y la compila en un archivo `.docx` llamando a la herramienta nativa del sistema:

* **`compile_json_to_docx(json_path, docx_path)`**
  * `json_path`: Ruta relativa del archivo JSON de origen (ej: `especificacion.json`).
  * `docx_path`: Ruta relativa de destino para el archivo Word (ej: `documento.docx`).

> [!IMPORTANT]
> **INVOQUE LA HERRAMIENTA NATIVA DIRECTAMENTE:**
> Debes invocar la herramienta `compile_json_to_docx` directamente desde tu interfaz de herramientas (tool calls) como un comando estructurado.
> * **NO** es una función o librería de Python que puedas importar (está estrictamente prohibido hacer `import compile_json_to_docx` o usar `from atlas_system import...`).
> * **NO** ejecutes comandos de consola (shell) ni scripts de Python intermedios para intentar compilar el JSON.
> * Invócala única y exclusivamente como la llamada de herramienta `compile_json_to_docx(json_path, docx_path)`.

> [!WARNING]
> **ORDEN DE OPERACIONES CRÍTICO:** La herramienta `compile_json_to_docx` requiere que el archivo JSON de especificación exista físicamente en el disco. 
> Por lo tanto, en tus turnos iniciales DEBES escribir el archivo JSON utilizando la herramienta `write_file` (y `append_file` si es extenso) antes de llamar a `compile_json_to_docx`. Nunca intentes compilar un archivo JSON que aún no has creado.

---

## ⛔ ERRORES CRÍTICOS — PROHIBIDO COMETER (ANTI-PATTERNS)

Esta sección documenta los errores más frecuentes que el modelo comete al generar especificaciones de Word. **Estudia y evita TODOS estos patrones.**

### ❌ ERROR 1: Usar la clave `"sections"` en lugar de `"elements"`

**NUNCA hagas esto:**
```json
{
  "settings": { ... },
  "sections": [
    { "type": "heading", "text": "Capítulo 1" }
  ]
}
```

**SIEMPRE usa `"elements"` como clave raíz del contenido:**
```json
{
  "settings": { ... },
  "elements": [
    { "type": "heading", "level": 1, "text": "Capítulo 1" }
  ]
}
```

> [!CAUTION]
> Si usas `"sections"`, `"content"`, `"chapters"`, `"blocks"` o cualquier otra clave diferente a `"elements"`, el compilador ignorará TODO el contenido y generará un documento en blanco sin reportar un error visible. Esto es un fallo silencioso y catastrófico.

---

### ❌ ERROR 2: Fragmentar el JSON incorrectamente con `append_file`

Cuando el documento es extenso, se usa `write_file` para el inicio y `append_file` para añadir contenido. El error más frecuente es dejar el JSON **incompleto o mal cerrado** entre fragmentos.

**NUNCA hagas esto (JSON roto entre fragmentos):**

Fragmento 1 (write_file):
```json
{
  "settings": { "font_name": "Arial" },
  "elements": [
    { "type": "heading", "level": 1, "text": "Capítulo 1" },
    { "type": "paragraph", "text": "Contenido..." }
  ]
}
```

Fragmento 2 (append_file — INCORRECTO):
```json
,
    { "type": "heading", "level": 1, "text": "Capítulo 2" }
```

Esto crea un JSON inválido porque el primer fragmento ya cerró el array `]` y el objeto `}`.

**ESTRATEGIA CORRECTA para documentos extensos:**

**Fragmento 1 (write_file) — deja el array `elements` ABIERTO:**
```json
{
  "settings": { "font_name": "Arial", "watermark": "BORRADOR" },
  "elements": [
    { "type": "cover_page", "title": "Mi Documento", "subtitle": "Subtítulo" },
    { "type": "heading", "level": 1, "text": "Sección 1" },
    { "type": "paragraph", "text": "Contenido de la sección 1." }
```

**Fragmentos intermedios (append_file) — solo comas y más elementos:**
```json
    ,
    { "type": "heading", "level": 1, "text": "Sección 2" },
    { "type": "paragraph", "text": "Contenido de la sección 2." }
```

**Fragmento final (append_file) — cierra el array y el objeto raíz:**
```json
    ,
    { "type": "signature_block", "signatures": [{ "name": "Autor", "role": "Cargo" }] }
  ]
}
```

> [!IMPORTANT]
> **Regla de oro:** El archivo JSON completo debe tener exactamente **un** `{` de apertura, **un** `]` para cerrar `elements` y **un** `}` de cierre al final. Verifica mentalmente esta estructura antes de compilar.

---

### ❌ ERROR 3: Tipos de elemento no válidos

El compilador **solo reconoce** estos tipos de elementos dentro de `"elements"`:

| Tipo válido | Descripción |
|---|---|
| `cover_page` | Portada del documento |
| `heading` | Título o subtítulo (nivel 1, 2 o 3) |
| `paragraph` | Párrafo de texto |
| `table` | Tabla con filas y columnas |
| `image` | Imagen embebida |
| `page_break` | Salto de página |
| `signature_block` | Bloque de firmas al final |

**NUNCA uses tipos inventados como:** `"section"`, `"toc"`, `"table_of_contents"`, `"list"`, `"bullet_list"`, `"caption"`, `"divider"`, `"box"`, `"callout"`, `"standard"`, `"system_section"`.

Si quieres un índice (TOC), represéntalo con una tabla (`"type": "table"`) y filas con los números de sección.
Si quieres viñetas, usa `"type": "paragraph"` con `"style": "bullet"`.

---

### ❌ ERROR 4: Saltos de línea físicos dentro de strings JSON

**NUNCA insertes un salto de línea físico dentro de un valor de texto:**
```json
{ "type": "paragraph", "text": "Primera línea
Segunda línea" }
```

**Usa siempre la secuencia de escape `\\n`:**
```json
{ "type": "paragraph", "text": "Primera línea\\nSegunda línea" }
```

---

### ❌ ERROR 5: Comillas sin escapar dentro de strings

**NUNCA dejes comillas dobles sin escapar dentro de un valor:**
```json
{ "type": "paragraph", "text": "El protocolo "TCP/IP" es fundamental" }
```

**Escapa siempre las comillas internas con `\\\"`:**
```json
{ "type": "paragraph", "text": "El protocolo \\\"TCP/IP\\\" es fundamental" }
```

---

## Planificación para Documentos Extensos (Más de 10-20 páginas o mas)

Si el documento de Word solicitado es extenso (p. ej., tesis, libros o manuales largos de más de 10 a 20 páginas o mas depende de la complejidad), está estrictamente prohibido intentar generar todo el contenido en una sola llamada de respuesta del LLM para evitar el límite de tokens de salida. 

En su lugar, el agente debe seguir obligatoriamente este plan de 3 pasos:

1. **Generación del Plan Interno en Markdown (.md):** El agente diseña el índice, capítulos y estructura y **los escribe obligatoriamente en un archivo de planificación con extensión `.md`** (ej: `missions/plan_tesis.md`). Está **estrictamente prohibido** crear un archivo JSON para representar el plan de trabajo.
2. **Seguimiento y Escritura en Bloques Grandes (Máxima Eficiencia por Turno):**
   - **PROHIBIDO hacer `append_file` de pedacitos individuales de 50 a 200 bytes** (ej: enviar solo un título o solo un párrafo por turno). Esto agota innecesariamente el límite de 30 turnos del agente.
   - **DEBES escribir bloques grandes y completos de 2 a 3 capítulos por cada llamada de `append_file`** (de 3.000 a 8.000 bytes por llamada).
   - De este modo, un documento extenso de 15 a 20 páginas se construye limpiamente en solo 4 a 5 turnos:
     - *Turno 1*: `write_file` con `settings`, portada, objetivos e índice (deja el array `elements` abierto).
     - *Turno 2*: `append_file` con Capítulos 1, 2 y 3 completos.
     - *Turno 3*: `append_file` con Capítulos 4, 5, 6 y 7 completos.
     - *Turno 4*: `append_file` con Capítulos 8, 9, 10, Conclusión, Bibliografía y cierre final `] }`.
     - *Turno 5*: Invocar la herramienta nativa `compile_json_to_docx(json_path, docx_path)` para compilar el documento Word.
3. **Compilación Única de Golpe:** Una vez que el archivo JSON contiene la especificación completa del documento completo (con el array `elements` y el objeto raíz correctamente cerrados), el agente invoca la herramienta nativa `compile_json_to_docx` una única vez para generar el archivo Word final.

> [!IMPORTANT]
> **REGLAS DE ORO PARA LA ESCRITURA DEL JSON (EVITAR ERRORES SINTÁCTICOS):**
> * **Saltos de línea en texto:** Está **completamente prohibido** dejar saltos de línea físicos/crudos en medio de un valor string del JSON. Si necesitas representar un salto de línea en un párrafo, debes escribir literalmente la secuencia de escape `\\n` (dos caracteres: barra invertida + n).
> * **Comillas internas:** Cualquier comilla doble dentro de un valor de texto debe estar correctamente escapada como `\\\"`.
> * **Compilación directa:** Invoca directamente la herramienta nativa `compile_json_to_docx(json_path, docx_path)` para compilar. No utilices comandos de validación estrictos en Python como `json.load` en el shell, ya que carecen del reparador automático de caracteres y dobles escapes (`\\\\\"`) integrado en la herramienta nativa del sistema, el cual auto-corrige y compila el documento de forma segura. Si la compilación falla con errores graves de sintaxis insalvables, detente, limpia y reescribe por completo el archivo JSON desde cero.

---

## Esquema JSON del Documento

Al generar la especificación, el modelo de IA debe devolver un objeto JSON que siga el siguiente esquema técnico:

```json
{
  "settings": {
    "font_name": "Arial" | "Times New Roman" | "Calibri",
    "font_size": 11,
    "line_spacing": 1.15,
    "margin_inch": 1.0,
    "theme_color": "1B365D",
    "orientation": "portrait" | "landscape",
    "watermark": "CONFIDENCIAL" | "BORRADOR" | null
  },
  "elements": [
    {
      "type": "cover_page",
      "title": "Título del Documento",
      "subtitle": "Subtítulo o descripción",
      "author": "Nombre del Autor",
      "organization": "Nombre de la Empresa",
      "date": "Fecha de Emisión"
    },
    {
      "type": "heading",
      "level": 1 | 2 | 3,
      "text": "Título de la Sección",
      "border": "bottom" | "top" | null
    },
    {
      "type": "paragraph",
      "style": "Normal" | "bullet",
      "align": "left" | "center" | "right",
      "bold": false,
      "italic": false,
      "color": "HEX_COLOR" | null,
      "text": "Texto del párrafo",
      "border": "bottom" | "top" | null
    },
    {
      "type": "table",
      "align": "center" | "left",
      "widths_inches": [1.5, 3.5, 1.5],
      "headers": ["Columna 1", "Columna 2", "Columna 3"],
      "rows": [
        [
          { "value": "Celda 1.1", "bold": true, "fill": "F2F5F8", "color": "1B365D" },
          "Celda 1.2 (texto simple)",
          { "value": "1,500 USD", "align": "right" }
        ]
      ]
    },
    {
      "type": "image",
      "path": "ruta/local/imagen.png",
      "width_inches": 5.0,
      "align": "center",
      "caption": "Figura 1: Descripción de la imagen"
    },
    {
      "type": "page_break"
    },
    {
      "type": "signature_block",
      "signatures": [
        { "name": "Nombre Firma 1", "role": "Cargo 1" },
        { "name": "Nombre Firma 2", "role": "Cargo 2" }
      ]
    }
  ]
}
```

---

## Directrices de Diseño según el Tipo de Documento

### 1. Documento Formal (Contratos, Propuestas, Informes Ejecutivos)
* **Paleta:** Azul Marino (`1B365D`) como `theme_color` principal.
* **Portada:** Incluir un elemento `"type": "cover_page"` como primer elemento del documento.
* **Márgenes:** `"margin_inch": 1.0`.
* **Encabezados:** Usar `"border": "bottom"` en los títulos principales (Heading 1) para trazar una línea elegante de color bajo la cabecera.
* **Firmas:** Finalizar con un bloque `"type": "signature_block"` para formalizar la aprobación de las partes.

### 2. Documento Normal (Memos, Cartas, Actas)
* **Paleta:** Gris Carbón (`2D3748`) o Azul Marino (`1B365D`).
* **Portada:** No incluir portada. Iniciar directamente con un título centrado (`"align": "center"`) con un borde inferior.
* **Estructura:** Párrafos limpios con interlineado `"line_spacing": 1.15` y espaciado sutil.

### 3. Formularios y Fichas de Recolección de Datos
* **Cajas de Entrada:** Representar las zonas de llenado mediante tablas de una o dos celdas con `"border": "box"`.
* **Casillas de verificación:** Usar caracteres claros como `[ ]` o `☐` para las opciones interactivas.
* **Espaciado:** Interlineado corto y celdas con padding para facilitar la escritura manual o digital.

### 4. Presentaciones y Diapositivas (Formato Horizontal)
* **Orientación:** Configurar `"orientation": "landscape"` (horizontal).
* **Saltos:** Colocar un elemento `"type": "page_break"` después de cada diapositiva/sección.
* **Títulos:** Títulos grandes (`heading` nivel 1) y centrados.
* **Cuerpo:** Evitar bloques de texto. Usar únicamente viñetas concisas (`"style": "bullet"`).
* **Cajas Destacadas:** Para notas especiales o citas, usar una tabla de 1 fila y 1 columna con un sombreado de fondo claro (ej: `"fill": "F2F5F8"`).

---

## Validación de la Salida
Para validar el documento y cerciorarse de que el diseño cumple con los estándares estéticos, realiza una conversión de prueba a PDF y exporta las imágenes:

```bash
soffice --headless --convert-to pdf salida.docx
pdftoppm -png -r 100 salida.pdf page
```
Inspecciona visualmente las páginas resultantes para ajustar los anchos de columna de las tablas o los márgenes de página.