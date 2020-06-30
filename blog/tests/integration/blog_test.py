from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_post(self):
        b = Blog('Blog', 'Me')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(b.posts[0].title, 'Test Post')

    def test_json_no_post(self):
        b = Blog('Blog', 'Me')

        expected = {
            'title': b.title,
            'author': b.author,
            'posts': [],
        }

        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('Blog', 'Me')
        b.create_post('Test Post', 'Test Content')

        expected = {
            'title': b.title,
            'author': b.author,
            'posts': [
                {
                    'title': 'Test Post',
                    'content': 'Test Content'
                }
            ]
        }

        self.assertDictEqual(expected, b.json())
