from django.db import models

class Stars(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey("Category", on_delete=models.CASCADE)


    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=600, db_index=True)

    def __str__(self):
        return self.name

