from django.db import models


class ProductRecord(models.Model):
    product = models.ForeignKey(
        "product.Product", related_name="records", on_delete=models.CASCADE
    )
    store = models.ForeignKey(
        "store.Store",
        related_name="records_of_products",
        on_delete=models.PROTECT,
    )
    date = models.DateTimeField(verbose_name="Product price check date")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    link = models.TextField()

    class Meta:
        unique_together = ("product", "date", "store")
