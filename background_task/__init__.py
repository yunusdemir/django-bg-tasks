__version__ = '0.1.10'


def background(*arg, **kw):
    from .tasks import tasks
    return tasks.background(*arg, **kw)
