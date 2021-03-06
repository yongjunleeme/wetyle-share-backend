# Generated by Django 3.0.3 on 2020-03-06 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'followers',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_id', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=500)),
                ('kakao_id', models.CharField(max_length=100, null=True)),
                ('facebook_id', models.CharField(max_length=100, null=True)),
                ('twitter_id', models.CharField(max_length=100, null=True)),
                ('google_id', models.CharField(max_length=100, null=True)),
                ('nickname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(max_length=10)),
                ('image_url', models.URLField(blank=True, max_length=2000, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('homepage_url', models.URLField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('follow_relation', models.ManyToManyField(through='user.Follower', to='user.User')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plus_point', models.IntegerField(blank=True, null=True)),
                ('minus_point', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='user.User')),
            ],
            options={
                'db_table': 'points',
            },
        ),
        migrations.AddField(
            model_name='follower',
            name='followee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='followee', to='user.User'),
        ),
        migrations.AddField(
            model_name='follower',
            name='follower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='follower', to='user.User'),
        ),
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together={('follower', 'followee')},
        ),
    ]
