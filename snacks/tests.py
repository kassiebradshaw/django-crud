from unittest.runner import TextTestRunner
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack
# Create your tests here.

class SnackTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = "tester",
            email = "tester@email.com",
            password="pass"
        )
        self.snack = Snack.objects.create(
            title="Crackers",
            purchaser=self.user,
            description="So many kinds to pick from"
        )

    def test_model_string_representation(self):
        self.assertEqual(str(self.snack), "Crackers")

    def test_model_details(self):
        self.assertEqual(f"{self.snack.title}", "Crackers")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(f"{self.snack.description}", "So many kinds to pick from")
    
    def test_snacks_page(self):
        url = reverse('list_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_detail_page(self):
        response = self.client.get(reverse("detail_view", args="1"))
        self.assertEqual(response.status_code, 200)
    
    def test_snack_list_view(self):
        url = reverse('list_view')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_snack_detail_view(self):
        response = self.client.get(reverse("detail_view", args="1"))
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_create_view(self):
        url = reverse("create_view")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_create.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_update_view(self):
        url = reverse("update_view", args="1")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_update.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_delete_view(self):
        url = reverse("delete_view", args="1")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_delete.html")
        self.assertTemplateUsed(response, 'base.html')
