from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Glass

class GlassModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_Glass = Glass.objects.create(
            Admine = test_user,
            Name = 'Title of Blog',
            Discription = 'Words about the blog'
        )
        test_Glass.save()

    def test_blog_content(self):
        glass = Glass.objects.get(id=1)

        self.assertEqual(str(glass.Admine), 'tester')
        self.assertEqual(glass.Name, 'Title of Blog')
        self.assertEqual(glass.Discription, 'Words about the blog')

class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_Glass = Glass.objects.create(
            Admine = test_user,
            Name = 'Title of Blog',
            Discription = 'Words about the blog'
        )
        test_Glass.save()

        response = self.client.get(reverse('blog_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id':1,
            'Name': test_Glass.Name,
            'Discription': test_Glass.Discription,
            'Admine': test_user.id,
        })


    def test_create(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        url = reverse('blog_list')
        data = {
            "title":"Testing is Fun!!!",
            "Discription":"when the right tools are available",
            "Admine":test_user.id,
        }

        response = self.client.Glass(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

        self.assertEqual(Glass.objects.count(), 1)
        self.assertEqual(Glass.objects.get().Name, data['Name'])

    def test_update(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_Glass = Glass.objects.create(
            Admine = test_user,
            Name = 'Name of Blog',
            Discription = 'Words about the blog'
        )

        test_Glass.save()

        url = reverse('blog_detail',args=[test_Glass.id])
        data = {
            "Name":"Testing is Still Fun!!!",
            "Admine":test_Glass.Admine.id,
            "Discription":test_Glass.Discription,
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK, url)

        self.assertEqual(Glass.objects.count(), test_Glass.id)
        self.assertEqual(Glass.objects.get().Name, data['Name'])


    def test_delete(self):
        """Test the api can delete a Glass."""

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_Glass = Glass.objects.create(

            Admine = test_user,
            Name = 'Title of Blog',
            Discription = 'Words about the blog'

        )

        test_Glass.save()

        Glass = Glass.objects.get()

        url = reverse('Glasss_detail', kwargs={'pk': Glass.id})


        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)