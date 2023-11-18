from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomadmin', '0002_merchantuser_is_added_by_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('title_details', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomadmin.products')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAbout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomadmin.products')),
            ],
        ),
    ]
