"""add foreign key to posts table

Revision ID: 6845c93c9676
Revises: 5696963a058c
Create Date: 2022-11-22 01:40:17.769035

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6845c93c9676'
down_revision = '5696963a058c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
