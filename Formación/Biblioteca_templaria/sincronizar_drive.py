import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# ==========================================
# CONFIGURACIÓN DE SINCRONIZACIÓN OTE
# ==========================================

# El ID de la carpeta extraído de tu enlace (1KVHLjfgQemvAr_odxRm8bgUF0uP9ypNN)
ID_CARPETA_DRIVE = '1KVHLjfgQemvAr_odxRm8bgUF0uP9ypNN'

# Ruta de tu carpeta local en la PC
RUTA_LOCAL = r'C:\Users\HP 250 G10\Documents\GITHUT\OTE\Formación'

def autenticar_drive():
    """Maneja la autenticación con la API de Google Drive."""
    print("🔐 Verificando credenciales de Google Drive...")
    gauth = GoogleAuth()
    
    # Intenta cargar credenciales guardadas previamente
    gauth.LoadCredentialsFile("credenciales_drive.txt")
    
    if gauth.credentials is None:
        # Autentica mediante el navegador si no hay credenciales
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresca el token si ha expirado
        gauth.Refresh()
    else:
        # Autoriza con las credenciales existentes
        gauth.Authorize()
        
    # Guarda las credenciales para la próxima ejecución
    gauth.SaveCredentialsFile("credenciales_drive.txt")
    return GoogleDrive(gauth)

def subir_archivos(drive):
    """Lee la carpeta local y sube los archivos a Drive."""
    print(f"📂 Escaneando carpeta local: {RUTA_LOCAL}")
    
    if not os.path.exists(RUTA_LOCAL):
        print(f"⚠️ La carpeta no existe. Creando directorio local: {RUTA_LOCAL}")
        os.makedirs(RUTA_LOCAL)

    # Obtener lista de archivos que ya están en la carpeta de Drive para no duplicar
    query = f"'{ID_CARPETA_DRIVE}' in parents and trashed=false"
    archivos_en_drive = drive.ListFile({'q': query}).GetList()
    nombres_en_drive = {archivo['title']: archivo['id'] for archivo in archivos_en_drive}

    archivos_locales = os.listdir(RUTA_LOCAL)
    
    for nombre_archivo in archivos_locales:
        ruta_completa = os.path.join(RUTA_LOCAL, nombre_archivo)
        
        # Solo procesamos archivos, no subcarpetas en este script básico
        if os.path.isfile(ruta_completa):
            if nombre_archivo in nombres_en_drive:
                print(f"⏭️ Omitiendo (Ya existe en Drive): {nombre_archivo}")
                # Opcional: Aquí podrías agregar lógica para actualizar el archivo si fue modificado
            else:
                print(f"☁️ Subiendo nuevo archivo: {nombre_archivo}...")
                nuevo_archivo = drive.CreateFile({
                    'title': nombre_archivo,
                    'parents': [{'id': ID_CARPETA_DRIVE}]
                })
                nuevo_archivo.SetContentFile(ruta_completa)
                nuevo_archivo.Upload()
                print("  ✅ Subida exitosa.")

if __name__ == '__main__':
    print("⚔️ INICIANDO SINCRONIZADOR TEMPLARIO (PC <-> DRIVE) ⚔️")
    print("-" * 50)
    
    # 1. Autenticar
    drive_app = autenticar_drive()
    # 2. Ejecutar subida
    subir_archivos(drive_app)
    
    print("-" * 50)
    print("Sincronización finalizada.")