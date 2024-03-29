"""create student tables

Revision ID: aaf1893099b8
Revises: 
Create Date: 2024-02-20 19:13:47.100382

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "aaf1893099b8"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "course",
        sa.Column("Id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("Name", sa.String(length=255), nullable=False),
        sa.Column("Major", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("Id"),
    )
    op.create_table(
        "student",
        sa.Column("Id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("Name", sa.String(length=255), nullable=False),
        sa.Column("Major", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("Id"),
    )
    op.create_table(
        "registration",
        sa.Column("StudentId", sa.Integer(), nullable=False),
        sa.Column("CourseId", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["CourseId"],
            ["course.Id"],
        ),
        sa.ForeignKeyConstraint(
            ["StudentId"],
            ["student.Id"],
        ),
        sa.PrimaryKeyConstraint("StudentId", "CourseId"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("registration")
    op.drop_table("student")
    op.drop_table("course")
    # ### end Alembic commands ###
