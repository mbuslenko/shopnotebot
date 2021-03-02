from django.db import models


class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name="User's id"
    )
    name = models.TextField(
        verbose_name="User's name"
    )

    def __str__(self):
        return f'#{self.external_id} {self.name}'

    class Meta:
        verbose_name = 'Profile'


class Month(models.Model):
    name = models.TextField(verbose_name="Name")

    def __str__(self):
        return f"Month {self.name}"

    class Meta:
        verbose_name = "Month"


class Item(models.Model):
    profile = models.ForeignKey(to="shoplist.profile", verbose_name="Item's author", on_delete=models.PROTECT)
    name = models.TextField(verbose_name="Name")
    link = models.TextField(verbose_name="Link", default="Null")
    price = models.IntegerField(verbose_name="Price")
    month = models.ForeignKey(to="shoplist.month", verbose_name="Month", on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name="Creation date", auto_now_add=True)


class Category(models.Model):
    profile = models.ForeignKey(to="shoplist.profile", verbose_name="Category author", on_delete=models.PROTECT)
    name = models.TextField(verbose_name="Category's name")
    created_at = models.DateTimeField(verbose_name="Creation date", auto_now_add=True)

    def __str__(self):
        return f"Category {self.name}, from {self.profile}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
