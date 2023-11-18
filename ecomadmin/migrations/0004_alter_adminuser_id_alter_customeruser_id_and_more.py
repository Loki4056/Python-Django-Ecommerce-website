from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomadmin', '0003_productabout_productdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='merchantuser',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='staffuser',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
