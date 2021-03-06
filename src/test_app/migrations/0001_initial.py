# Generated by Django 3.0.4 on 2020-04-16 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='case',
            fields=[
                ('CaseNo', models.AutoField(primary_key=True, serialize=False)),
                ('summary', models.TextField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(default=False)),
                ('cdescription', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=32)),
                ('caddress', models.CharField(max_length=32)),
                ('cga_income', models.DecimalField(decimal_places=2, max_digits=32)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=32)),
                ('eaddress', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
                ('eemail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('ProductNo', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=32)),
                ('pdescription', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='salesperson',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=32)),
                ('semail', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CaseNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.case')),
                ('ProductNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.product')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.salesperson')),
            ],
        ),
        migrations.CreateModel(
            name='resolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cm_resolution', models.TextField(blank=True, max_length=255, null=True)),
                ('rname', models.CharField(max_length=32)),
                ('step', models.TextField(blank=True, max_length=255, null=True)),
                ('ProductNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='relate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CaseNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.case')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.product')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CaseNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.case')),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.Employee')),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.resolution')),
            ],
        ),
        migrations.CreateModel(
            name='caseComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('CaseNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.case')),
                ('EID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CaseNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.case')),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.product')),
            ],
        ),
    ]
