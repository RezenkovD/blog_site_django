# Generated by Django 4.0.6 on 2022-07-07 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_alter_blog_options_alter_blog_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_of_publication',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]