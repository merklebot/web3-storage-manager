"""add filesize field to content

Revision ID: a184d34a2914
Revises: d1722de59635
Create Date: 2022-12-19 04:05:13.923114

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a184d34a2914"
down_revision = "d1722de59635"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("content", sa.Column("filesize", sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("content", "filesize")
    # ### end Alembic commands ###
