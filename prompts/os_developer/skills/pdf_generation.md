---
name: pdf
description: Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.
enabled: true
license: Proprietary. LICENSE.txt has complete terms
---

# Skill: PDF Generation (Atlas)

> **Filosofía de esta skill:** El agente **nunca** intenta generar PDFs directamente con librerías Python complejas.  
> El flujo es siempre: **diseñar HTML → ejecutar la herramienta nativa `compile_html_to_pdf` → PDF listo.**
> **Ubicación de archivos**: Especifica siempre las rutas de entrada y salida de forma relativa al workspace (ej: `reporte.html`, `documento.pdf`). La herramienta nativa se encarga de resolver las rutas del sistema automáticamente.

---

## 1. Cuándo usar esta skill

| El usuario pide... | Acción |
|---|---|
| Crear un PDF, reporte, factura, documento | → Flujo estándar (§3) |
| Convertir contenido existente a PDF | → Flujo estándar (§3) |
| Leer o extraer texto de un PDF existente | → Ver §6 (lectura) |
| Combinar, dividir o manipular PDFs | → Ver §7 (operaciones) |

---

## 2. Herramienta de Conversión Nativa (`compile_html_to_pdf`)

Para generar un archivo PDF a partir de un diseño HTML, el sistema dispone de la herramienta nativa **`compile_html_to_pdf`**.
Esta herramienta ejecuta internamente el motor de renderización (Playwright Chromium) de forma segura, se encarga de resolver las rutas y los espacios físicos en Windows automáticamente, y **abre el PDF generado de forma automática en el navegador web predeterminado** al completarse la conversión con éxito.

### Firma de la Herramienta

- **`compile_html_to_pdf(html_path, pdf_path)`**
  * `html_path`: Ruta relativa del archivo HTML de origen (ej: `reporte.html`).
  * `pdf_path`: Ruta relativa de destino para el archivo PDF (ej: `reporte.pdf`).

Está **ESTRICTAMENTE PROHIBIDO** ejecutar comandos manuales de terminal para compilar archivos PDF o escribir scripts Python intermedios para llamar al generador, a menos que la tarea lo exija explícitamente. Usa siempre la herramienta nativa.

---

## 3. Flujo Estándar de Creación 

> [!IMPORTANT]
> **REGLA DE SIMPLICIDAD:**
> A menos que la tarea de Atlas pida explícitamente programar o entregar un script de Python (ej: *"crea un script en Python que..."*), está **ESTRICTAMENTE PROHIBIDO** crear archivos `.py` intermedios.
> Tu flujo de trabajo debe ser directo y sin crear archivos de código:
> 1. Escribe el archivo `.html` directamente usando la herramienta `write_file`.
> 2. Compila el PDF llamando a la herramienta nativa `compile_html_to_pdf`.
> Esto evita dejar archivos temporales de Python innecesarios en el workspace.

### Paso 1 — Diseñar el HTML
El HTML debe ser **autocontenido**: todo CSS va en `<style>` dentro del `<head>`. Sin archivos externos, sin fuentes de Google Fonts por URL (pueden fallar), sin JavaScript complejo.

