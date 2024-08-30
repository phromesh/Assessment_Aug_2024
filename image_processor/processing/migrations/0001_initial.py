# Generated by Django 5.1 on 2024-08-29 19:25

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProcessing',
            fields=[
                ('request_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('original_url', models.URLField()),
                ('processed_image_path', models.ImageField(upload_to='processed_images/')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processing.imageprocessing')),
            ],
        ),
    ]
