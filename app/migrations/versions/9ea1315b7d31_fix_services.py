"""fix services

Revision ID: 9ea1315b7d31
Revises: 5bcdf8012709
Create Date: 2024-01-04 19:52:27.723708

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '9ea1315b7d31'
down_revision: Union[str, None] = '5bcdf8012709'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('services', sa.JSON(), nullable=True))
    op.drop_column('hotels', 'service')
    op.add_column('rooms', sa.Column('services', sa.JSON(), nullable=False))
    op.drop_column('rooms', 'service')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rooms', sa.Column('service', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False))
    op.drop_column('rooms', 'services')
    op.add_column('hotels', sa.Column('service', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.drop_column('hotels', 'services')
    # ### end Alembic commands ###