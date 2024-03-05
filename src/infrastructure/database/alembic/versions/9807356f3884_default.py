"""default

Revision ID: 9807356f3884
Revises: 
Create Date: 2024-03-03 11:03:21.851720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9807356f3884'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urls',
    sa.Column('hash_id', sa.String(length=7), nullable=False),
    sa.Column('origin_url', sa.String(length=256), nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='true', nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('hash_id', name=op.f('pk_urls'))
    )
    op.create_index(op.f('ix_urls_hash_id'), 'urls', ['hash_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_urls_hash_id'), table_name='urls')
    op.drop_table('urls')
    # ### end Alembic commands ###
