from django.db import models

class Hackathons(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title + str(self.url)

