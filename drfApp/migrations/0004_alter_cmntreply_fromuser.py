# Generated by Django 4.1.7 on 2023-04-01 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drfApp', '0003_rename_frr_cmntreply_fromuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmntreply',
            name='fromUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentReplyFrom', to=settings.AUTH_USER_MODEL),
        ),
    ]
