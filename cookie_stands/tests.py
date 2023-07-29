from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import CookieStand

class CookieStandModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser', email='test@example.com', password='testpass'
        )
        cls.cookie_stand = CookieStand.objects.create(
            location='Test Location',
            owner=cls.user,
            description='Test Description',
            hourly_sales=[10, 20, 15, 5, 8],
            minimum_customers_per_hour=5,
            maximum_customers_per_hour=30,
            average_cookies_per_sale=1.5,
        )

    def test_str_representation(self):
        self.assertEqual(str(self.cookie_stand), 'Test Location')

    def test_get_absolute_url(self):
        expected_url = reverse('cookie_stands_detail', args=[str(self.cookie_stand.id)])
        self.assertEqual(self.cookie_stand.get_absolute_url(), expected_url)

    def test_owner_is_foreign_key(self):
        self.assertEqual(self.cookie_stand.owner, self.user)

    def test_location_max_length(self):
        max_length = self.cookie_stand._meta.get_field('location').max_length
        self.assertLessEqual(len(self.cookie_stand.location), max_length)

    def test_description_blank(self):
        field = self.cookie_stand._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_hourly_sales_default_list(self):
        self.assertEqual(self.cookie_stand.hourly_sales, [10, 20, 15, 5, 8])

    def test_minimum_customers_per_hour_default_value(self):
        self.assertEqual(self.cookie_stand.minimum_customers_per_hour, 5)

    def test_maximum_customers_per_hour_default_value(self):
        self.assertEqual(self.cookie_stand.maximum_customers_per_hour, 30)

    def test_average_cookies_per_sale_default_value(self):
        self.assertEqual(self.cookie_stand.average_cookies_per_sale, 1.5)
