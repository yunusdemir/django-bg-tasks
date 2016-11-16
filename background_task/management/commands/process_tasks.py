# -*- coding: utf-8 -*-
import logging
import time

from django import VERSION
from django.core.management.base import BaseCommand

from background_task.tasks import tasks, autodiscover


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Run tasks that are scheduled to run on the queue'

    # Command options are specified in an abstract way to enable Django < 1.8 compatibility
    OPTIONS = (
        (('--duration', ), {
            'action': 'store',
            'dest': 'duration',
            'type': int,
            'default': 0,
            'help': 'Run task for this many seconds (0 or less to run forever) - default is 0',
        }),
        (('--sleep', ), {
            'action': 'store',
            'dest': 'sleep',
            'type': float,
            'default': 5.0,
            'help': 'Sleep for this many seconds before checking for new tasks (if none were found) - default is 5',
        }),
        (('--queue', ), {
            'action': 'store',
            'dest': 'queue',
            'help': 'Only process tasks on this named queue',
        }),
    )

    if VERSION < (1, 8):
        from optparse import make_option
        option_list = BaseCommand.option_list + tuple([make_option(*args, **kwargs) for args, kwargs in OPTIONS])

    # Used in Django >= 1.8
    def add_arguments(self, parser):
        for (args, kwargs) in self.OPTIONS:
            parser.add_argument(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self._tasks = tasks

    def handle(self, *args, **options):
        duration = options.pop('duration', 0)
        sleep = options.pop('sleep', 5.0)
        queue = options.pop('queue', None)

        autodiscover()

        start_time = time.time()

        while (duration <= 0) or (time.time() - start_time) <= duration:
            if not self._tasks.run_next_task(queue):
                logger.debug('waiting for tasks')
                time.sleep(sleep)
