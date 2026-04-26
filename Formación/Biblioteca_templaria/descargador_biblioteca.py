import os
import re
import requests

# ==========================================
# CONFIGURACIÓN DEL DESCARGADOR TEMPLARIO
# ==========================================
INDEX_FILE = 'index.md'
BASE_DIR = 'Descargas_PDF'

def crear_estructura_base():
    """Crea el directorio raíz de descargas si no existe."""
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
        print(f"📁 Directorio base creado: {BASE_DIR}/")

def descargar_archivo(url, ruta_destino):
    """Descarga el archivo desde la URL y lo guarda en la ruta destino."""
    try:
        print(f"Descargando: {os.path.basename(ruta_destino)}...")
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, stream=True, timeout=20)
        response.raise_for_status() 
        
        # Validación estricta: Asegurarse de que el enlace descarga un PDF real y no una página HTML de error
        content_type = response.headers.get('Content-Type', '').lower()
        if 'pdf' not in content_type and 'octet-stream' not in content_type:
            print(f"  ❌ Error: El enlace no contiene un archivo PDF válido (Detectado: {content_type}).")
            return

        with open(ruta_destino, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("  ✅ Descarga completada.")
    except Exception as e:
        print(f"  ❌ Error al descargar desde {url}\n     Detalle: {e}")

def procesar_indice():
    """Lee el index.md, extrae rutas y URLs, y procesa la descarga."""
    if not os.path.exists(INDEX_FILE):
        print(f"❌ Error: No se encontró el archivo '{INDEX_FILE}' en el directorio actual.")
        return

    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    crear_estructura_base()

    # Regex para capturar el nombre sugerido y la URL
    regex_archivo = re.compile(r'`([^`]+\.pdf)`')
    regex_url = re.compile(r'(https?://[^\s\|\]\)]+)')

    for linea in lineas:
        if '|' in linea and '.pdf' in linea:
            match_archivo = regex_archivo.search(linea)
            match_url = regex_url.search(linea)

            if match_archivo:
                nombre_archivo = match_archivo.group(1)
                
                if match_url:
                    url = match_url.group(1)
                    # Extraemos la categoría de los corchetes iniciales (ej. "[Historia general]")
                    tema_match = re.search(r'^\[(.*?)\]', nombre_archivo)
                    tema_carpeta = tema_match.group(1).strip().replace(' ', '_') if tema_match else 'Otros'
                    
                    ruta_carpeta = os.path.join(BASE_DIR, tema_carpeta)
                    if not os.path.exists(ruta_carpeta):
                        os.makedirs(ruta_carpeta)
                        
                    ruta_destino = os.path.join(ruta_carpeta, nombre_archivo)
                    
                    if not os.path.exists(ruta_destino):
                        descargar_archivo(url, ruta_destino)
                    else:
                        print(f"⏭️  Omitiendo (ya existe): {nombre_archivo}")
                else:
                    print(f"⚠️  URL no encontrada para: {nombre_archivo}")

if __name__ == '__main__':
    print("⚔️ INICIANDO AUTOMATIZACIÓN DE BIBLIOTECA TEMPLARIA ⚔️")
    print("-" * 50)
    procesar_indice()
    print("-" * 50)
    print(f"Proceso finalizado. Los PDFs han sido guardados en la carpeta: '{BASE_DIR}'")