"""empty message

Revision ID: 1ee542bb34ca
Revises: 4d64b208cbdb
Create Date: 2022-06-12 13:55:57.214864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ee542bb34ca'
down_revision = '4d64b208cbdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('branchs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('branchs')
    # ### end Alembic commands ###
