# ✠ Orden Templaria Ecléctica (OTE)
**Gran Priorato Nacional del Paraguay**

Este repositorio contiene la arquitectura digital, los reglamentos internos, el manual de marca y la estructura web completa del Gran Priorato Nacional del Paraguay de la Orden Templaria Ecléctica (OTE).

## 🗂️ Estructura del Proyecto

El sistema está organizado en áreas operativas, normativas y digitales para facilitar su escalabilidad:

```text
📦 OTE
 ┣ 📜 index.html                  # Portal Web Principal (Página de Inicio)
 ┣ 📂 image/
 ┃ ┗ 📂 logo/                     # Escudos, logos y recursos gráficos (PNG/SVG)
 ┣ 📂 Web_y_Redes/                # Presencia Digital e Identidad
 ┃ ┣ 📜 MANUAL_MARCA.html         # Estética Templaria Clásica v3.0 (Colores y fuentes)
 ┃ ┣ 📜 formulario_ingreso.html   # Sistema integrado de postulación
 ┃ ┣ 📜 ESTRATEGIA_REDES.html     # Planificación de Social Media
 ┃ ┗ 📜 LISTA_VERIFICACION.html   # Auditoría de canales y dominios
 ┣ 📂 Reglamentos/                # Normativa y Estructura Organizacional
 ┃ ┣ 📜 ESTATUTOS_GENERALES.html  # Leyes fundamentales de la Orden
 ┃ ┣ 📜 SISTEMA_INTEGRAL.html     # Modelo integral de grados, ciclos y operación
 ┃ ┣ 📜 ORGANIGRAMA_VISUAL.html   # Jerarquía gráfica de la OTE
 ┃ ┗ 📜 PROMPT_MAESTRO.md         # Motor base de IA para generación documental
 ┣ 📂 Prioratos_Regionales/       # Sub-divisiones Territoriales Multisito
 ┃ ┣ 📜 LISTA_PRIORATOS.html      # Directorio de Prioratos y Encomiendas
 ┃ ┣ 📜 priorato_pax.html         # Subpágina: Priorato Regional de Pax
 ┃ ┗ 📜 priorato_santo_grial.html # Subpágina: Priorato Santo Grial
 ┣ 📂 Origen/                     # Documentos Fundacionales
 ┃ ┣ 📜 CARTA_FUNDACIONAL.md
 ┃ ┣ 📜 JURAMENTO_ESCUDERO.md
 ┃ ┗ 📜 CONVOCATORIA_OFICIAL.md
 ┣ 📂 Calendarios/
 ┃ ┗ 📜 CALENDARIO_OPERATIVO.md   # Ciclos semanales, mensuales y litúrgicos
 ┗ 📂 Rituales/
   ┗ 📜 RITUAL_INICIACION_ESCUDERO.md
```

## 🎨 Diseño y Estética Visual

Todo el ecosistema web estático está desarrollado respetando estrictamente el **Manual de Marca v3.0 (Estética Templaria Clásica)** de la Orden, logrando un balance entre elegancia histórica y legibilidad moderna.

- **Fondo Base:** Textura Pergamino (`#f4f1ea`)
- **Texto Principal:** Gris Oscuro (`#2c2c2c`)
- **Acento de Autoridad:** Rojo Templario (`#9b111e`) para la Cruz, botones y títulos.
- **Acento Esotérico:** Lila Templario (`#9370db`) para interacciones (hovers) y heráldica específica.
- **Tipografías Oficiales:** *Cinzel* (Titulares y Menús) y *EB Garamond* (Cuerpos de texto).

## 🚀 Despliegue y Uso

Este proyecto ha sido diseñado de manera modular utilizando tecnologías estándar de la web (**HTML5, CSS3, Vanilla JS**) sin depender de frameworks pesados, lo que asegura rapidez de carga, durabilidad a largo plazo y facilidad de lectura multiplataforma.

### Ejecución Local
1. Clona este repositorio o descárgalo en tu equipo.
2. Abre el archivo `index.html` en tu navegador web moderno de preferencia.
3. Navega por todas las secciones, prioratos y reglamentos de manera nativa utilizando los enlaces integrados.

### Arquitectura Futura
El proyecto está estructurado para soportar un **despliegue multisitio (Multi-tenant)** en plataformas como Vercel o Netlify, permitiendo la utilización de subdominios locales (ej. `prioratodepax.oteparaguay.org`) que apunten a sus respectivos módulos dentro de este mismo código fuente.

---

<div align="center">
  <i>"Non nobis, Domine, non nobis, sed Nomini Tuo da gloriam"</i>
</div>