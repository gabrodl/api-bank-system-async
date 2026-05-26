"""update timestamps defaults transactions

Revision ID: eacddb7b6658
Revises: 5a36b2ff8ed0
Create Date: 2026-05-21 13:44:43.410706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'eacddb7b6658'
down_revision: Union[str, Sequence[str], None] = '5a36b2ff8ed0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_column("transactions", "updated_at")
    
    op.alter_column(
        "transactions",
        "created_at",
        server_default=sa.text("now()"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "transactions",
        sa.Column("updated_at",
                  postgresql.TIMESTAMP(),
                  autoincrement=False,
                  nullable=True
        )
    )
    
    op.alter_column(
        "transactions",
        "created_at",
        server_default=None,
    )
    # ### end Alembic commands ###
