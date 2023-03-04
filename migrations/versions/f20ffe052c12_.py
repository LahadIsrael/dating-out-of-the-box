"""empty message

Revision ID: f20ffe052c12
Revises: 
Create Date: 2023-03-04 00:51:36.012360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f20ffe052c12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('profile_pic', sa.String(length=120), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('gender', sa.String(length=120), nullable=False),
    sa.Column('interests', sa.String(length=120), nullable=True),
    sa.Column('sexual_interests', sa.String(length=120), nullable=True),
    sa.Column('is_online', sa.Boolean(), nullable=True),
    sa.Column('current_plan', sa.String(length=120), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('global__messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=250), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('profile_pic', sa.String(length=120), nullable=True),
    sa.Column('groups_longitude', sa.Float(), nullable=True),
    sa.Column('groups_latitude', sa.Float(), nullable=True),
    sa.Column('gender', sa.String(length=120), nullable=True),
    sa.Column('interests', sa.String(length=120), nullable=True),
    sa.Column('is_online', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('groups_activity_type', sa.String(length=120), nullable=True),
    sa.Column('groups_guidelines', sa.String(length=250), nullable=True),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=250), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user__review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('payload', sa.String(length=250), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user__review')
    op.drop_table('messages')
    op.drop_table('groups')
    op.drop_table('global__messages')
    op.drop_table('user')
    # ### end Alembic commands ###
