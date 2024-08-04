from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from .models import Users, db
from .forms import LoginForm, SignupForm, UpdateProfileForm
from .signals import is_image_file, compress_image
import os

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        try:
            # Hash the password
            hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')

            # Handle profile picture upload
            profile_pic = form.profile_pic.data
            if profile_pic and is_image_file(profile_pic):
                pic_filename = secure_filename(profile_pic.filename)
                file_path = os.path.join(current_app.root_path, 'static/profile_pics', pic_filename)
                profile_pic.save(file_path)
                compress_image(file_path, file_path)
            else:
                pic_filename = 'default.png'

            # Create a new user
            new_user = Users(
                username=form.username.data,
                password_hash=hashed_password,
                profile_pic=pic_filename,
                name=form.name.data,
                email=form.email.data,
                favorite_color=form.favorite_color.data
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred while creating the account: {e}", 'danger')
    return render_template('auth/signup.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = Users.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                flash("Login Successful", "success")
                return redirect(url_for('main.songs'))
            else:
                flash("Wrong Username or Password", "danger")
        except Exception as e:
            flash(f"An error occurred while logging in: {e}", "danger")
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    try:
        logout_user()
        flash("You have been logged out.", "info")
    except Exception as e:
        flash(f"An error occurred while logging out: {e}", "danger")
    return redirect(url_for('auth.login'))

@auth.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html')

@auth.route('/update_profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    form = UpdateProfileForm(obj=current_user)
    if form.validate_on_submit():
        try:
            # Check if passwords match
            if form.password.data and form.password.data != form.confirm_password.data:
                flash('Passwords do not match. Please try again.', 'danger')
                return render_template('auth/update_profile.html', form=form)

            # Update password if provided
            if form.password.data:
                current_user.password_hash = generate_password_hash(form.password.data, method='pbkdf2:sha256')

            # Update other fields
            if form.name.data:
                current_user.name = form.name.data
            if form.username.data:
                current_user.username = form.username.data
            if form.email.data:
                current_user.email = form.email.data
            if form.favorite_color.data:
                current_user.favorite_color = form.favorite_color.data
            if form.is_admin.data is not None:
                current_user.is_admin = form.is_admin.data

            # Handle profile picture update
            if form.profile_pic.data and hasattr(form.profile_pic.data, 'filename'):
                if is_image_file(form.profile_pic.data):
                    pic_filename = secure_filename(form.profile_pic.data.filename)
                    # Define the file path correctly
                    file_path = os.path.join('static/profile_pics', pic_filename)
                    full_file_path = os.path.join(current_app.root_path, file_path)
                    form.profile_pic.data.save(full_file_path)
                    compress_image(full_file_path, full_file_path)
                    current_user.profile_pic = pic_filename
                else:
                    flash('Invalid file type. Please upload an image file.', 'danger')
                    return render_template('auth/update_profile.html', form=form)

            db.session.commit()
            flash('Your profile has been updated!', 'success')
            return redirect(url_for('main.songs'))
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred while updating your profile: {e}", 'danger')
    else:
        if request.method == 'POST':
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')

    return render_template('auth/update_profile.html', form=form)
