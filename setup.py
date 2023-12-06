from setuptools import setup, find_packages
import codecs

version = __import__('background_task').__version__

classifiers = [c for c in open('classifiers').read().splitlines() if '#' not in c]

setup(
    name='django-bg-tasks',
    version=version,
    description='Database backed asynchronous task queue',
    long_description=codecs.open('README.rst', encoding='utf-8').read(),
    author='Anywyse.audio',
    author_email='admin@arteria.ch',
    url='http://github.com/yunusdemir/django-bg-tasks',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    zip_safe=True,
    classifiers=classifiers,
)
