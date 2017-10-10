from setuptools import setup, find_packages

setup(name='ncssl-api-client',
      version='0.1',
      description='Command line interface for Namecheap SSL API',
      url='TO BE DEFINED',
      author='Anton Ku',
      author_email='anton.ku.nc@gmail.com',
      license='MIT',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      install_requires=[
          'requests',
          'mock',
          'xmltodict',
          'pyyaml',
          'coloredlogs',
          'ipgetter',
      ],
      entry_points={
          'console_scripts': ['ncsslapi=ncssl_api_client.ncsslapi:main'],
      },
      test_suite='tests',
      include_package_data=True,
      zip_safe=False)