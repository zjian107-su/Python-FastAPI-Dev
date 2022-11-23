"""add user table

Revision ID: 5696963a058c
Revises: 86b68f25d808
Create Date: 2022-11-22 01:33:42.628764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5696963a058c'
down_revision = '86b68f25d808'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'),
                              nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
