# Generated by Django 4.0.6 on 2022-07-04 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Enter your blog', max_length=10000)),
                ('date_of_publication', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='blog_author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('summary', models.TextField(help_text='Enter your biography', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='blog_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Enter comment about blog here.', max_length=1000)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_blog.blog')),
                ('blog_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_blog.blog_author')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_blog.blog_author'),
        ),
    ]
