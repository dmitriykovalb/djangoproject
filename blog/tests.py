from django.test import TestCase
from .models import Posts
import unittest
from datetime import datetime


class DateTestCase(TestCase):

    def test_date(self):
        dt = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')[:-3]
        a = Posts()
        self.assertEqual(a.date, dt)

    def test_title(self):
        a = Posts()
        self.assertTrue(len(a.title) <= 100)
