"""add content column to the post table

Revision ID: 86b68f25d808
Revises: a37bc3cb1053
Create Date: 2022-11-22 00:30:48.536064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86b68f25d808'
down_revision = 'a37bc3cb1053'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('post', 'content')
    pass
