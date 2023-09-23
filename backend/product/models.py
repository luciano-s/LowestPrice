from django.db import models


class Product(models.Model):
    class RequirementLevel(models.TextChoices):
        INDISPENSABLE = "indispensable"
        IMPORTANT = "important"
        NICE_TO_HAVE = "nice to have"

    name = models.TextField()
    categories = models.ManyToManyField("category.Category", related_name="products")
    priority = models.CharField(
        choices=RequirementLevel.choices, default=RequirementLevel.NICE_TO_HAVE
    )
    key = models.SlugField(verbose_name="Key to compare with similar products")
