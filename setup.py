from setuptools import setup, find_packages

setup(name='ncssl-api-client',
      version='1.0.1',
      description='Command line interface for Namecheap SSL API',
      url='https://github.com/antonku/ncssl_api_client',
      author='Anton Kudinov',
      author_email='anton.ku.nc@gmail.com',
      license='MIT',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      install_requires=[
          'future',
          'enum34',
          'requests',
          'mock',
          'xmltodict',
          'pyyaml',
          'coloredlogs',
          'ipgetter',
      ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'License :: OSI Approved :: MIT License',
      ],
      entry_points={
          'console_scripts': ['ncsslapi=ncssl_api_client.__main__:main_cli_wrapper'],
      },
      test_suite='tests',
      include_package_data=True,
      zip_safe=False)
