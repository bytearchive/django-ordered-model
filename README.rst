====================
django-ordered-model
====================

Allows models to be ordered and provides a simple admin interface for
reordering them.

Based on http://www.djangosnippets.org/snippets/998/ and
http://www.djangosnippets.org/snippets/259/

Requires:

* Django 1.4

Installation
============

::

    $ python setup.py install

Usage
=====

Add ``ordered_model`` to your ``SETTINGS.INSTALLED_APPS``.

To add ordering to your model, inherit from the ``OrderedModel`` class::

    from django.db import models
    from ordered_model.models import OrderedModel

    class Item(OrderedModel):
        name = models.CharField(max_length=100)

Model instances now have ``move_up()`` and ``move_down()`` methods to move them
relative to each other.

To add re-ordering controls to a model's admin interface, inherit from the
``OrderedModelAdmin`` class.  Your model admin will now have a method called
``move_up_down_links``, which outputs html for two buttons which control model
ordering.  Use the admin class's ``list_display`` property to add these buttons
into the admin interface::

    from django.contrib import admin
    from ordered_model.admin import OrderedModelAdmin
    from .models import Item


    class ItemAdmin(OrderedModelAdmin):
        list_display = ('name', 'move_up_down_links')

    admin.site.register(Item, ItemAdmin)

Test suite
==========

::

    $ ./run_tests.sh
