from . import email
from flask import redirect, url_for, flash
from flask_mail import Message
from .. import mail, MAIL_USERNAME
from .forms import subscription_form


@email.route("/subscribe")
def subscribe():
    form = subscription_form()
    if form.validate_on_submit():
        subemail = form.email.data
        msg = Message('Hello user.', recipients=subemail)
        msg.html = '<h2>Welcome to Simakush-Blogging-Website.</h2> <p>This is a personal blogging website where you can create and share your opinions and other users can read and comment on them. This website has a feature that displays random quotes to inspire their users.</p>'
        mail.send(msg)
        flash('You have been added to our subscription', 'success')
        return redirect(url_for('main.home'))

    return redirect(url_for('main.home'))