import os
import sys
import asyncio
import argparse

# Configurar encoding en Windows para prevenir UnicodeEncodeError en la consola
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from playwright.async_api import async_playwright

async def convert_html_to_pdf(input_html: str, output_pdf: str = None, **kwargs):
    """
    Convierte un archivo HTML local a PDF usando Playwright Chromium.
    Soporta argumentos de formato, orientacion, zoom y margenes en mm.
    """
    input_html = os.path.abspath(input_html)
    if not os.path.exists(input_html):
        print(f"Error: Archivo HTML no encontrado: {input_html}", file=sys.stderr)
        sys.exit(1)

    if output_pdf is None:
        output_pdf = os.path.splitext(input_html)[0] + ".pdf"
    output_pdf = os.path.abspath(output_pdf)

    # Asegurar que el directorio de salida existe
    out_dir = os.path.dirname(output_pdf)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    print(f"Cargando HTML desde: {input_html}")
    print(f"Destino del PDF: {output_pdf}")

    page_size = kwargs.get("page_size", "A4").title()
    orientation = kwargs.get("orientation", "Portrait").title()
    landscape = (orientation == "Landscape")
    
    margin_top = kwargs.get("margin_top", 15)
    margin_bottom = kwargs.get("margin_bottom", 15)
    margin_left = kwargs.get("margin_left", 15)
    margin_right = kwargs.get("margin_right", 15)
    
    print_background = not kwargs.get("no_background", False)
    scale = kwargs.get("zoom", 1.0)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1200, "height": 800})
        page = await context.new_page()
        
        file_url = f"file:///{input_html.replace(os.sep, '/')}"
        await page.goto(file_url)
        
        await page.wait_for_load_state("networkidle")
        await page.wait_for_load_state("domcontentloaded")
        await asyncio.sleep(0.5)
        
        await page.pdf(
            path=output_pdf,
            format=page_size,
            landscape=landscape,
            print_background=print_background,
            scale=scale,
            margin={
                "top": f"{margin_top}mm",
                "bottom": f"{margin_bottom}mm",
                "left": f"{margin_left}mm",
                "right": f"{margin_right}mm"
            }
        )
        await browser.close()
        
    size = os.path.getsize(output_pdf)
    print(f"[OK] PDF generado: {output_pdf} ({size / 1024:.1f} KB)")
    return output_pdf

def convert(input_html: str, output_pdf: str = None, **kwargs) -> str:
    """
    Wrapper sincrono para poder importar convert directamente en scripts Python.
    """
    return asyncio.run(convert_html_to_pdf(input_html, output_pdf, **kwargs))

def main():
    parser = argparse.ArgumentParser(
        description="Convierte HTML a PDF usando Playwright Chromium (interfaz compatible con wkhtmltopdf)",
    )
    parser.add_argument("input_html",           help="Archivo HTML de entrada")
    parser.add_argument("output_pdf", nargs="?", help="Archivo PDF de salida (opcional)")
    parser.add_argument("--page-size",    default="A4",      help="Tamaño de pagina: A4, Letter, Legal")
    parser.add_argument("--orientation",  default="Portrait", help="Portrait o Landscape")
    parser.add_argument("--margin-top",   default=15, type=int)
    parser.add_argument("--margin-bottom",default=15, type=int)
    parser.add_argument("--margin-left",  default=15, type=int)
    parser.add_argument("--margin-right", default=15, type=int)
    parser.add_argument("--no-background", action="store_true")
    parser.add_argument("--zoom",         default=1.0, type=float)

    args = parser.parse_args()

    try:
        convert(
            input_html    = args.input_html,
            output_pdf    = args.output_pdf,
            page_size     = args.page_size,
            orientation   = args.orientation,
            margin_top    = args.margin_top,
            margin_bottom = args.margin_bottom,
            margin_left   = args.margin_left,
            margin_right  = args.margin_right,
            no_background = args.no_background,
            zoom          = args.zoom,
        )
        sys.exit(0)
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
