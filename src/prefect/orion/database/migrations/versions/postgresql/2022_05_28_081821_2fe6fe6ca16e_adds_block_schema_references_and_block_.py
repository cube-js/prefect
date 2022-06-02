"""Adds block schema references and block document references

Revision ID: 2fe6fe6ca16e
Revises: 724e6dcc6b5d
Create Date: 2022-05-28 08:18:21.527986

"""
import sqlalchemy as sa
from alembic import op

import prefect

# revision identifiers, used by Alembic.
revision = "2fe6fe6ca16e"
down_revision = "724e6dcc6b5d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "block_schema_reference",
        sa.Column(
            "id",
            prefect.orion.utilities.database.UUID(),
            server_default=sa.text("(GEN_RANDOM_UUID())"),
            nullable=False,
        ),
        sa.Column(
            "created",
            prefect.orion.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated",
            prefect.orion.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column(
            "parent_block_schema_id",
            prefect.orion.utilities.database.UUID(),
            nullable=False,
        ),
        sa.Column(
            "reference_block_schema_id",
            prefect.orion.utilities.database.UUID(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["parent_block_schema_id"],
            ["block_schema.id"],
            name=op.f(
                "fk_block_schema_reference__parent_block_schema_id__block_schema"
            ),
            ondelete="cascade",
        ),
        sa.ForeignKeyConstraint(
            ["reference_block_schema_id"],
            ["block_schema.id"],
            name=op.f(
                "fk_block_schema_reference__reference_block_schema_id__block_schema"
            ),
            ondelete="cascade",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_block_schema_reference")),
    )
    op.create_index(
        op.f("ix_block_schema_reference__updated"),
        "block_schema_reference",
        ["updated"],
        unique=False,
    )
    op.create_table(
        "block_document_reference",
        sa.Column(
            "id",
            prefect.orion.utilities.database.UUID(),
            server_default=sa.text("(GEN_RANDOM_UUID())"),
            nullable=False,
        ),
        sa.Column(
            "created",
            prefect.orion.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated",
            prefect.orion.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column(
            "parent_block_document_id",
            prefect.orion.utilities.database.UUID(),
            nullable=False,
        ),
        sa.Column(
            "reference_block_document_id",
            prefect.orion.utilities.database.UUID(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["parent_block_document_id"],
            ["block_document.id"],
            name=op.f(
                "fk_block_document_reference__parent_block_document_id__block_document"
            ),
            ondelete="cascade",
        ),
        sa.ForeignKeyConstraint(
            ["reference_block_document_id"],
            ["block_document.id"],
            name=op.f(
                "fk_block_document_reference__reference_block_document_id__block_document"
            ),
            ondelete="cascade",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_block_document_reference")),
    )
    op.create_index(
        op.f("ix_block_document_reference__updated"),
        "block_document_reference",
        ["updated"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_block_document_reference__updated"),
        table_name="block_document_reference",
    )
    op.drop_table("block_document_reference")
    op.drop_index(
        op.f("ix_block_schema_reference__updated"), table_name="block_schema_reference"
    )
    op.drop_table("block_schema_reference")
    # ### end Alembic commands ###