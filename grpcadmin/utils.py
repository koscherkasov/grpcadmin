import os

ENCODING = 'utf-8'
PROTO_BUF_DIR = 'proto_buf'
PROTO_PY_DIR = 'proto_py'
SERVICES_DIR = 'services'
INIT_FILE = '__init__.py'
PROTO_FORMAT = '.proto'
PROTO_TEMPLATE = 'syntax="proto2"\n'


def create_service(name):
    """Creating stub dirs service

    :param name: services name
    :type name: str
    """

    # create common dir for service
    os.makedirs(name, exist_ok=False)

    # create proto_buf dir with proto file
    os.makedirs(os.path.join(name, PROTO_BUF_DIR))
    with open(os.path.join(name, PROTO_BUF_DIR, name + PROTO_FORMAT), 'w', encoding=ENCODING) as f:
        f.write(PROTO_TEMPLATE)

    # create package proto_py
    os.makedirs(os.path.join(name, PROTO_PY_DIR))
    open(os.path.join(name, PROTO_PY_DIR, INIT_FILE), 'w').close()

    # create package services
    os.makedirs(os.path.join(name, SERVICES_DIR))
    open(os.path.join(name, SERVICES_DIR, INIT_FILE), 'w').close()
