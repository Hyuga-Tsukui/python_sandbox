
# Create your tests here.

import pytest
# import django.db.transaction

from .models import Question
from datetime import date


@pytest.mark.django_db
class TestSample:

    @classmethod
    @pytest.fixture(autouse=True, scope='class')
    def db_setup(cls, django_db_setup, django_db_blocker):
        with django_db_blocker.unblock():
            for i in range(10000):
                Question.objects.create(question_text=f'test-{i}', pub_date=date(year=2022, month=5, day=2))

    def test__sample(self):
        acutual = Question.objects.filter(question_text='test-0')
        assert acutual[0].question_text == 'test-0'

    def test__sample1(self):
        acutual = Question.objects.filter(question_text='test-1')
        assert acutual[0].question_text == 'test-1'

    def test__sample3(self):
        acutual = Question.objects.filter(question_text='test-2')
        assert acutual[0].question_text == 'test-2'

    def test__sample4(self):
        acutual = Question.objects.filter(question_text='test-3')
        assert acutual[0].question_text == 'test-3'

    def test__sample5(self):
        acutual = Question.objects.filter(question_text='test-4')
        assert acutual[0].question_text == 'test-4'

    def test__sample6(self):
        acutual = Question.objects.filter(question_text='test-5')
        assert acutual[0].question_text == 'test-5'

@pytest.mark.django_db
class TestSample2:

    def test__sample(self):
        acutual = Question.objects.filter(question_text='test-0')
        assert acutual[0].question_text == 'test-0'
