"""add role field

Revision ID: 5ebb8f3681c2
Revises: b73cadc62c35
Create Date: 2024-06-09 18:02:55.432355

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel



# revision identifiers, used by Alembic.
revision: str = '5ebb8f3681c2'
down_revision: Union[str, None] = 'b73cadc62c35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'books', ['uid'])
    op.add_column('user_accounts', sa.Column('role', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_accounts', 'role')
    op.drop_constraint(None, 'books', type_='unique')
    # ### end Alembic commands ###
