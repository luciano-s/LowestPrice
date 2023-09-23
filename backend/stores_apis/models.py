from django.db import models


class StoreApi(models.Model):
    key = models.TextField()
    store = models.OneToOneField(
        "store.Store", related_name="api_access", on_delete=models.CASCADE
    )
    url = models.TextField()
