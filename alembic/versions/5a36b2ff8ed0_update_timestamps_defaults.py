"""update timestamps defaults

Revision ID: 5a36b2ff8ed0
Revises: 75f5c7d809e8
Create Date: 2026-05-20 21:38:33.029250

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a36b2ff8ed0'
down_revision: Union[str, Sequence[str], None] = '75f5c7d809e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "bank_accounts",
        "created_at",
        server_default=sa.text("now()"),
    )

    op.alter_column(
        "bank_accounts",
        "updated_at",
        server_default=sa.text("now()"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "bank_accounts",
        "created_at",
        server_default=None,
    )
    
    op.alter_column(
        "bank_accounts",
        "updated_at",
        server_default=None,
    )
    # ### end Alembic commands ###
