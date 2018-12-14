# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    bookname = models.CharField(db_column='Bookname', unique=True, max_length=255)  # Field name made lowercase.
    original_bookname = models.CharField(db_column='Original_Bookname', max_length=255)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
    how_much_charter = models.IntegerField(db_column='How_much_charter')  # Field name made lowercase.
    how_much_translated = models.IntegerField(db_column='How_much_translated', blank=True, null=True)  # Field name made lowercase.
    translate_done = models.IntegerField(db_column='Translate_done')  # Field name made lowercase.
    who_translate = models.ForeignKey('Transletors', models.DO_NOTHING, db_column='Who_translate')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Books'


class Journal(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.ForeignKey('Transletors', models.DO_NOTHING, db_column='Username')  # Field name made lowercase.
    bookname = models.ForeignKey(Books, models.DO_NOTHING, db_column='BookName')  # Field name made lowercase.
    page = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Journal'


class Reader(models.Model):
    username = models.CharField(db_column='Username', unique=True, max_length=255)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(db_column='First_name', max_length=255)  # Field name made lowercase.
    second_name = models.CharField(db_column='Second_Name', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reader'


class Transletors(models.Model):
    username = models.CharField(db_column='Username', unique=True, max_length=255)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(db_column='First_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    second_name = models.CharField(db_column='Second_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    english_level = models.CharField(db_column='English_level', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transletors'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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
