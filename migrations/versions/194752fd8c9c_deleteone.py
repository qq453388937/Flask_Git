"""deleteone

Revision ID: 194752fd8c9c
Revises: 21679506b4a8
Create Date: 2018-03-14 00:41:21.642017

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '194752fd8c9c'
down_revision = '21679506b4a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('authors', 'phone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authors', sa.Column('phone', mysql.VARCHAR(length=32), nullable=True))
    # ### end Alembic commands ###
