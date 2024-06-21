from django.db import models


# Create your models here.
class Comments(models.Model):
    comment_text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    def __str__(self):
        return self.comment_text

