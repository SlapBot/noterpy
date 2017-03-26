**********
noterpy
**********

|version| |license|

Python client around ``The simplest way to keep notes.`` (a.k.a. ``Simple Note``): https://simplenote.com/

It's built on top of ``simplenote.py``: https://github.com/mrtazz/simplenote.py

**NOTE:** This library and its author are not endorsed by or affiliated with `SimpleNote.com <https://simplenote.com/>`_.


Installation
============

Using ``pip``:


::

    pip install newsapi


Dependencies
============

- simplenote

API
===

Let's you do stuffs like ``noter.add_note("Hi")`` which returns ``NoteInfo`` instance and has
all the attributes such as ``version``, ``modified_date``, etc, and some methods like
``update("updated")``, ``trash()``, ``delete()`` and a ``get()`` which returns ``Note`` instance
and has ``content`` and all the above attributes in NoteInfo, so basically it controls ``key`` attribute
present in each note request so you can work on writing and reading notes instead of managing
stupid hashed key, and has bunch of other methods for which I'll write documentation later.
Just being a lazy-ass, because of working in a new project (duh).


.. |version| image:: http://img.shields.io/pypi/v/omdb.svg?style=flat-square
    :target: https://pypi.python.org/pypi/newsapi

.. |license| image:: http://img.shields.io/pypi/l/omdb.svg?style=flat-square
    :target: https://pypi.python.org/pypi/newsapi
