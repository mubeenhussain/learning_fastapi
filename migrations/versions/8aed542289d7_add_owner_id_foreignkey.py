"""Add owner_id ForeignKey

Revision ID: 8aed542289d7
Revises: 10132e9a88ea
Create Date: 2025-07-08 01:32:12.491305

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8aed542289d7'
down_revision: Union[str, Sequence[str], None] = '10132e9a88ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
