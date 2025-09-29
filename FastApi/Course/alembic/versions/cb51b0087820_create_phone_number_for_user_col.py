"""create phone number for user col

Revision ID: cb51b0087820
Revises: 
Create Date: 2025-09-29 04:21:47.207722

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb51b0087820'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String() , nullable=True))

def downgrade() -> None:
    op.drop_column('users', 'phone_number')    
