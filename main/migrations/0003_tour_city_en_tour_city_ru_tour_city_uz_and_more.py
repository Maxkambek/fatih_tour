# Generated by Django 4.2 on 2023-05-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tour_image_big'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='city_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='city_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='city_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='duration_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='duration_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='duration_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='location_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='location_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='location_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tourdate',
            name='date_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tourdate',
            name='date_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tourdate',
            name='date_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tourdetail',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tourdetail',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tourdetail',
            name='content_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tourdetail',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tourdetail',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tourdetail',
            name='description_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tourdetail',
            name='title_en',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='tourdetail',
            name='title_ru',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='tourdetail',
            name='title_uz',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='tourdropdown',
            name='name_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='tourdropdown',
            name='name_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='tourdropdown',
            name='name_uz',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='tourdropdown',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tourdropdown',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tourdropdown',
            name='text_uz',
            field=models.TextField(null=True),
        ),
    ]
