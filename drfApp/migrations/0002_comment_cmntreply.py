# Generated by Django 4.1.7 on 2023-04-01 10:35

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drfApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='fromU', unique=True)),
                ('cmnt', models.TextField()),
                ('cmntDate', models.DateTimeField(auto_now_add=True)),
                ('fromU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromCmnt', to=settings.AUTH_USER_MODEL)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drfApp.notes')),
                ('toU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CmntReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmntR', models.TextField()),
                ('frR', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='cmntR', unique=True)),
                ('cmtRply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
