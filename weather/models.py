from django.db import models

class Weather():
    title = models.CharField(max_length=500)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey()


    def __str__(self):
        return self.title


