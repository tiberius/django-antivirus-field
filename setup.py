from distutils.core import setup

setup(
    name='django-antivirus-field',
    version='0.1.0',
    packages=[''],
    url='https://github.com/budurli/django-antivirus-field',
    license='MIT',
    author='Maxim Smirnoff',
    author_email='smirnoffmg@gmail.com',
    description='Django FileField with ClamAV protection',
    requires=['django', 'pyclamd', 'south'],
)
