from django.test import TestCase, Client
from django.utils import timezone
from .models import MoodEntry
from django.contrib.auth.models import User


class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self):
        now = timezone.now()
        mood = MoodEntry.objects.create(
          mood="Happy",
          time = now,
          feelings = "I'm happy, even though my clothes are soaked from the rain :(",
          mood_intensity = 8,
        )
        self.assertTrue(mood.is_mood_strong)

    #testing the main page

    def test_main_template_uses_correct_page_title(self):
        self.user = User.objects.create_user(username='Admin', password='Y62hhBkYD_@ACTH')

        # Log in the client
        self.client.login(username='Admin', password='Y62hhBkYD_@ACTH')

        self.client.cookies['last_login'] = '2024-09-20 00:00:00'

        response = self.client.get("/")
        html_response = response.content.decode("utf8")
        self.assertIn("PBD Mental Health Tracker", html_response)