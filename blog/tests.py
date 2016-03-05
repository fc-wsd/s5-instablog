from django.test import TestCase
from django.test import Client
from django.db import transaction
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from .models import Post
from .models import Category


User = get_user_model()


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User()
        self.user.set_password('12345678')
        self.user.save()
        self.category = Category(name='Category')
        self.category.save()

    def test_create_post_by_model(self):
        new_post = Post()
        new_post.title = 'hello world'
        new_post.content = 'lorem ipsum'

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                new_post.save()
        self.assertIsNone(new_post.pk)

    def test_create_post_by_model_successful(self):
        new_post = Post()
        new_post.category = self.category
        new_post.user = self.user
        new_post.save()

        self.assertTrue(isinstance(new_post.pk, int))

    def test_get_create_post_view_without_login(self):
        c = Client()

        url = '/posts/100000/'
        res = c.get(url)
        self.assertEqual(res.status_code, 404)

        new_post = Post()
        new_post.title = 'aaa'
        new_post.content = 'bbbb'
        new_post.category = self.category
        new_post.user = self.user
        new_post.save()

        url = reverse('view_post', kwargs={'pk': new_post.pk})

        res = c.get(url)
        self.assertEqual(res.status_code, 200)

        url = reverse('create_post')
        data = {'title': 'world', 'content': 'hello'}
        res = c.post(url, data, follow=False)
        self.assertIn(res.status_code, (301, 302, )) 

