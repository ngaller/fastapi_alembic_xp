"""create hero table

Revision ID: a99f1b59bd3e
Revises: 
Create Date: 2022-04-07 16:16:58.181352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a99f1b59bd3e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'hero',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('secret_name', sa.String(50), nullable=False),
        sa.Column('weapon', sa.String(50), nullable=True),
        sa.Column('age', sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table('hero')
