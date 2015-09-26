from django.test import TestCase
from .views import ViewsCounterGet, ViewsCounterMain

class ViewsTests(TestCase):

    def test_ViewsCounterGet(self):
	
        self.assertEqual(1, 1)
