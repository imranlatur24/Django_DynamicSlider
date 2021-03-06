# Generated by Django 3.2.9 on 2022-02-04 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0002_alter_slidermodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='slidermodel',
            name='action_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slidermodel',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='slidermodel',
            name='image',
            field=models.ImageField(upload_to='pics/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='slidermodel',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
