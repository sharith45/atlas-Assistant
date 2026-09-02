---
name: Generación de Presentaciones PowerPoint (PPTX)
description: Sistema completo maestro de generación de presentaciones ejecutivas, científicas y corporativas en PowerPoint (PPTX) mediante ejecución directa de scripts Python (python-pptx). Incluye arquitectura de narrativa (Story Arc), diseño visual Card-Based 16:9, retícula cartesiana, reglas anti-bugs, patrones de layout (2/3 columnas, KPIs, Split 50/50, Timelines), integración de visuales/IA y protocolo de validación QA.
enabled: true
---

# Sistema Maestro de Generación PPTX para ATLAS — Ejecución Directa Python (.py)

ATLAS genera cualquier presentación profesional de alto impacto (ejecutiva, científica, startup, institucional, ventas) mediante **ejecución directa de scripts Python (`python-pptx`)**. Utiliza coordenadas cartesianas exactas, maquetación basada en tarjetas (Card-Based System), badges anidados, jerarquía tipográfica estricta y plantillas de código anti-bugs.

---

## 🏛️ 1. FILOSOFÍA "VISUAL-FIRST" Y ARQUETIPOS DE NARRATIVA (STORY ARC)

### Principios Fundamentales de Diseño
- **60-70% Contenido Visual / 30-40% Texto**: Las diapositivas son un soporte visual, no un documento de lectura denso.
- **Espacio en Blanco Generoso (40-50%)**: Dejar respirar el diseño. El desorden visual reduce la retención y el impacto.
- **Regla del Punto Único**: Cada diapositiva debe transmitir **una sola idea principal** bien definida.
- **Regla 3-4-6**: Máximo **3 a 4 puntos o tarjetas por diapositiva**, con **4 a 6 palabras clave por viñeta**. Cero párrafos largos.

### Arco Narrativo Universal
1. **Hook / Gancho (30-60 seg)**: Capturar la atención con un dato impactante o pregunta provocadora.
2. **Contexto & Justificación (10%)**: Establecer la importancia del tema apoyado en datos o literatura.
3. **El Problema / Brecha (10%)**: Definir claramente la necesidad o el riesgo a resolver.
4. **Solución / Enfoque (20%)**: Explicar la metodología, producto o estrategia propuesta.
5. **Resultados & Evidencia (40-50%)**: *La sección principal*. Métricas clave, gráficos, demostraciones y logros.
6. **Implicaciones & Proyección (10%)**: Significado a futuro, ROI o próximos pasos.
7. **Cierre Memorable & Q&A (5%)**: Conclusión clara, llamada a la acción y datos de contacto.

### Estructuras Según el Tipo de Presentación
- **Ejecutiva / Corporativa**: Portada → Resumen Ejecutivo (KPIs) → Problema → Estrategia → Resultados Financieros/Operativos → Próximos Pasos.
- **Pitch Deck (Startup / Inversionistas)**: Problema → Solución → Tamaño de Mercado (TAM/SAM/SOM) → Modelo de Negocio → Tracción/Métricas → Equipo → Petición de Inversión (Ask).
- **Científica / Académica / Conferencia**: Título → Introducción & Antecedentes (citas) → Hipótesis → Metodología → Resultados Clave (gráficos) → Discusión → Conclusión & Agradecimientos.
- **Ventas / Demo Comercial**: Gancho → Dolor del Cliente → Solución / Caso de Éxito → Demostración de Funcionalidades → Comparación vs Competencia → Pricing & CTA.

---

## 🎨 2. SISTEMA DE DISEÑO VISUAL Y PALETAS DE COLOR

### Paleta Principal: Dark Mode Moderno / SaaS Dashboard (Predeterminada)
- **Fondo General (`bg_main`)**: Dark Slate / Navy (`#0F172A` -> RGB: `15, 23, 42`)
- **Tarjetas / Contenedores (`card_bg`)**: Dark Blue Card (`#1E293B` -> RGB: `30, 41, 59`)
- **Contenedores de Acento / Badges (`badge_bg`)**: Slate Accent (`#334155` -> RGB: `51, 65, 85`)
- **Texto Primario (`text_primary`)**: Blanco Puro (`#F1F5F9` -> RGB: `241, 245, 249`)
- **Texto Secundario (`text_secondary`)**: Muted Gray (`#94A3B8` -> RGB: `148, 163, 184`)
- **Colores de Acento**:
  - **Electric Cyan (`#38BDF8` / RGB: `56, 189, 248`)**: Categorías, bordes clave, números destacados.
  - **Success Green (`#4ADE80` / RGB: `74, 222, 128`)**: Métricas positivas, logros, soluciones.
  - **Danger Red (`#F87171` / RGB: `248, 113, 113`)**: Alertas, riesgos, competidores, problemas.

