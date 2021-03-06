# Generated by Django 2.2 on 2020-03-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonialsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonials_author', models.CharField(max_length=150, verbose_name='Nome do autor:')),
                ('author_picture', models.ImageField(blank=True, null=True, upload_to='img/author/', verbose_name='Sua foto')),
                ('author_job', models.CharField(max_length=150, verbose_name='Cargo função na empresa:')),
                ('testimonials_description', models.CharField(blank=True, max_length=800, null=True, verbose_name='Seu depoimento')),
            ],
            options={
                'verbose_name': 'testimonial',
                'verbose_name_plural': 'testimonials',
            },
        ),
    ]
