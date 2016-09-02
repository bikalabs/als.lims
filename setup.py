import os
from setuptools import setup, find_packages

version = '0.1'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(name='als.lims',
      version=version,
      description="ALS LIMS",
      long_description=read("README.rst") + \
                       read("CHANGES.rst") + \
                       "\n\n" + \
                       "Authors and maintainers\n" + \
                       "-----------------------\n" + \
                       "- Bika Lab Systems, http://bikalabs.com\n" + \
                       "- Naralabs, http://naralabs.com",
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Intended Audience :: Information Technology",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
      ],
      keywords=['lims', 'opensource'],
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['als'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'robotsuite',
              'robotframework-selenium2library',
              'plone.app.robotframework',
              'Products.PloneTestCase',
              'robotframework-debuglibrary',
              'plone.resource',
              'plone.app.textfield',
          ]
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
