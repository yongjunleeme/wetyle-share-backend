# Generated by Django 3.0.3 on 2020-03-03 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('small_image_url', models.URLField(max_length=2000)),
                ('large_image_url', models.URLField(max_length=2000)),
            ],
            options={
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'colors',
            },
        ),
        migrations.CreateModel(
            name='FirstCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'first_categories',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shipping_address', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_url', models.URLField(max_length=2000)),
                ('price', models.IntegerField(default=0)),
                ('discounted_price', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('detailed_info', models.TextField()),
                ('add_info', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Brand')),
                ('first_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.FirstCategory')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='SecondCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('first_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.FirstCategory')),
            ],
            options={
                'db_table': 'second_categories',
            },
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'shippings',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='ThirdCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fist_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.FirstCategory')),
                ('second_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.SecondCategory')),
            ],
            options={
                'db_table': 'third_categories',
            },
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Size')),
            ],
            options={
                'db_table': 'product_stocks',
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Size')),
            ],
            options={
                'db_table': 'product_sizes',
            },
        ),
        migrations.CreateModel(
            name='ProductLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'product_likes',
            },
        ),
        migrations.CreateModel(
            name='ProductInqury',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decription', models.CharField(max_length=500)),
                ('is_answer', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=500)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'product_inqueries',
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Color')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
            ],
            options={
                'db_table': 'product_colors',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='procuct_size',
            field=models.ManyToManyField(through='product.ProductSize', to='product.Size'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_color',
            field=models.ManyToManyField(through='product.ProductColor', to='product.Color'),
        ),
        migrations.AddField(
            model_name='product',
            name='second_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.SecondCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='third_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.ThirdCategory'),
        ),
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Color')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Size')),
            ],
            options={
                'db_table': 'ordered_products',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Shipping'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User'),
        ),
    ]
