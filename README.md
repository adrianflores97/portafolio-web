# Portafolio web — primera versión

Sitio estático responsive para presentar perfil, servicios y proyectos del portafolio freelance. No requiere framework, backend, build, base de datos, claves ni servicios de pago.

## Estado

**MVP inicial / plantilla personalizable.** Los cuatro proyectos de la web están marcados **Planificado** y no se enlazan a repositorios inexistentes. El enlace principal de la sección de contacto lleva a GitHub. **Todavía falta configurar un canal de contacto real**; no afirma que GitHub permita mensajes directos.

## Estructura

```text
portafolio-web/
├── index.html
├── css/styles.css
├── js/main.js
├── assets/favicon.svg
├── tests/test_site.py
├── .nojekyll
├── .gitignore
└── README.md
```

## Personalización obligatoria

El nombre público **Adrian Flores** y el usuario **adrianflores97** ya están incorporados.

- Revisa los textos y corrige cualquier afirmación con la que no te identifiques.
- **Canal de contacto:** aún no configurado. Cuando lo elijas, adapta `#contacto` sin publicar datos privados.

Revisa también títulos, descripciones y experiencia; publica exclusivamente afirmaciones que puedas respaldar. No incluyas datos de tu empleo o de clientes.

**Importante:** Esta versión no incluye un formulario ni un correo inventado. El enlace de GitHub es para ver código, no para iniciar una conversación de manera garantizada.

## Ejecutar localmente

Desde la carpeta `portafolio-web`:

```bash
python -m http.server 8000
```

Abre `http://localhost:8000/` en un navegador. Detén el servidor con `Ctrl+C`.

## Comprobaciones automáticas locales

```bash
python -m unittest discover -s tests -v
```

Estas comprobaciones revisan archivos y estructura básica; **no** sustituyen pruebas visuales, de accesibilidad o de despliegue real.

## Publicar en GitHub Pages

1. Crea el repositorio público `freelance-tech-portfolio` vacío (sin README inicial).
2. Desde esta carpeta, tras personalizar los datos:

```bash
git init
git add .
git commit -m "feat: primera versión del portafolio web"
git branch -M main
git remote add origin https://github.com/adrianflores97/freelance-tech-portfolio.git
git push -u origin main
```

3. En GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**.
4. Selecciona **Branch: main** y carpeta **/(root)**. Guarda.
5. Comprueba la URL `https://adrianflores97.github.io/freelance-tech-portfolio/` cuando GitHub haya terminado de publicar.

La URL solo estará disponible después de crear el repositorio y configurar Pages. GitHub Pages no ejecuta código backend; este sitio no tiene formulario que almacene datos.

## Futuras mejoras

1. Enlazar P1 cuando tenga código, README y evidencia de prueba.
2. Agregar capturas reales y casos de estudio.
3. Optimizar textos para el tipo de clientes que respondan a las propuestas.
4. Si hiciera falta, agregar dominio propio y analítica respetuosa con privacidad.
