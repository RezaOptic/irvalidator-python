from setuptools import setup, find_packages


setup(name='irvalidator',
      version='0.1',
      url='https://github.com/RezaOptic/irvalidator',
      license='MIT',
      author='Reza Noori',
      author_email='rezaoptic@yahoo.com',
      description='IBAN, National Id, Bank Card Number, MobileNumber',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False,
      test_suite='nose.collector')
