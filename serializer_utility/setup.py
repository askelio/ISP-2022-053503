from setuptools import setup

setup(name='Serializer',
      version='1.0',
      description='Python Distribution Utilities',
      author='Alex Hryharovich',
      author_email='gogolyadza@gmail.com',
      packages=['SerializerFactory', 'SerializerFactory.Serializers', 'ConsoleUtility', 'ConsoleUtility.Files','Tests'],
      install_requires=['PyYaml == 6.0',
                        'PyToml == 0.1.21'],
      entry_points={'console_scripts': ['utility = ConsoleUtility.utility:utility_code']}
      )
