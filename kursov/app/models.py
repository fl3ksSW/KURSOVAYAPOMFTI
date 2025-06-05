from django.db import models

# Create your models here.
class ExampleModel(models.Model):
    """
    Example model for demonstration purposes.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Example Model"
        verbose_name_plural = "Example Models"

class AnotherModel(models.Model):
    """
    Another example model for demonstration purposes.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Another Model"
        verbose_name_plural = "Another Models"

class CustomUser(models.Model):
    """
    Custom user model for authentication.
    """
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

class Product(models.Model):
    """
    Product model for e-commerce applications.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class Order(models.Model):
    """
    Order model for e-commerce applications.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.product.name}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

class Category(models.Model):
    """
    Category model for organizing products.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Comment(models.Model):
    """
    Comment model for user feedback.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.product.name}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

class Review(models.Model):
    """
    Review model for product ratings.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} - {self.product.name}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