### Paletas Alternativas Según el Dominio
- **Executive Clean (Light Mode)**: Fondo `#F8FAFC`, Tarjetas `#FFFFFF`, Texto `#0F172A`, Acento Azul `#2563EB`.
- **Deep Emerald (Biotech / Salud / Sostenibilidad)**: Fondo `#064E3B`, Tarjetas `#047857`, Texto `#ECFDF5`, Acento Verde Lima `#34D399`.
- **Cybersecurity / Tech Dark**: Fondo `#090D16`, Tarjetas `#111827`, Texto `#F9FAFB`, Acento Violeta `#8B5CF6`.

> [!IMPORTANT]
> **Regla de Contraste WCAG 4.5:1 / 7:1**: Asegurar siempre un alto contraste entre texto y fondo. Nunca usar texto gris oscuro sobre fondos oscuros o texto claro sobre fondos blancos.

---

## 📐 3. REGLAS DE ORO DE MAQUETACIÓN (16:9 WIDESCREEN - 13.333" x 7.5")

1. **Márgenes Estándar (Geometría Cartesiana)**:
   - Margen Izquierdo: `Inches(0.8)`
   - Ancho Útil: `Inches(11.733)`
   - Alto Útil: `Inches(6.5)`
   - Header Y Categoría: `Inches(0.5)`
   - Header Y Título Principal: `Inches(0.85)`

2. **Header Estructurado (Obligatorio en todas excepto Portada)**:
   - **Categoría (Tag Superior)**: `11pt` Bold, All-Caps, Color Acento (Cian `#38BDF8`).
   - **Título Principal**: `26pt` Bold, Color Blanco (`#F1F5F9`), Alto `Inches(0.8)`.

3. **Tarjetas y Contenedores (Card-Based Design)**:
   - TODO bloque de información relevante DEBE ir dentro de un contenedor `MSO_SHAPE.ROUNDED_RECTANGLE`.
   - Prohibido dejar texto flotando libremente sobre el fondo base sin tarjeta.
   - Fondo de tarjeta: `#1E293B` con borde de `1.5pt` (`#334155` o color de acento).
   - **Padding Interno**: Desfase de `0.25"` entre los bordes de la tarjeta y la caja de texto interna (`left + Inches(0.25)`, `top + Inches(0.25)`).

4. **Tipografía, Jerarquía y Alineación Estricta**:
   - Fuente Base: `Calibri`, `Segoe UI` o `Arial`.
   - Títulos de Diapositiva: `26pt` Bold.
   - Títulos de Tarjeta: `16pt - 18pt` Bold.
   - Métricas / Números Gigantes: `36pt - 44pt` Bold Cyan/Green.
   - Cuerpo de Texto / Viñetas: `12pt - 13pt` Regular, Muted Gray (`#94A3B8`), `space_before = Pt(6)`.
   - **Alineación**: **Alineación a la Izquierda (`PP_ALIGN.LEFT`) por defecto** para máxima legibilidad. Centrado únicamente en Badges numéricos o KPIs.

---

## 🧩 4. CATÁLOGO DE PATRONES DE LAYOUTS EJECUTIVOS (COORDENADAS PYTHON)

### Patrón A: Layout de 3 Columnas (Grid de Tarjetas)
Ideal para comparar 3 pilares, servicios, características o etapas.
- `col_width = Inches(3.64)`
- `col_gap = Inches(0.4)`
- `top = Inches(1.8)`, `height = Inches(5.0)`
- Columna 1: `left = Inches(0.8)`
- Columna 2: `left = Inches(0.8) + Inches(3.64) + Inches(0.4) = Inches(4.84)`
- Columna 3: `left = Inches(4.84) + Inches(3.64) + Inches(0.4) = Inches(8.88)`

### Patrón B: Layout Métricas Clave / KPIs (Big Number Cards)
Ideal para tracción, resultados financieros y métricas principales.
- 4 Tarjetas horizontales de `width = Inches(2.68)`, `gap = Inches(0.33)`.
- Cada tarjeta contiene:
  - Badge Superior: Categórica en `11pt` Bold.
  - Valor Gigante: `38pt` Bold (Cian o Verde).
  - Descripción: `11pt` Muted Gray.

