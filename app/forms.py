from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField, DateField, FileField
from wtforms.validators import DataRequired, EqualTo, Length, Email, Optional
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField
from flask_wtf.file import FileField

# Create a Form Class
class UserForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	username = StringField("Username", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	favorite_color = StringField("Favorite Color")
	password_hash = PasswordField('Password', validators=[DataRequired(), EqualTo('password_hash2', message='Passwords Must Match!')])
	password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
	profile_pic = FileField("Profile Pic")
	submit = SubmitField("Submit")

#Create new song
class SongForm(FlaskForm):
	title = StringField("Title", validators=[DataRequired()])
	artist = StringField("Artist", validators=[DataRequired()])
	album = StringField("Album", validators=[DataRequired()])
	genre = StringField("Genre", validators=[DataRequired()])
	release_date = DateField("Release Date", format='%Y-%m-%d', validators=[DataRequired()])
	song_file = FileField("Song File", validators=[DataRequired()])
	song_profile = FileField("Song Image")
	submit = SubmitField("Submit")

#Create new Playlist
class PlaylistForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	description = StringField("Description", validators=[DataRequired()])
	playlist_profile = FileField("Image")
	submit = SubmitField("Submit")

#LoginForm
class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Login")

class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    favorite_color = StringField("Favorite Color")
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    profile_pic = FileField('Profile Picture')
    submit = SubmitField('Sign Up')

class UpdateProfileForm(FlaskForm):
    name = StringField('Name', validators=[Optional(), Length(min=2, max=20)])
    username = StringField('Username', validators=[Optional(), Length(min=2, max=20)])
    email = StringField("Email", validators=[Optional(), Email()])
    favorite_color = StringField("Favorite Color")
    password = PasswordField('New Password', validators=[Optional()])
    confirm_password = PasswordField('Confirm New Password', validators=[Optional(), EqualTo('password')])
    profile_pic = FileField('Profile Picture')
    submit = SubmitField('Update')