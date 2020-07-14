import datetime
from django.test import TestCase

from .models import Paper


class DateCastTestCase(TestCase):
    ''' Test the capability of casting the string publish_time
        into its datefield version publish_date
    '''

    def test_valid_date(self):
        paper = Paper.objects.create(publish_time='2001-01-02')
        self.assertEqual(paper.publish_date, datetime.date(2001, 1, 2))

    def test_valid_year(self):
        paper = Paper.objects.create(publish_time='2001')
        self.assertEqual(paper.publish_date, datetime.date(2001, 1, 1))

    def test_invalid_digit(self):
        paper = Paper.objects.create(publish_time='5')
        self.assertEqual(paper.publish_date, None)

    def test_invalid_string(self):
        paper = Paper.objects.create(publish_time='not valid')
        self.assertEqual(paper.publish_date, None)
