# Generated by Django 3.2.7 on 2021-10-24 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0038_auto_20211024_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('movie_id', models.IntegerField()),
                ('title', models.CharField(max_length=120)),
                ('genres', models.CharField(max_length=130)),
                ('imdb_id', models.IntegerField()),
                ('tmdb_id', models.IntegerField()),
                ('Image_url', models.URLField()),
                ('text', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='fav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
