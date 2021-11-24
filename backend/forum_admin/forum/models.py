from django.db import models
class ForumUser(models.Model):
    name = models.CharField(max_length=30)
    humor = models.IntegerField()
    tag = models.CharField(max_length=30)
    def __str__(self):
        return f'<ForumUser {self.name}>'
    # def __repr__(self):
    #     return f'<ForumUser {self.name}>'