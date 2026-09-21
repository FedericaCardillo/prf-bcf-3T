from setuptools import setup

#with open("README", 'r') as f:
#    long_description = f.read()

setup(
   name='prf-bcf-3T',
   version='1.0',
   description='Preprocessing anatomical and functional MRI data',
   license="MIT",
   # long_description=long_description,
   author='FedericaCardillo',
   author_email='f.cardillo@umcg.nl',
   url="https://github.com/FedericaCardillo1999/prf-bcf-3T",
   packages=['EGRET3APreproc'],  #same as name
   install_requires=['wheel', 'bar', 'greek']
)
