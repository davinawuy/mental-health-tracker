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

    def test_main_template_uses_correct_page_title(self): # Test the main page title
        self.user = User.objects.create_user(username='Admin', password='Y62hhBkYD_@ACTH') # Create a user

        # Log in the client user into the website
        self.client.login(username='Admin', password='Y62hhBkYD_@ACTH') #login the user

        # Set the last login time so the user is not redirected to the login page
        self.client.cookies['last_login'] = '2024-09-21 00:00:00' # Set the last login time

        # Get the response from the page
        response = self.client.get("/") # Get the client response
        html_response = response.content.decode("utf8") # Decode the response
        self.assertIn("PBD Mental Health Tracker", html_response) # Check if the response contains the title