"""Pruebas de humo de estructura; no prueban UX ni producción."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PortfolioSmokeTests(unittest.TestCase):
    def test_required_files(self):
        for relative in ('index.html', 'css/styles.css', 'js/main.js', 'assets/favicon.svg'):
            with self.subTest(file=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_content_sections(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        for section in ('servicios', 'proyectos', 'sobre-mi', 'contacto'):
            with self.subTest(section=section):
                self.assertIn(f'id="{section}"', html)

    def test_projects_are_not_misrepresented(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertEqual(html.count('class="project-status">Planificado'), 4)
        self.assertIn('No se publican resultados ni repositorios ficticios', html)

    def test_github_username_is_personalized(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertIn('https://github.com/adrianflores97', html)
        self.assertNotIn('TU_USUARIO_GITHUB', html)
        self.assertNotIn('TU_CORREO@ejemplo.com', html)

    def test_professional_identity(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertIn('Adrian Flores', html)
        self.assertNotIn('TU_NOMBRE', html)

    def test_linked_local_assets_exist(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        for asset in ('css/styles.css', 'js/main.js', 'assets/favicon.svg'):
            with self.subTest(asset=asset):
                self.assertTrue((ROOT / asset).is_file())
                self.assertIn(f'./{asset}', html)


if __name__ == '__main__':
    unittest.main()
