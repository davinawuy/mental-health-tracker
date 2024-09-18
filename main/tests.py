from django.test import TestCase, Client
from django.utils import timezone
from .models import MoodEntry

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
    def test_main_template_uses_correct_page_title(self): # new test
        response = Client().get("/")                    # create an instance of the client and send a GET request to the main page
        html_response = response.content.decode("utf8") # decode the response content to a string
        self.assertIn("PBD Mental Health Tracker", html_response) # check if the string "PBD Mental Health Tracker" is in the response