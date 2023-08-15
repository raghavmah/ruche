# Generated by Django 4.2.4 on 2023-08-13 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagetitle', models.CharField(max_length=60, verbose_name='Enter the Page Sub Heading')),
                ('pagetext', models.CharField(max_length=1000, verbose_name='Enter Page  Description')),
            ],
            options={
                'verbose_name_plural': 'ABOUT-US PAGE TITLE AND DESCRIPTION',
            },
        ),
        migrations.CreateModel(
            name='carousels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(null=True, upload_to='D:\\ruche\\frontend/img', verbose_name='Enter The Image for carousel')),
                ('Img_title', models.CharField(max_length=30, null=True, verbose_name='Enter The image title')),
                ('Img_desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='Enter The image description')),
            ],
            options={
                'verbose_name_plural': 'CAROUSELS IMAGES',
            },
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagetitle', models.CharField(max_length=60, verbose_name='Enter the Page Sub Heading')),
                ('pagetext', models.CharField(max_length=1000, verbose_name='Enter Page  Description')),
            ],
            options={
                'verbose_name_plural': 'CONTACT PAGE TITLE AND DESCRIPTION',
            },
        ),
        migrations.CreateModel(
            name='headers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='D:\\ruche\\frontend/img', verbose_name='Enter The Logo')),
                ('email', models.EmailField(blank=True, max_length=256, null=True, verbose_name='Enter The Email id')),
                ('insta', models.URLField(blank=True, max_length=500, null=True, verbose_name='Enter The Instagram  Profile URl')),
                ('facebook', models.URLField(blank=True, max_length=500, null=True, verbose_name='Enter The FaceBook Profile URl')),
                ('twitter', models.URLField(blank=True, max_length=500, null=True, verbose_name='Enter The twitter  Profile URl')),
            ],
            options={
                'verbose_name_plural': 'LOGO IMAGE AND SOCIAL MEDIA LINKS',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagetitle', models.CharField(max_length=60, verbose_name='Enter the Page Sub Heading')),
                ('pagetext', models.CharField(max_length=1000, verbose_name='Enter Page  Description')),
            ],
            options={
                'verbose_name_plural': 'HOME PAGE TITLE AND DESCRIPTION',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Enter the Categories Name')),
            ],
            options={
                'verbose_name_plural': 'PRODUCTS NAME',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, null=True, verbose_name='Enter The image title')),
                ('desp', models.CharField(max_length=250, verbose_name='Enter Image Description')),
                ('image', models.ImageField(upload_to='D:\\ruche\\frontend/img')),
                ('des', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rugs.products')),
            ],
            options={
                'verbose_name_plural': 'PRODUCTS IMAGES',
            },
        ),
    ]
