from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='job_directory_two',
   version='1.0',
   description='A usefulway to lookup jobs',
   license="MIT",
   author='Kevin Stradtman',
   author_email='stradtkt22@gmail.com',
   url="",
   packages=['job_directory_two'],  #same as name
   install_requires=['django-filters'], #external packages as dependencies
   scripts=[]
)