# -*- coding: utf-8 -*-
import signal


class GracefulKiller(object):
    """Catch signals to allow graceful shutdown."""

    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True
