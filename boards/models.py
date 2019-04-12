from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Board(models.Model):
	name = models.CharField(max_length=40,unique=True)
	description = models.TextField(max_length=200)

	def __str__(self):
		return self.name

	def get_posts_count(self):
		return Post.objects.filter(topic__board=self).count()

	def get_last_post(self):
		return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
	subject = models.CharField(max_length=300)
	last_updated = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey(Board, related_name='topics')
	starter = models.ForeignKey(User,related_name='topics')
	views = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.subject


class Post(models.Model):
	message = models.TextField(max_length=5000)
	topic = models.ForeignKey(Topic,related_name='posts')
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User,related_name='posts')
	updated_by = models.ForeignKey(User,null=True,related_name='+')

	def __str__(self):
		truncated_message = Truncator(self.message)
		return truncated_message.chars(30)


	

	