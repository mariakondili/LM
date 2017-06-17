#!/usr/bin/env python


#$ cd Documents/[..]/LM
#$ source ~/.virtualenvs/leerstand_djangodemo/bin/activate
##> Last line of "activate" script: ++ export DJANGO_SETTINGS_MODULE=leerstandsmelder.settings

#$ python3
import os
import leerstandsmelder 
from leerstandsmelder import location
from leerstandsmelder import region
from django.db import models
from leerstandsmelder.location.models import Location 

## !!! ## 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/maritilia/Documents/LEERSTAND_FRA/django_db/LM/leerstandsmelder/location/models.py", line 5, in <module>
#     class Location(models.Model):
#   File "/home/maritilia/.virtualenvs/leerstand_djangodemo/lib/python3.5/site-packages/django/db/models/base.py", line 110, in __new__
#     app_config = apps.get_containing_app_config(module)
#   File "/home/maritilia/.virtualenvs/leerstand_djangodemo/lib/python3.5/site-packages/django/apps/registry.py", line 247, in get_containing_app_config
#     self.check_apps_ready()
#   File "/home/maritilia/.virtualenvs/leerstand_djangodemo/lib/python3.5/site-packages/django/apps/registry.py", line 125, in check_apps_ready
#     raise AppRegistryNotReady("Apps aren't loaded yet.")
# django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.