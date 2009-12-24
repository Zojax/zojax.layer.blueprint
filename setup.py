from setuptools import setup, find_packages
import os

version = '0.9'

setup(name='zojax.layer.blueprint',
      version=version,
      description="Skin layer for Blueprint CSS framerwork.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Andrey Fedoseev',
      author_email='andrey.fedoseev@gmail.com',
      url='',
      license='',
      packages=find_packages('src'),
      package_dir={'':'src'},
      namespace_packages=['zojax', 'zojax.layer'],
      include_package_data=True,
      zip_safe=False,
      extras_require = dict(
        test = ['zope.app.testing',]
        ),
      install_requires=[
            'setuptools',
            'zope.interface',
            'zope.component',
            'zojax.resource',
            'zojax.resourcepackage',

          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      dependency_links = ['http://download.zope.org/distribution', 'http://eggs.carduner.net/'],
      )