**Plantilla base:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <style>
    /* Reset y base */
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: Arial, sans-serif;
      font-size: 11pt;
      color: #2c3e50;
      line-height: 1.5;
    }

    /* Encabezado del documento */
    .header {
      border-bottom: 3px solid #1B365D;
      padding-bottom: 12px;
      margin-bottom: 24px;
    }
    h1 { font-size: 20pt; color: #1B365D; }
    h2 { font-size: 14pt; color: #34495e; margin: 16px 0 8px; }

    /* Tablas */
    table { width: 100%; border-collapse: collapse; margin: 12px 0; }
    th { background: #1B365D; color: white; padding: 8px 10px; text-align: left; }
    td { padding: 7px 10px; border-bottom: 1px solid #e0e0e0; }
    tr:nth-child(even) td { background: #f7f9fc; }

    /* Salto de página */
    .page-break { page-break-after: always; }

    /* Footer */
    .footer {
      position: relative;
      margin-top: 40px;
      font-size: 8pt;
      color: #999;
      text-align: center;
      border-top: 1px solid #eee;
      padding-top: 4px;
    }
  </style>
</head>
<body>

  <div class="header">
    <h1>Título del Documento</h1>
    <p>Subtítulo o descripción breve</p>
  </div>

  <h2>Sección 1</h2>
  <p>Contenido de la sección...</p>

  <table>
    <thead>
      <tr><th>Columna A</th><th>Columna B</th><th>Columna C</th></tr>
    </thead>
    <tbody>
      <tr><td>Dato 1</td><td>Dato 2</td><td>Dato 3</td></tr>
    </tbody>
  </table>

  <!-- Salto de página explícito -->
  <div class="page-break"></div>

  <h2>Sección 2 — página nueva</h2>
  <p>Contenido...</p>

  <div class="footer">
    Generado por Sistema Atlas · {today_date}
  </div>

</body>
</html>
```

### Paso 2 — Escribir el HTML en disco
Escribe el contenido HTML directamente usando la herramienta `write_file` en el archivo de tu elección (ej: `sistema_digestivo.html`).

### Paso 3 — Compilar a PDF usando la herramienta nativa
Llama a la herramienta `compile_html_to_pdf` pasando el archivo HTML de origen y la ruta de destino deseada para el PDF:

* **Ejemplo de llamada:**
  `compile_html_to_pdf(html_path="sistema_digestivo.html", pdf_path="sistema_digestivo_humano.pdf")`

### Paso 4 — Validar el PDF Resultante
Verifica de forma proactiva que la llamada a la herramienta retornó éxito (`[SUCCESS]`) y el archivo PDF se ha creado en el disco.

---

## 4. Reglas de Diseño HTML para PDF

### Estilo Visual Académico y Profesional (OBLIGATORIO)

- **Emojis e Iconos Informales**: Está **ESTRICTAMENTE PROHIBIDO** usar emojis o iconos informales similares (como ⌨️, 🚀, 💻, etc.) dentro del HTML para la generación del PDF. El diseño debe ser serio, académico y sobrio.
- **Títulos y Subtítulos**: Todos los encabezados (`h1`, `h2`, `h3`, etc.) deben tener negrilla explícita (`font-weight: bold`). Los subtítulos y secciones secundarias deben llevar un color sobrio y distinguible (como `#1B365D` o `#2c3e50`) para dar contraste profesional, en lugar de negro plano o colores genéricos chillones.
- **Formateo Editorial y Legibilidad**: Todo documento debe tener un interlineado profesional (`line-height` entre `1.5` y `1.6`), espaciado entre párrafos (`margin-bottom` de `12px` a `16px`), márgenes laterales de página adecuados, y padding holgado en las celdas de las tablas (`padding: 8px 12px`) para garantizar una lectura cómoda y un acabado editorial.

### Lo que funciona bien

| Elemento | Notas |
|---|---|
| CSS en `<style>` embebido | Siempre funciona |
| Fuentes del sistema | `Arial`, `Times New Roman`, `Courier New`, `Georgia` |
| Colores hex y rgb | Funcionan correctamente |
| Tablas HTML estándar | Soporte completo |
| `page-break-after: always` | Salto de página explícito |
| Imágenes en base64 | `<img src="data:image/png;base64,..."` |
| Imágenes por ruta local absoluta | `<img src="/ruta/absoluta/img.png">` |

### Lo que puede fallar o está prohibido

| Elemento | Alternativa / Regla |
|---|---|
| Google Fonts por URL | Usar fuentes del sistema |
| `position: fixed` en footer | **PROHIBIDO**. Causa duplicación o renderizado roto en PDFs multipágina. Usar siempre `position: relative` o `static` en el flujo natural del documento. |
| JavaScript (`<script>`) | **PROHIBIDO**. El PDF generado es estático. No incluyas scripts de JS (como DOMContentLoaded), botones interactivos o lógica dinámica, ya que no se ejecutarán en el documento final. |
| CSS Grid complejo | Preferir `<table>` para layouts tabulares y divs estándar |
| SVG externo `<img src="file.svg">` | Embeber SVG inline `<svg>...</svg>` |
| Caracteres Unicode raros | Verificar que el PDF los renderice |

### Saltos de página

```css
/* Forzar salto antes de un elemento */
.nueva-pagina { page-break-before: always; }

/* Forzar salto después de un elemento */
.terminar-pagina { page-break-after: always; }

/* Evitar salto dentro de un elemento */
.mantener-junto { page-break-inside: avoid; }
```

---

## 5. Plantilla HTML/CSS de Referencia

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <style>
    body { font-family: Arial, sans-serif; padding: 40px; line-height: 1.5; color: #2c3e50; }
    h1 { font-weight: bold; color: #1B365D; border-bottom: 2px solid #1B365D; padding-bottom: 5px; }
    h2 { font-weight: bold; color: #34495e; margin-top: 20px; }
    table { width: 100%; border-collapse: collapse; margin-top: 15px; }
    th { background: #1B365D; color: white; font-weight: bold; padding: 8px 12px; text-align: left; }
    td { padding: 8px 12px; border-bottom: 1px solid #ddd; }
    .page-break { page-break-after: always; }
    .footer { position: relative; margin-top: 40px; font-size: 8pt; color: #999; border-top: 1px solid #eee; padding-top: 5px; text-align: center; }
  </style>
</head>
<body>
  <h1>Reporte Ejecutivo</h1>
  <p>Página 1: Introducción de datos y resumen...</p>
  
  <div class="page-break"></div>
  
  <h2>Detalle de Tabla</h2>
  <table>
    <thead>
      <tr><th>Producto</th><th>Ingresos</th></tr>
    </thead>
    <tbody>
      <tr><td>Suscripción Pro</td><td>$62,000</td></tr>
    </tbody>
  </table>
  <div class="footer">Documento Oficial · Generado por Atlas System</div>
</body>
</html>
```

---

## 6. Lectura y Extracción de PDFs Existentes

Para **leer** un PDF (no crear), usar `pypdf` o `pdfplumber`:

```python
# Extraer texto simple
from pypdf import PdfReader

reader = PdfReader("documento.pdf")
for page in reader.pages:
    print(page.extract_text())

# Extraer tablas
import pdfplumber

with pdfplumber.open("documento.pdf") as pdf:
    for page in pdf.pages:
        tablas = page.extract_tables()
        for tabla in tablas:
            print(tabla)
```

---

## 7. Operaciones sobre PDFs Existentes

Para manipular PDFs ya creados (no crear nuevos):

```python
from pypdf import PdfReader, PdfWriter

# Combinar
writer = PdfWriter()
for archivo in ["doc1.pdf", "doc2.pdf"]:
    for page in PdfReader(archivo).pages:
        writer.add_page(page)
with open("combinado.pdf", "wb") as f:
    writer.write(f)

# Dividir — extraer páginas 1 a 3
reader = PdfReader("input.pdf")
writer = PdfWriter()
for i in range(3):
    writer.add_page(reader.pages[i])
with open("paginas_1_3.pdf", "wb") as f:
    writer.write(f)

# Cifrar
writer.encrypt("password_usuario", "password_admin")

# Rotar
page = reader.pages[0]
page.rotate(90)
```

---

## 10. Checklist Antes de Entregar el PDF

- [ ] HTML tiene `<meta charset="UTF-8">`
- [ ] Todo el CSS está embebido en `<style>` dentro del `<head>`
- [ ] No hay rutas a archivos externos que puedan no existir
- [ ] Se ejecutó la herramienta nativa `compile_html_to_pdf` con éxito
- [ ] El PDF existe y pesa más de 1 KB
- [ ] El contenido dinámico (datos, fechas, tablas) está correctamente interpolado en el HTML