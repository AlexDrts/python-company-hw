from django.test import SimpleTestCase
from django.urls import reverse

from .data import SECTIONS


class SectionsTests(SimpleTestCase):
    def test_sections_open(self):
        for section in SECTIONS:
            response = self.client.get(reverse(f'sections:{section}'))
            self.assertEqual(response.status_code, 200, section)
            self.assertEqual(response.context['active'], section)

    def test_subsections_open(self):
        for section, data in SECTIONS.items():
            for slug, sub in data['subsections'].items():
                response = self.client.get(reverse('sections:subsection', args=[section, slug]))
                self.assertEqual(response.status_code, 200, f'{section}/{slug}')
                self.assertContains(response, sub['title'])

    def test_unknown_pages_return_404(self):
        for url in ['/news/unknown/', '/unknown/services/', '/unknown/', '/a/b/c/']:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404, url)
            self.assertTemplateUsed(response, '404.html')

    def test_missing_slash_redirects(self):
        self.assertRedirects(self.client.get('/news'), '/news/', status_code=301)
        self.assertRedirects(self.client.get('/unknown'), '/unknown/', status_code=301, target_status_code=404)

    def test_contact_redirect(self):
        self.assertRedirects(self.client.get('/contact/'), '/contacts/', status_code=301)
