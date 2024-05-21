from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

USER_DATA = {
        "email": "TestUser@softuni.bg",
        "password": "TestPassword"
    }
User = get_user_model()
class ProductCreateViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            email=USER_DATA['email'],
            password=USER_DATA['password'],
            first_name='Test',
            last_name='User',
            name_farm='Test Farm'
        )

    def test_get_create__when_logged_in_user__expect_200_and_correct_template(self):
        # Login the user
        self.client.login(email=USER_DATA['email'], password=USER_DATA['password'])
        # Act
        response = self.client.get(reverse("create product"))
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product-add-page.html")
    def test_get_create__when_anonymous_user__expect_302_with_redirect_to_login(self):
        pass
    def test_post_create__when_logged_in_user__expect_200_and_correct_redirect(self):
        pass
