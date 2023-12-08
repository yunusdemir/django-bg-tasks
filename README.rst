=======================
Django Background Tasks
=======================

This package is a fork from [django-background-tasks](https://github.com/arteria/django-background-tasks), which does not seem to be maintained anymore. The package itself is a fork from django-background-task.

Django Background Task is a database-backed work queue for Django, loosely based around `Ruby's DelayedJob`_ library. This project was adopted and adapted from lilspikey_ `django-background-task`.

.. _Ruby's DelayedJob: https://github.com/tobi/delayed_job
.. _lilspikey: https://github.com/lilspikey/

In Django Background Task, all tasks are implemented as functions (or any other callable).

There are two parts to using background tasks:

- creating the task functions and registering them with the scheduler
- setup a cron task (or long running process) to execute the tasks


Docs
====
See `Read the docs`_.

The docs are still from the original project and need to be updated.

.. _Read the docs: http://django-background-tasks.readthedocs.io/en/latest/
