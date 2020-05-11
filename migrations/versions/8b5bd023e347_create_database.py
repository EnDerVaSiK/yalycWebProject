"""create database

Revision ID: 8b5bd023e347
Revises: 
Create Date: 2020-05-06 17:57:09.612280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b5bd023e347'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyName', sa.String(length=64), nullable=True),
    sa.Column('logoCompany', sa.LargeBinary(), nullable=True),
    sa.Column('tagLine', sa.String(length=64), nullable=True),
    sa.Column('foreword', sa.String(length=256), nullable=True),
    sa.Column('aboutUs', sa.String(length=256), nullable=True),
    sa.Column('workWithUs', sa.String(length=256), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_companyName'), 'company', ['companyName'], unique=True)
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('picture', sa.LargeBinary(), nullable=True),
    sa.Column('describe', sa.String(length=64), nullable=True),
    sa.Column('companyId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['companyId'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    op.drop_index(op.f('ix_company_companyName'), table_name='company')
    op.drop_table('company')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
