from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post

# Test creating new post
class PostUnitTest(TestCase):
    def test_post(self):
        title = 'title'
        content = 'content'
        post = Post.objects.create(
            title=title,
            content=content
        )
        self.assertEqual(post.title, title)
        self.assertEqual(post.content, content)


# Test creating new user 
class UserUintTest(TestCase):
    def test_create_user(self):
        username = 'abdelrahman'
        password = 'admin'
        email = 'abdelrahman@gmail.com'
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
