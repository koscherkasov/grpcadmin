import os

ENCODING = 'utf-8'
PROTO_BUF_DIR = 'proto_buf'
PROTO_PY_DIR = 'proto_py'
SERVICES_DIR = 'services'
INIT_FILE = '__init__.py'
PROTO_FORMAT = '.proto'
PROTO_TEMPLATE = 'syntax="proto2"\n'


def create_service(name):
    os.makedirs(name, exist_ok=False)
    os.makedirs(os.path.join(name, PROTO_BUF_DIR))
    with open(os.path.join(name, PROTO_BUF_DIR, name + PROTO_FORMAT), 'tw', encoding=ENCODING) as f:
        f.write(PROTO_TEMPLATE)

    os.makedirs(os.path.join(name, PROTO_PY_DIR))
    open(os.path.join(name, PROTO_PY_DIR, INIT_FILE), 'tw').close()

    os.makedirs(os.path.join(name, SERVICES_DIR))
    open(os.path.join(name, SERVICES_DIR, INIT_FILE), 'tw').close()
