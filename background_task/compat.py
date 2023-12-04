from django.db import close_old_connections


def close_connection():
    close_old_connections()