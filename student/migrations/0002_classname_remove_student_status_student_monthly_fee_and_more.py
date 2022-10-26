# Generated by Django 4.0.4 on 2022-06-11 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='status',
        ),
        migrations.AddField(
            model_name='student',
            name='monthly_fee',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('class_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student.classname')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='batch_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student.batch'),
        ),
        migrations.AddField(
            model_name='student',
            name='class_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student.classname'),
        ),
    ]