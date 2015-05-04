__version__ = '0.1.11'


def background(*arg, **kw):
    from .tasks import tasks
    return tasks.background(*arg, **kw)