### Patrón C: Split 50/50 (Visual a la Izquierda / Tarjeta a la Derecha)
Ideal para presentar diagramas, capturas de pantalla o imágenes junto con viñetas explicativas.
- Columna Izquierda (Imagen/Gráfico): `left = Inches(0.8)`, `width = Inches(5.6)`, `top = Inches(1.8)`, `height = Inches(5.0)`.
- Columna Derecha (Card de Texto): `left = Inches(6.8)`, `width = Inches(5.733)`, `top = Inches(1.8)`, `height = Inches(5.0)`.

### Patrón D: Timeline / Proceso Secuencial Horizontal
Ideal para fases de proyectos, roadmaps o pasos metodológicos.
- 4 Bloques horizontales alineados a `top = Inches(2.2)`, `height = Inches(4.2)`.
- Indicadores numéricos superiores (`01`, `02`, `03`, `04`) en Badges destacados.

---

## ⚡ 5. PLANTILLA BASE DE CÓDIGO PYTHON (BOILERPLATE ANTI-BUGS)

El script Python generado DEBE utilizar esta **plantilla sólida y libre de errores de importación**:

```python
import os
import sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN          # 🚨 OBLIGATORIO: PP_ALIGN (NO WD_PARAGRAPH_ALIGNMENT)
from pptx.enum.shapes import MSO_SHAPE

# Configuración de codificación para consola Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# 🚨 RUTAS RELATIVAS SÓLIDAS (CERO PATH TRAVERSAL)
SCRIPT_DIR = Path(__file__).parent
OUTPUT_FILE = SCRIPT_DIR / "presentacion_ejecutiva.pptx"

# PALETA DARK MODE NAVY / SAAS DASHBOARD
COLORS = {
    "bg_main": RGBColor(15, 23, 42),       # Dark Slate background
    "card_bg": RGBColor(30, 41, 59),       # Dark Blue Card
    "badge_bg": RGBColor(51, 65, 85),      # Slate Accent / Badge
    "text_primary": RGBColor(241, 245, 249), # White text
    "text_secondary": RGBColor(148, 163, 184), # Muted Gray text
    "accent_cyan": RGBColor(56, 189, 248),   # Cyan Accent
    "success_green": RGBColor(74, 222, 128), # Green Accent
    "danger_red": RGBColor(248, 113, 113),   # Red Accent
}

FONT_BASE = "Segoe UI"

def set_slide_background(slide, color: RGBColor):
    """Establece el color de fondo sólido en la diapositiva."""
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_card(slide, left, top, width, height, bg_color: RGBColor, border_color: RGBColor = None, border_size: float = 1.5):
    """Crea un contenedor redondeado (Card-Based System)."""
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(border_size)
    else:
        shape.line.fill.background()
    return shape

def add_header(slide, categoria: str, titulo: str):
    """Encabezado estandarizado seguro de 2 niveles sin placeholders."""
    # Tag / Categoría Superior
    tx_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.733), Inches(0.35))
    tf_c = tx_cat.text_frame
    tf_c.word_wrap = True
    p_c = tf_c.paragraphs[0]
    p_c.text = categoria.upper()
    p_c.font.name = FONT_BASE
    p_c.font.size = Pt(11)
    p_c.font.bold = True
    p_c.font.color.rgb = COLORS["accent_cyan"]

    # Título Principal
    tx_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.733), Inches(0.75))
    tf_t = tx_t.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = titulo
    p_t.font.name = FONT_BASE
    p_t.font.size = Pt(26)
    p_t.font.bold = True
    p_t.font.color.rgb = COLORS["text_primary"]

def add_bullet_point(tf, title: str, body: str):
    """Agrega un punto con título en negrita y cuerpo explicativo conciso."""
    p = tf.add_paragraph()
    p.space_before = Pt(8)
    
    # Run Título
    r1 = p.add_run()
    r1.text = title + ": "
    r1.font.name = FONT_BASE
    r1.font.size = Pt(13)
    r1.font.bold = True
    r1.font.color.rgb = COLORS["text_primary"]

    # Run Cuerpo
    r2 = p.add_run()
    r2.text = body
    r2.font.name = FONT_BASE
    r2.font.size = Pt(12)
    r2.font.bold = False
    r2.font.color.rgb = COLORS["text_secondary"]

def main():
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    blank_layout = prs.slide_layouts[6]  # 🚨 OBLIGATORIO: Usar layout 6 en blanco

    # ----------------------------------------------------
    # SLIDE 1: PORTADA EJECUTIVA
    # ----------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, COLORS["bg_main"])
    
    # Tarjeta Principal Portada
    add_card(s1, Inches(1.5), Inches(1.5), Inches(10.333), Inches(4.5), COLORS["card_bg"], COLORS["accent_cyan"], 2.0)
    
    tx_portada = s1.shapes.add_textbox(Inches(2.0), Inches(2.2), Inches(9.333), Inches(3.0))
    tf1 = tx_portada.text_frame
    tf1.word_wrap = True
    
    p0 = tf1.paragraphs[0]
    p0.text = "INFORME ESTRATÉGICO Y EJECUTIVO"
    p0.font.name = FONT_BASE
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = COLORS["accent_cyan"]
    
    p1 = tf1.add_paragraph()
    p1.space_before = Pt(12)
    p1.text = "Título de la Presentación Ejecutiva"
    p1.font.name = FONT_BASE
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = COLORS["text_primary"]

    p2 = tf1.add_paragraph()
    p2.space_before = Pt(10)
    p2.text = "Subtítulo explicativo o resumen del alcance del proyecto"
    p2.font.name = FONT_BASE
    p2.font.size = Pt(16)
    p2.font.color.rgb = COLORS["text_secondary"]

    # ----------------------------------------------------
    # SLIDE 2: CONTENIDO EN 3 TARJETAS (GRID LAYOUT)
    # ----------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, COLORS["bg_main"])
    add_header(s2, "ANÁLISIS ESTRATÉGICO", "Pilares Clave del Proyecto")

    col_w = Inches(3.64)
    col_gap = Inches(0.4)
    top_pos = Inches(1.8)
    h_pos = Inches(5.0)

    columns_data = [
        {"cat": "PILAR 01", "title": "Innovación Tecnológica", "bullets": [("Arquitectura SaaS", "Escalabilidad en la nube."), ("Integración API", "Conexión fluida de datos.")]},
        {"cat": "PILAR 02", "title": "Eficiencia Operativa", "bullets": [("Automatización", "Reducción de tiempos en 40%."), ("Optimización", "Uso eficiente de recursos.")]},
        {"cat": "PILAR 03", "title": "Seguridad & Compliance", "bullets": [("Cifrado E2E", "Protección de datos críticos."), ("Auditoría WCAG", "Accesibilidad garantizada.")]}
    ]

    for idx, col in enumerate(columns_data):
        left_pos = Inches(0.8) + idx * (col_w + col_gap)
        add_card(s2, left_pos, top_pos, col_w, h_pos, COLORS["card_bg"], COLORS["badge_bg"], 1.5)
        
        # Texto interno
        tx_box = s2.shapes.add_textbox(left_pos + Inches(0.25), top_pos + Inches(0.25), col_w - Inches(0.5), h_pos - Inches(0.5))
        tf = tx_box.text_frame
        tf.word_wrap = True
        
        # Categoría
        p_c = tf.paragraphs[0]
        p_c.text = col["cat"]
        p_c.font.name = FONT_BASE
        p_c.font.size = Pt(11)
        p_c.font.bold = True
        p_c.font.color.rgb = COLORS["accent_cyan"]
        
        # Título Columna
        p_t = tf.add_paragraph()
        p_t.space_before = Pt(4)
        p_t.text = col["title"]
        p_t.font.name = FONT_BASE
        p_t.font.size = Pt(18)
        p_t.font.bold = True
        p_t.font.color.rgb = COLORS["text_primary"]
        
        # Viñetas
        for b_title, b_body in col["bullets"]:
            add_bullet_point(tf, b_title, b_body)

    # Guardar archivo final
    prs.save(str(OUTPUT_FILE))
    print(f"✅ [OK] Presentación generada exitosamente: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
```

