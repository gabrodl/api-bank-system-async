"""add unique constraint

Revision ID: 75f5c7d809e8
Revises: fae4b3a2acce
Create Date: 2026-05-20 20:31:50.632342

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '75f5c7d809e8'
down_revision: Union[str, Sequence[str], None] = 'fae4b3a2acce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_index(
        "ix_bank_accounts_account_number",
        "bank_accounts",
        ["account_number"],
        unique=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index("ix_bank_accounts_account_number", table_name="bank_accounts")
    # ### end Alembic commands ###
