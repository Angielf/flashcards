# Generated by Django 2.0.4 on 2018-06-01 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front', models.TextField()),
                ('back', models.TextField()),
                ('parentDeck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Deck')),
            ],
        ),
    ]
