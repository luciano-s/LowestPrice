from django.db import models


class Store(models.Model):
    name = models.TextField(unique=True)
    url_for_querying = models.TextField()
