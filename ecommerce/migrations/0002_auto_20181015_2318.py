# Generated by Django 2.1.1 on 2018-10-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageelement',
            name='image',
            field=models.ImageField(blank=True, default='media/media/placeholder-image.jpg', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='construction_status',
            field=models.CharField(choices=[('Ready To Move', 'Ready To Move'), ('Under Construction', 'Under Construction')], max_length=100),
        ),
        migrations.AlterField(
            model_name='properties',
            name='post_date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
