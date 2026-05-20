"""create_tables

Revision ID: fae4b3a2acce
Revises: 
Create Date: 2026-05-18 19:03:52.038921

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fae4b3a2acce'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('bank_accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_number', sa.String(), nullable=False),
    sa.Column('balance', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('DEPOSIT', 'WITHDRAW', name='transactiontype'), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['bank_accounts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('transactions')
    op.drop_table('bank_accounts')
    op.execute("DROP TYPE transactiontype")
    # ### end Alembic commands ###
