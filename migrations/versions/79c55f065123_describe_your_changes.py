"""Describe your changes

Revision ID: 79c55f065123
Revises: 78458fb1ed8d
Create Date: 2025-07-15 20:44:01.669134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79c55f065123'
down_revision: Union[str, Sequence[str], None] = '78458fb1ed8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
