# Generated by Django 2.2 on 2021-09-15 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('fullName', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserData', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tobacco',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('current_status', models.CharField(blank=True, max_length=50, null=True)),
                ('previous_status', models.CharField(blank=True, max_length=50, null=True)),
                ('frequency', models.CharField(blank=True, max_length=50, null=True)),
                ('year_started', models.CharField(blank=True, max_length=50, null=True)),
                ('year_stopped', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='sexual',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('abusement', models.CharField(blank=True, max_length=50, null=True)),
                ('abusement_status', jsonfield.fields.JSONField(blank=True, null=True)),
                ('sexual_status', jsonfield.fields.JSONField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('current_status', models.CharField(blank=True, max_length=50, null=True)),
                ('previous_status', models.CharField(blank=True, max_length=50, null=True)),
                ('frequency', models.CharField(blank=True, max_length=50, null=True)),
                ('year_started', models.CharField(blank=True, max_length=50, null=True)),
                ('year_stopped', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='medication',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('drug_name', models.CharField(blank=True, max_length=100, null=True)),
                ('drug_dosage', models.CharField(blank=True, max_length=50, null=True)),
                ('begun_date', models.DateField(blank=True, null=True)),
                ('frequency', models.CharField(blank=True, max_length=50, null=True)),
                ('reason_taking', models.CharField(blank=True, max_length=50, null=True)),
                ('side_effect', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyHistory',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('relationship', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('cause_of_death', jsonfield.fields.JSONField(blank=True, null=True)),
                ('adopted', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('year_of_education', models.CharField(blank=True, max_length=50, null=True)),
                ('employee_status', models.CharField(blank=True, max_length=50, null=True)),
                ('occupation', jsonfield.fields.JSONField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('docName', models.CharField(blank=True, max_length=50, null=True)),
                ('docPhoneNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('docClinicName', models.TextField()),
                ('docSpecialization', jsonfield.fields.JSONField(blank=True, null=True)),
                ('docImage', models.ImageField(blank=True, max_length=254, null=True, upload_to='uploads/media/')),
                ('memberImage', models.URLField(default='https://i.picsum.photos/id/27/3264/1836.jpg?hmac=p3BVIgKKQpHhfGRRCbsi2MCAzw8mWBCayBsKxxtWO8g')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='caffine',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('current_status', models.CharField(blank=True, max_length=50, null=True)),
                ('previous_status', models.CharField(blank=True, max_length=50, null=True)),
                ('frequency', models.CharField(blank=True, max_length=50, null=True)),
                ('year_started', models.CharField(blank=True, max_length=50, null=True)),
                ('year_stopped', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='biotag',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('familyMemberName', models.CharField(blank=True, max_length=50, null=True)),
                ('familyMemberImage', models.ImageField(blank=True, max_length=254, null=True, upload_to='uploads/')),
                ('memberImage', models.URLField(default='https://i.picsum.photos/id/102/4320/3240.jpg?hmac=ico2KysoswVG8E8r550V_afIWN963F6ygTVrqHeHeRc')),
                ('familyMemberRelationship', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('height', models.CharField(blank=True, max_length=50, null=True)),
                ('weight', models.CharField(blank=True, max_length=50, null=True)),
                ('bmi', models.CharField(blank=True, max_length=50, null=True)),
                ('ethinicity', models.CharField(blank=True, max_length=50, null=True)),
                ('disability', jsonfield.fields.JSONField(blank=True, null=True)),
                ('preferred_language', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Alchol',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('current_status', models.CharField(blank=True, max_length=50, null=True)),
                ('previous_status', models.CharField(blank=True, max_length=50, null=True)),
                ('frequency', models.CharField(blank=True, max_length=50, null=True)),
                ('year_started', models.CharField(blank=True, max_length=50, null=True)),
                ('year_stopped', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
