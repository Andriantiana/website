"""new fields in user model

Revision ID: 8544a74a4c90
Revises: 221f7a357250
Create Date: 2020-04-01 13:14:01.685098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8544a74a4c90'
down_revision = '221f7a357250'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