---

## 🚫 6. REGLAS ANTI-ERRORES DE CÓDIGO (LECCIONES DE AUDITORÍA)

1. **🚨 NUNCA importar `WD_PARAGRAPH_ALIGNMENT`**: Ese módulo pertenece a `python-docx` (Word). En PowerPoint se debe importar **estrictamente `from pptx.enum.text import PP_ALIGN`** (`PP_ALIGN.LEFT`, `PP_ALIGN.CENTER`).
2. **🚨 PROHIBIDO usar `slide.placeholders` en `slide_layouts[6]`**: El layout 6 es en blanco y NO contiene placeholders (`KeyError: no placeholder on this slide`). Todo elemento debe crearse dinámicamente con `slide.shapes.add_textbox(...)` o `add_card(...)`.
3. **🚨 Asignación de Espaciado `space_before` y `space_after`**: Usar siempre `paragraph.space_before = Pt(integer)` con valores en puntos (`Pt(0)` a `Pt(36)`). NUNCA asignar enteros crudos de OpenXML ni EMUs.
4. **🚨 Ajuste Obligatorio `word_wrap = True`**: Activar siempre `text_frame.word_wrap = True` en todas las cajas de texto para evitar que el texto sobrepase horizontalmente el ancho de las tarjetas.
5. **🚨 Definición Sólida de Rutas**: Usar siempre `Path(__file__).parent / "nombre_archivo.pptx"` para evitar errores de directorio o path traversal (`workspace/workspace/...`).
6. **🚨 Edición Limpia sin Micro-Parches**: Si necesitas ajustar la maquetación, tamaños de fuente o espaciados de un script de PowerPoint, **reescribe la función o el script completo usando `write_file`** en lugar de aplicar múltiples micro-parches de una sola línea (`edit_file_patch`), ya que son propensos a fallos por diferencias de formato e indentación.
7. **⚡ Protocolo de Ejecución en 3 Turnos Max**:
   - Turno 1: Escribir el script Python `generar_presentacion_[tema].py` en la raíz del workspace activo con la plantilla base.
   - Turno 2: Ejecutar el script mediante `python generar_presentacion_[tema].py`.
   - Turno 3: Notificar al usuario con el enlace directo al archivo `.pptx` generado.

