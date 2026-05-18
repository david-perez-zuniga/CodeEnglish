"""empty message

Revision ID: ddc1854ac26f
Revises: e17ac3bb295d
Create Date: 2026-05-18 10:55:20.264085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ddc1854ac26f'
down_revision: Union[str, Sequence[str], None] = 'e17ac3bb295d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
