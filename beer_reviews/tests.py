from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Review

# Create your tests here
class ReviewTests(TestCase):
  @classmethod
  def setUpTestData(cls):
    testyMcTester= get_user_model().objects.create_user(username="testyMcTester", password="retseTcMytset")
    testyMcTester.save()

    test_review = Review.objects.create(
      author = testyMcTester,
      beer_name = "Coors",
      body = "Cold piss",
    )
    test_review.save()
  
  def test_review_content(self):
    review = Review.objects.get(id=1)
    actual_author = str(review.author)
    actual_body = str(review.body)
    actual_beer_name = str(review.beer_name)
    self.assertEqual(actual_author, "testyMcTester")
    self.assertEqual(actual_beer_name, "Coors")
    self.assertEqual(actual_body, "Cold piss")