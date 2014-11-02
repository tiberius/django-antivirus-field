from setuptools import setup, find_packages

setup(
    name='django-antivirus-field',
    version='0.2.0',
    packages=find_packages(),
    url='https://github.com/budurli/django-antivirus-field',
    license='MIT',
    author='Maxim Smirnoff',
    author_email='smirnoffmg@gmail.com',
    description='Django FileField with ClamAV protection',
    install_requires=['django', 'pyclamd', 'south'],
)
