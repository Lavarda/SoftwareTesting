from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Blog', 'Me')

        self.assertEqual('Blog', b.title)
        self.assertEqual('Me', b.author)
        self.assertLessEqual([], b.posts)

    def test_repr(self):
        b = Blog('Blog', 'Me')

        self.assertEqual(b.__repr__(), 'Blog by Me (0 posts)')

