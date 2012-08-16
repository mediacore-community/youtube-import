#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
      name='YouTubeImportMC',
      version='0.6',

      author='Felix Schwarz',
      author_email='info@schwarz.eu',
      license='GPL v3 or later', # see LICENSE.txt
        
      packages=find_packages(),
      namespace_packages = ['mcore'],
      include_package_data=True,
      package_data = {
          'mcore.youtube_import.templates': ['admin/*'],
      },
      entry_points = {
          'mediacore.plugin': [
              'youtube_import = mcore.youtube_import.mediacore_plugin',
          ],
      }
)

