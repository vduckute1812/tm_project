import environ
from os.path import dirname, join, exists
from threading import local
from split_settings.tools import include
from django.conf import settings

env = environ.Env()

BASE_DIR = dirname(dirname(__file__))

env_file = join(dirname(BASE_DIR), "config.env")
if not exists(env_file):
    env_file = "/toastmaster/config.env"

if exists(env_file):
    environ.Env.read_env(str(env_file))

APP_ENVIRONMENT = env.str("ENVIRONMENT", default="development")
include( *(f"environments/{APP_ENVIRONMENT}.py", "configs/[!_]*.py"))

tm_local = local()
