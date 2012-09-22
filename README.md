## massadmin

Mass updatting objects in Django's admin site.

## How to install

1. Put massadmin on your project path (the one with the ```__init__.py``` & ```urls.py```)
2. Add ```'massadmin'``` to ```INSTALLED_APPS``` in ```settings.py```
3. Change line 9 in ```urls.py```: ```... 'server.massadmin.massadmin.mass_change_view'``` to reference the appropriate location of massadmin
3. Add ```url(r'^admin/', include("massadmin.urls")),``` to ```urls.py```
