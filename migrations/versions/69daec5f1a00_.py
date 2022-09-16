"""empty message

Revision ID: 69daec5f1a00
Revises: 1ee542bb34ca
Create Date: 2022-06-12 18:08:03.272298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69daec5f1a00'
down_revision = '1ee542bb34ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('services')
    # ### end Alembic commands ###
