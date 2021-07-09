"""Initial migration.

Revision ID: 54d7657ce68c
Revises: 
Create Date: 2021-07-09 17:11:13.904653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54d7657ce68c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Articulos',
    sa.Column('SKU', sa.Integer(), nullable=False),
    sa.Column('Nombre', sa.String(length=1020), nullable=True),
    sa.Column('Precio', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('SKU')
    )
    op.create_index(op.f('ix_Articulos_Precio'), 'Articulos', ['Precio'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=280), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_timestamp'), 'posts', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_timestamp'), table_name='posts')
    op.drop_table('posts')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_Articulos_Precio'), table_name='Articulos')
    op.drop_table('Articulos')
    # ### end Alembic commands ###