# -*- coding: utf-8 -*-
import multiprocessing

from django.conf import settings

try:
    cpu_count = multiprocessing.cpu_count()
except Exception:
    cpu_count = 1


class AppSettings(object):
    """
    """
    @property
    def MAX_ATTEMPTS(self):
        """Control how many times a task will be attempted."""
        return getattr(settings, 'MAX_ATTEMPTS', 25)

    @property
    def BACKGROUND_TASK_MAX_ATTEMPTS(self):
        """Control how many times a task will be attempted."""
        return self.MAX_ATTEMPTS

    @property
    def MAX_RUN_TIME(self):
        """Maximum possible task run time, after which tasks will be unlocked and tried again."""
        return getattr(settings, 'MAX_RUN_TIME', 3600)

    @property
    def BACKGROUND_TASK_MAX_RUN_TIME(self):
        """Maximum possible task run time, after which tasks will be unlocked and tried again."""
        return self.MAX_RUN_TIME

    @property
    def BACKGROUND_TASK_RUN_ASYNC(self):
        """Control if tasks will run asynchronous in a ThreadPool."""
        return getattr(settings, 'BACKGROUND_TASK_RUN_ASYNC', False)

    @property
    def BACKGROUND_TASK_ASYNC_THREADS(self):
        """Specify number of concurrent threads."""
        return getattr(settings, 'BACKGROUND_TASK_ASYNC_THREADS', cpu_count)

app_settings = AppSettings()
