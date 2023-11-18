from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchantuser',
            name='is_added_by_admin',
            field=models.BooleanField(default=False),
        ),
    ]
