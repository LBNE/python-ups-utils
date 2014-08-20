from setuptools import setup
setup(name = 'ups-util',
      version = '0.0',
      description = 'UPS Utilities',
      author = 'Brett Viren',
      author_email = 'brett.viren@gmail.com',
      license = 'GPLv2',
      url = 'http://github.com/brettviren/ups-utils',
      package_dir = {'':'python'},
      packages = ['ups'],
      install_requires=[
          "networkx",
          "click"
      ],
      entry_points = {
          'console_scripts': [
              'urman = ups.urman:main',
          ]
      }
)
