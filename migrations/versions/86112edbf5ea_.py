"""empty message

Revision ID: 86112edbf5ea
Revises: 
Create Date: 2022-03-15 17:49:32.440923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86112edbf5ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('novbe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filial', sa.String(length=30), nullable=False),
    sa.Column('xidmet', sa.String(length=30), nullable=False),
    sa.Column('date', sa.String(length=30), nullable=False),
    sa.Column('time', sa.String(length=30), nullable=False),
    sa.Column('number', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('xeber',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.Column('describe', sa.String(length=30), nullable=False),
    sa.Column('date', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('xeber')
    op.drop_table('novbe')
    op.drop_table('cards')
    # ### end Alembic commands ###