---

## 🖼️ 7. INTEGRACIÓN DE VISUALES E ILUSTRACIONES (IMÁGENES Y DIAGRAMAS)

Cuando la diapositiva requiera elementos visuales externos (diagramas, capturas de pantalla, esquemas o imágenes generadas por IA):

1. **Inserción de Imágenes en Tarjetas**:
   ```python
   # Inserción con margen interno dentro de una celda/card
   slide.shapes.add_picture(
       "ruta/a/imagen.png",
       left=left_pos + Inches(0.25),
       top=top_pos + Inches(1.2),
       width=col_w - Inches(0.5)
   )
   ```
2. **Uso del Patrón Split 50/50**: Colocar el elemento gráfico a la izquierda (`Inches(0.8)`) cubriendo el 50% del espacio horizontal, y la tarjeta de texto explicativo a la derecha (`Inches(6.8)`).
3. **Imágenes de Fondo**: En caso de requerir un fondo visual ilustrativo en la portada, usar imágenes en alta resolución con superposición de tarjeta oscura para preservar el contraste WCAG del texto.

---

## 🔍 8. VALIDACIÓN VISUAL Y CONTROL DE CALIDAD (QA)

Antes de entregar la presentación al usuario, se debe aplicar la siguiente lista de verificación (QA Checklist):

### Lista de Verificación Visual (QA Checklist)
- [ ] **Sin Texto Cortado**: Ningún título o texto sobrepasa los bordes de la tarjeta ni del slide (`word_wrap = True`).
- [ ] **Sin Solapamientos**: Ninguna caja de texto cubre una imagen o badge.
- [ ] **Contraste Seguro**: Todo el texto es perfectamente legible (Texto claro sobre tarjeta oscura `#1E293B`).
- [ ] **Jerarquía Visual Clara**: Categoría (11pt Bold Cyan) → Título (26pt Bold Blanco) → Subtítulo/Card (16pt Bold) → Cuerpo (12pt Muted Gray).
- [ ] **Formato Widescreen 16:9**: `prs.slide_width = Inches(13.333)`, `prs.slide_height = Inches(7.5)`.
- [ ] **Alineación Consistente**: Todo el contenido principal alineado a la izquierda (`PP_ALIGN.LEFT`).
- [ ] **Regla 3-4-6**: Ninguna tarjeta contiene párrafos gigantes de texto continuo.

---

## ⏱️ 9. CONTROL DE TIEMPOS, PACING Y PREPARACIÓN DE LA PRESENTACIÓN

- **Regla de 1 Diapositiva por Minuto**: Para una presentación de 15 minutos, planificar entre **12 y 15 diapositivas máximo**.
- **Distribución Estratégica de Diapositivas**:
  - Introducción y Contexto: 2 - 3 slides (15%)
  - Metodología / Enfoque: 2 - 3 slides (15%)
  - Resultados Clave / Evidencia: 6 - 8 slides (50%)
  - Implicaciones & Cierre: 2 - 3 slides (20%)
- **Diapositivas de Respaldo (Backup Slides)**: Colocar anexos detallados al final de la presentación tras la diapositiva de cierre para responder preguntas complejas durante la sesión de Q&A.
