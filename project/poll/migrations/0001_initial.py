# Generated by Django 3.1.4 on 2020-12-03 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500)),
                ('question_type', models.CharField(choices=[('text_answer', 'Text answer'), ('one_choice', 'One choice'), ('multiple_choice', 'Multiple choice')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_option_name', models.CharField(max_length=500)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.question')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('manager', 'Manager'), ('registred_user', 'Registred user'), ('anonymous_user', 'Anonymous user')], max_length=50)),
                ('user_uid', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.CharField(blank=True, max_length=500, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.question')),
                ('question_option', models.ManyToManyField(to='poll.QuestionOption')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.userprofile'),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_name', models.CharField(max_length=50)),
                ('poll_date_start', models.DateTimeField(auto_now_add=True)),
                ('poll_date_end', models.DateTimeField(blank=True, null=True)),
                ('poll_description', models.CharField(blank=True, max_length=500, null=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.userprofile')),
            ],
        ),
    ]
