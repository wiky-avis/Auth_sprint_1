"""delete colum login

Revision ID: ec609b56f6b4
Revises: aa15c0dc0e24
Create Date: 2023-04-08 10:21:53.492683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec609b56f6b4'
down_revision = 'aa15c0dc0e24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_roles_id'), ['id'])

    with op.batch_alter_table('user_role', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_role_id'), ['id'])

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('uq_users_login', type_='unique')
        batch_op.create_unique_constraint(batch_op.f('uq_users_id'), ['id'])
        batch_op.drop_column('login')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('login', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(batch_op.f('uq_users_id'), type_='unique')
        batch_op.create_unique_constraint('uq_users_login', ['login'])

    with op.batch_alter_table('user_role', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_role_id'), type_='unique')

    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_roles_id'), type_='unique')

    # ### end Alembic commands ###
