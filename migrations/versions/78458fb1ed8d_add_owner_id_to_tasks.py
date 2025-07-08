"""Add owner_id to tasks

Revision ID: 78458fb1ed8d
Revises: 8aed542289d7
Create Date: 2025-07-08 17:43:26.338277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '78458fb1ed8d'
down_revision: Union[str, Sequence[str], None] = '8aed542289d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('tasks', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.create_foreign_key(
        'fk_tasks_owner_id_users',
        'tasks',
        'users',
        ['owner_id'],
        ['id']
    )


def downgrade() -> None:
    op.drop_constraint('fk_tasks_owner_id_users', 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'owner_id')

