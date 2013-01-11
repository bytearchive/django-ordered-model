from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='django-ordered-model',
      version='0.2.0',
      description='Allows Django models to be ordered and provides a simple admin interface for reordering them.',
      long_description=readme(),
      author='Ben Firshman',
      author_email='ben@firshman.co.uk',
      url='https://github.com/bfirsh/django-ordered-model',
      packages=[
          'ordered_model',
          'ordered_model.tests',
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
      ],
      package_data={
          'ordered_model': [
              'static/ordered_model/arrow-up.gif',
              'static/ordered_model/arrow-down.gif',
              'locale/de/LC_MESSAGES/django.po',
              'locale/de/LC_MESSAGES/django.mo',
              'locale/pl/LC_MESSAGES/django.po',
              'locale/pl/LC_MESSAGES/django.mo',
          ]
      })
