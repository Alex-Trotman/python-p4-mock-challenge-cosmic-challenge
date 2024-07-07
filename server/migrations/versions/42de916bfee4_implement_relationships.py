"""implement relationships

Revision ID: 42de916bfee4
Revises: 56afe28e328c
Create Date: 2024-07-07 12:11:41.581839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42de916bfee4'
down_revision = '56afe28e328c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('missions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('scientist_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_missions_scientist_id_scientists'), 'scientists', ['scientist_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_missions_planet_id_planets'), 'planets', ['planet_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('missions', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_missions_planet_id_planets'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_missions_scientist_id_scientists'), type_='foreignkey')
        batch_op.drop_column('scientist_id')
        batch_op.drop_column('planet_id')

    # ### end Alembic commands ###
