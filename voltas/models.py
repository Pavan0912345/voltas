# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    sk = models.CharField(unique=True, max_length=128, blank=True, null=True)
    source_name = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    product_url = models.TextField(blank=True, null=True)
    mrp = models.TextField(blank=True, null=True)
    deal_price = models.TextField(blank=True, null=True)
    discount_percentage = models.CharField(max_length=255, blank=True, null=True)
    seller_name = models.CharField(max_length=255, blank=True, null=True)
    seller_name_and_id = models.TextField(blank=True, null=True)
    seller_address = models.TextField(blank=True, null=True)
    bank_offers = models.TextField(blank=True, null=True)
    offers = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    model_name = models.TextField(blank=True, null=True)
    capacity = models.CharField(max_length=255, blank=True, null=True)
    colour = models.CharField(max_length=255, blank=True, null=True)
    technical_details = models.TextField(blank=True, null=True)
    seller_details = models.TextField(blank=True, null=True)
    seller_actual_name = models.TextField(blank=True, null=True)
    seller_id = models.CharField(max_length=255, blank=True, null=True)
    channel_sku = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    model_number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    mop_modified = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Product'


class VoltasProductDetails(models.Model):
    sk = models.CharField(unique=True, max_length=128, blank=True, null=True)
    source_name = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    product_url = models.TextField(blank=True, null=True)
    mrp = models.TextField(blank=True, null=True)
    deal_price = models.TextField(blank=True, null=True)
    discount_percentage = models.CharField(max_length=255, blank=True, null=True)
    seller_name = models.CharField(max_length=255, blank=True, null=True)
    seller_name_and_id = models.TextField(blank=True, null=True)
    seller_address = models.TextField(blank=True, null=True)
    bank_offers = models.TextField(blank=True, null=True)
    offers = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    model_name = models.TextField(blank=True, null=True)
    capacity = models.CharField(max_length=255, blank=True, null=True)
    colour = models.CharField(max_length=255, blank=True, null=True)
    technical_details = models.TextField(blank=True, null=True)
    seller_details = models.TextField(blank=True, null=True)
    seller_actual_name = models.TextField(blank=True, null=True)
    seller_id = models.CharField(max_length=255, blank=True, null=True)
    channel_sku = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    model_number = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    mop_modified = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Voltas_product_details'


class AllProductDetails(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    rating = models.CharField(max_length=10, blank=True, null=True)
    soldby = models.CharField(db_column='soldBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    capacity = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    asin = models.CharField(db_column='ASIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    genericname = models.CharField(db_column='genericName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_product_details'


class AmazonIfb(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    details_url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amazon_ifb'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Products(models.Model):
    title = models.CharField(max_length=1000)
    price = models.CharField(max_length=50)
    rating = models.CharField(max_length=300, blank=True, null=True)
    sold_by = models.CharField(max_length=555, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    capacity = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    technical_details = models.JSONField(blank=True, null=True)
    asin = models.CharField(max_length=50, blank=True, null=True)
    generic_name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Voltas(models.Model):
    title = models.CharField(max_length=1000)
    price = models.CharField(max_length=50)
    rating = models.CharField(max_length=50, blank=True, null=True)
    sold_by = models.CharField(max_length=555, blank=True, null=True)
    brand = models.CharField(max_length=300, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    capacity = models.CharField(max_length=500, blank=True, null=True)
    model = models.CharField(max_length=500, blank=True, null=True)
    technical_details = models.TextField(blank=True, null=True)
    asin = models.CharField(max_length=500, blank=True, null=True)
    generic_name = models.CharField(max_length=555, blank=True, null=True)
    url = models.CharField(max_length=1000)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voltas'


class VoltasMappingTable(models.Model):
    sk = models.CharField(unique=True, max_length=128, db_collation='utf8mb4_bin')
    inv_vfx = models.TextField(blank=True, null=True)
    tonnage = models.TextField(blank=True, null=True)
    star_rating = models.TextField(blank=True, null=True)
    series = models.TextField(blank=True, null=True)
    fascia = models.TextField(blank=True, null=True)
    material_code = models.TextField(blank=True, null=True)
    model_name = models.TextField(blank=True, null=True)
    mop = models.TextField(blank=True, null=True)
    amazon_url = models.TextField(blank=True, null=True)
    amazon_sku = models.TextField(blank=True, null=True)
    flipkart_url = models.TextField(blank=True, null=True)
    flipkart_sku = models.TextField(blank=True, null=True)
    vijay_url = models.TextField(blank=True, null=True)
    vijay_sku = models.TextField(blank=True, null=True)
    croma_url = models.TextField(blank=True, null=True)
    croma_sku = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'voltas_mapping_table'
