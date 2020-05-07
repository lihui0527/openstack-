from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date blogs')
    class Meta:
        ordering = ('-pub_date',)
    def __unicode__(self):
            return self.title
