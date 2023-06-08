from django.db import models

PROGRAMS = (
    ('Loyalty #1', 'Loyalty #1'),
    ('Loyalty #2', "Loyalty #2"),
    ('Loyalty #3', 'Loyalty #3')
)


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name


class LoyaltyProgram(models.Model):
    name = models.CharField(choices=PROGRAMS, max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    purchase_date = models.DateTimeField(auto_now_add=True)


class LoyaltyPoint(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loyalty_program = models.ForeignKey(LoyaltyProgram, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)


