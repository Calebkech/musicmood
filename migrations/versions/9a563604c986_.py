"""empty message

Revision ID: 9a563604c986
Revises: a0b7aef0f033
Create Date: 2024-06-14 18:45:45.971389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a563604c986'
down_revision = 'a0b7aef0f033'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('playlist_song')
    op.drop_table('rating')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rating',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('value', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('song_id', sa.INTEGER(), nullable=True),
    sa.Column('playlist_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlist.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['song_id'], ['song.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('playlist_song',
    sa.Column('playlist_id', sa.INTEGER(), nullable=True),
    sa.Column('song_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlist.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['song.id'], )
    )
    # ### end Alembic commands ###
