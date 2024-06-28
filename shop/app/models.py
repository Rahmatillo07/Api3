from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Review(models.Model):
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment


from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    price = models.PositiveIntegerField()
    created = models.DateField()
    term = models.DateField(verbose_name='muddati')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    comment = models.ManyToManyField(Review, null=True, blank=True)

    def __str__(self):
        return self.title
