from django.test import SimpleTestCase
from django.urls import reverse


class FeedbackTests(SimpleTestCase):
    def test_form_opens(self):
        response = self.client.get(reverse('feedback:form'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Send message')

    def test_invalid_form_shows_errors(self):
        response = self.client.post(reverse('feedback:form'), {'name': '', 'email': 'wrong', 'topic': 'other', 'message': 'hi'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form-error')

    def test_valid_form_redirects_to_thanks(self):
        data = {'name': 'Anna', 'email': 'anna@example.com', 'topic': 'project', 'message': 'We need a new website.'}
        response = self.client.post(reverse('feedback:form'), data, follow=True)
        self.assertRedirects(response, reverse('feedback:thanks'))
        self.assertContains(response, 'Thank you, Anna!')
