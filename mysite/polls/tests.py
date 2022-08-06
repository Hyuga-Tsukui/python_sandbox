
# Create your tests here.

import pytest

from .models import Question
from datetime import date

class TestSample:

    @pytest.fixture(autouse=True, scope='class')
    def setUp(self, django_db_setup, django_db_blocker):
        with django_db_blocker.unblock():
            for i in range(10000):
                Question.objects.create(question_text=f'test-{i}', pub_date=date(year=2022, month=5, day=2))

    @pytest.mark.django_db
    def test__sample(self):
        acutual = Question.objects.filter(question_text='test-0')
        assert acutual[0].question_text == 'test-0'
    
    @pytest.mark.django_db
    def test__sample1(self):
        acutual = Question.objects.filter(question_text='test-1')
        assert acutual[0].question_text == 'test-1'
    
    @pytest.mark.django_db
    def test__sample3(self):
        acutual = Question.objects.filter(question_text='test-2')
        assert acutual[0].question_text == 'test-2'
    
    @pytest.mark.django_db
    def test__sample4(self):
        acutual = Question.objects.filter(question_text='test-3')
        assert acutual[0].question_text == 'test-3'
    
    @pytest.mark.django_db
    def test__sample5(self):
        acutual = Question.objects.filter(question_text='test-4')
        assert acutual[0].question_text == 'test-4'

    @pytest.mark.django_db
    def test__sample6(self):
        acutual = Question.objects.filter(question_text='test-5')
        assert acutual[0].question_text == 'test-5'