from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

from database import Base  # 👈 ONE shared Base
from models import user  # 👈 Import to register the models

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata  # 👈 Use ONE metadata

def run_migrations_offline():
    ...

def run_migrations_online():
    ...

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
