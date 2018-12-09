from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=100)
    last_update = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')



class Post(models.Model):
    message = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    create_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    update_by = models.ForeignKey(User, null=True, related_name='+',
                                  on_delete=models.CASCADE)
