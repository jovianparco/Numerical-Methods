from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pacakage',
  version='1',
  description='Modules for Finding Roots',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Bedana, Enerio, Gonzales, Parco',
  author_email='majelyn.mhae.enerio@adamson.edu.ph',
  license='MIT', 
  classifiers=classifiers,
  keywords='roots', 
  packages=find_packages(),
  install_requires=[''] 
)