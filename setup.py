from setuptools import setup

setup(name='grpcadmin',
      version='0.1',
      description='Admin for hrpc',
      url='https://github.com/koscherkasov/grpcadmin',
      author='',
      author_email='john@example.com',
      license='MIT',
      packages=['grpcadmin'],
      zip_safe=False,
      # install_requires=[
      #       'click',
      # ],
      entry_points='''
          [console_scripts]
          grpc-admin=grpcadmin.command_line:cli
      ''',
      )