"""empty message

Revision ID: 414d4bda1fa4
Revises: 
Create Date: 2024-03-13 12:32:55.508767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '414d4bda1fa4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('num_bedrooms', sa.Integer(), nullable=True),
    sa.Column('num_bathrooms', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('photo_filename', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
