# Generated by Django 4.1.6 on 2023-04-05 12:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Other', 'Other')], max_length=100)),
                ('mobile', models.CharField(default=None, max_length=12)),
                ('state', models.CharField(choices=[('Rj', 'Rajasthan'), ('Up', 'UtterPradesh'), ('Mp', 'MadhyaPradesh'), ('Mh', 'Maharashtra'), ('Guj', 'Gujarat'), ('Tn', 'Tamilnadu')], max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('salary', models.FloatField()),
                ('description', models.TextField(max_length=400)),
                ('experience', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(default=datetime.date.today)),
                ('is_approved', models.BooleanField(default=False)),
                ('company', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='JobInfo.company')),
            ],
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('experience', models.CharField(choices=[('Fresher', 'Fresher'), ('1y', '1 year'), ('2y', '2 year'), ('3y', '3 year'), ('4y', '4 year'), ('5y', '5 year'), ('above 5y', 'above 5 year')], max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='ApplicantPhotos')),
                ('resume', models.FileField(blank=True, upload_to='ApplicantResume')),
                ('apply_date', models.DateField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobInfo.applicant')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobInfo.job')),
            ],
        ),
    ]
