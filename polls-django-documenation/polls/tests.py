import datetime

from django.utils import timezone
from django.urls import reverse
from django.test import TestCase

from .models import Question


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    question = Question.objects.create(
        question_text=question_text, pub_date=time)
    question.choice_set.create(choice_text='Choice1')
    return question


def create_question_with_choices(question_text, choice):
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    question = Question.objects.create(
        question_text=question_text, pub_date=time)
    question.choice_set.create(choice_text=choice, votes=0)
    return question


def create_question_without_choices(question_text):
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_future_question(self):
        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available")

    def test_future_and_past_question(self):
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(
            question_text="Future question", days=5)

        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(
            question_text="Past question.", days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


'''
=====================================================================================================
it’s silly that Questions can be published on the site that have no Choices. 
So, our views could check for this, and exclude such Questions. 
Our tests would create a Question without Choices and then test that it’s not published, 
as well as create a similar Question with Choices, and test that it is published.
We run these test on index , detail , results and vote views to check even if the user knows the exact
url to a specific question he will not find those with no choices
=====================================================================================================
'''


class ChoicesIndexViewTests(TestCase):
    '''
    Test if questions that have no choices are not displayed on the index page
    While those with choices are displayed
    '''

    def test_if_question_has_choices(self):
        question_with_choices = create_question_with_choices(
            question_text="Question with choices", choice='choice1')
        url = reverse('polls:index')
        response = self.client.get(url)
        self.assertContains(response, question_with_choices.question_text)

    def test_if_question_has_no_choices(self):
        no_choice_question = create_question_without_choices(
            question_text='no choice question')

        url = reverse('polls:index')
        response = self.client.get(url)
        self.assertNotContains(response, no_choice_question.question_text)


class ChoicesDetiledViewTests(TestCase):
    '''
    Test if questions that have no choices are not displayed on the detail page
    While those with choices are displayed even if user knows the url path to that page
    '''

    def test_if_question_has_choices(self):
        question_with_choices = create_question_with_choices(
            question_text="Question with choices", choice='choice1')
        url = reverse('polls:detail', args=(question_with_choices.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_if_question_has_no_choices(self):
        no_choice_question = create_question_without_choices(
            question_text='no choice question')
        url = reverse('polls:detail', args=(no_choice_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class ChoicesResultsViewTests(TestCase):
    '''
    Test if questions that have no choices are not displayed on the results page
    While those with choices are displayed even if user knows the url path to that page
    '''

    def test_if_question_has_choices(self):
        question_with_choices = create_question_with_choices(
            question_text="Question with choices", choice='choice1')
        url = reverse('polls:results', args=(question_with_choices.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_if_question_has_no_choices(self):
        no_choice_question = create_question_without_choices(
            question_text='no choice question')
        url = reverse('polls:results', args=(no_choice_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class ChoicesResultsViewTests(TestCase):
    '''
    Test if questions that have no choices are not displayed on the vote page
    While those with choices are displayed even if user knows the url path to that page
    '''

    def test_if_question_has_choices(self):
        question_with_choices = create_question_with_choices(
            question_text="Question with choices", choice='choice1')
        url = reverse('polls:vote', args=(question_with_choices.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_if_question_has_no_choices(self):
        no_choice_question = create_question_without_choices(
            question_text='no choice question')
        url = reverse('polls:vote', args=(no_choice_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
