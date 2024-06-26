# Generated by Django 4.2.11 on 2024-05-23 09:25

import bgfreshnet.accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_freshnetuser_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='users_profile_photos/', validators=[bgfreshnet.accounts.models.MaxFileSizeValidator(limit_value=10485760)]),
        ),
    ]
