# Generated by Django 2.2.6 on 2019-10-26 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccommodationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image_path', models.CharField(max_length=500)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'accommodationtype',
                'verbose_name_plural': 'accommodationtypes',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=500)),
                ('description', models.TextField(blank=True)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=30)),
                ('duration', models.IntegerField()),
                ('servicecharges', models.DecimalField(decimal_places=2, max_digits=30)),
                ('service_charge_description', models.TextField(blank=True)),
                ('rent', models.BooleanField(default=False)),
                ('sale', models.BooleanField(default=False)),
                ('geoLocation', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=255)),
                ('bills_included', models.BooleanField(default=False)),
                ('females', models.BooleanField(default=False)),
                ('males', models.BooleanField(default=False)),
                ('couples', models.BooleanField(default=False)),
                ('furnished', models.BooleanField(default=False)),
                ('smoking_allowed', models.BooleanField(default=False)),
                ('pets_allowed', models.BooleanField(default=False)),
                ('min_stay', models.IntegerField()),
                ('max_stay', models.IntegerField()),
                ('move_in_anytime', models.BooleanField(default=False)),
                ('bathrooms', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('garages', models.IntegerField()),
                ('agency', models.DecimalField(decimal_places=2, max_digits=30)),
                ('legal', models.DecimalField(decimal_places=2, max_digits=30)),
                ('caution', models.DecimalField(decimal_places=2, max_digits=30)),
                ('movein_date', models.CharField(max_length=20)),
                ('occupation_option', models.IntegerField(choices=[(1, 'Dont mind'), (2, 'Professional'), (3, 'Student'), (4, 'Clergy'), (5, 'Retired')], default=1)),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('landlord_option', models.IntegerField(choices=[(1, 'Dont mind'), (2, 'Yes'), (3, 'No')], default=1)),
                ('day_option', models.IntegerField(choices=[(1, 'Week days'), (2, 'Weekends'), (3, 'Both')], default=3)),
                ('advert_status', models.IntegerField(choices=[(1, 'On Advert'), (2, 'Advert Ended'), (3, 'Archived')], default=1)),
                ('photo1', models.CharField(max_length=500)),
                ('photo2', models.CharField(max_length=500)),
                ('photo3', models.CharField(max_length=500)),
                ('photo4', models.CharField(max_length=500)),
                ('photo5', models.CharField(max_length=500)),
                ('photo6', models.CharField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user_id', models.CharField(max_length=500)),
                ('active', models.BooleanField(default=True)),
                ('accommodationtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adverts', to='shareflatapp.AccommodationType')),
            ],
            options={
                'verbose_name': 'advert',
                'verbose_name_plural': 'adverts',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='AdvertCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=20)),
                ('duration', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'advertcategory',
                'verbose_name_plural': 'advertcategories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('code', models.CharField(max_length=3, unique=True)),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image_path', models.FilePathField(path='/base/roomtypes')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'roomtype',
                'verbose_name_plural': 'roomtypes',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='shareflatapp.Country')),
            ],
            options={
                'verbose_name': 'state',
                'verbose_name_plural': 'states',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('zipcode', models.CharField(max_length=10, unique=True)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='towns', to='shareflatapp.State')),
            ],
            options={
                'verbose_name': 'town',
                'verbose_name_plural': 'towns',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('zipcode', models.CharField(max_length=10, unique=True)),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='shareflatapp.Town')),
            ],
            options={
                'verbose_name': 'area',
                'verbose_name_plural': 'areas',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='AdvertReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user_id', models.CharField(db_index=True, max_length=255)),
                ('comments', models.TextField()),
                ('rating', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertreviews', to='shareflatapp.Advert')),
            ],
            options={
                'verbose_name': 'advertreview',
                'verbose_name_plural': 'advertreviews',
                'ordering': ('-date_created',),
            },
        ),
        migrations.AddField(
            model_name='advert',
            name='advertcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adverts', to='shareflatapp.AdvertCategory'),
        ),
        migrations.AddField(
            model_name='advert',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adverts', to='shareflatapp.Area'),
        ),
        migrations.AddField(
            model_name='advert',
            name='roomtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adverts', to='shareflatapp.RoomType'),
        ),
    ]
