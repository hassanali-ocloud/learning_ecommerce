"""create apt_num in address table

Revision ID: 0c40fc625f04
Revises: 32a62002e63b
Create Date: 2025-09-29 05:49:27.467737

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c40fc625f04'
down_revision: Union[str, Sequence[str], None] = '32a62002e63b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('address', sa.Column('apt_num', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("address", "apt_num")
