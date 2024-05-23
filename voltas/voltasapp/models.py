from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')
# Create your models here.

class Voltas_product_details(models.Model):
    sk = models.CharField(max_length=128, unique=True, null=True)
    source_name = models.CharField(max_length=255, null=True)
    source_id = models.IntegerField(null=True)
    category = models.CharField(max_length=255, null=True)
    product_name = models.TextField(null=True)
    product_url = models.TextField(null=True)
    mrp = models.TextField(null=True)
    deal_price = models.TextField(null=True)
    discount_percentage = models.CharField(max_length=255, null=True)
    seller_name = models.CharField(max_length=255, null=True)
    seller_name_and_id = models.TextField(null=True)
    seller_address = models.TextField(null=True)
    bank_offers = models.TextField(null=True)
    offers = models.TextField(null=True)
    brand = models.CharField(max_length=255, null=True)
    model_name = models.TextField(null=True)
    capacity = models.CharField(max_length=255, null=True)
    colour = models.CharField(max_length=255, null=True)
    technical_details = models.TextField(null=True)
    seller_details = models.TextField(null=True)
    seller_actual_name = models.TextField(null=True)
    seller_id = models.CharField(max_length=255, null=True)
    channel_sku = models.CharField(max_length=255, null=True)
    channel = models.CharField(max_length=255, null=True)
    model_number = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    zipcode = models.CharField(max_length=255, null=True)
    mop_modified = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    class Meta:
         db_table="Voltas_product_details"

# class washingmachine(models.Model):
#     title = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
#     rating = models.DecimalField(max_digits=3, decimal_places=1, null=True)
#     soldBy = models.CharField(max_length=255, null=True)
#     brand = models.CharField(max_length=255, null=True)
#     model = models.CharField(max_length=255, null=True)
#     capacity = models.CharField(max_length=50, null=True)
#     color = models.CharField(max_length=50, null=True)
#     asin = models.CharField(max_length=20, null=True)
#     genericname = models.CharField(max_length=50, null=True)
#     url = models.CharField(max_length=255, null=True)
#     energyEfficiency = models.CharField(max_length=50, null=True)
#     maximumRotationalSpeed = models.CharField(max_length=50, null=True)
#     noiseLevel = models.CharField(max_length=50, null=True)
#     installationType = models.CharField(max_length=50, null=True)
#     partNumber = models.CharField(max_length=50, null=True)
#     specialFeatures = models.TextField(null=True)
#     controlConsole = models.CharField(max_length=50, null=True)
#     numberOfStandardCycles = models.IntegerField(null=True)
#     accessLocation = models.CharField(max_length=50, null=True)
#     voltage = models.CharField(max_length=50, null=True)
#     certification = models.CharField(max_length=50, null=True)
#     material = models.CharField(max_length=50, null=True)
#     includedComponents = models.TextField(null=True)
#     batteriesRequired = models.CharField(max_length=5, null=True)
#     manufacturer = models.CharField(max_length=255, null=True)
#     countryOfOrigin = models.CharField(max_length=50, null=True)

#     class Meta:
#         db_table="washingmachine"
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin