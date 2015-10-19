import django.dispatch

task_created = django.dispatch.Signal(providing_args=['task'])
task_failed = django.dispatch.Signal(providing_args=['task'])
task_completed = django.dispatch.Signal(providing_args=['completed_task'])