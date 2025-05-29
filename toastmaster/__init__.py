import environ
from os.path import dirname, join, exists

env = environ.Env()

BASE_DIR = dirname(__file__)

env_file = join(dirname(BASE_DIR), "config.env")
if not exists(env_file):
    env_file = "/etc/aicore/config.env"

if exists(env_file):
    environ.Env.read_env(str(env_file))
