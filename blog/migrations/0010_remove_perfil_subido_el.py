# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170525_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='subido_el',
        ),
    ]
