import re
from flask import Blueprint, render_template, request

contact_bp = Blueprint('contact', __name__, template_folder='../templates')

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    message = ''
    message_type = ''
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        # Validation
        if not name or not email:
            message = 'Both name and email are required.'
            message_type = 'error'
        elif not re.fullmatch(r'[A-Za-z]+', name):
            message = 'Name must contain only alphabets (no numbers or special characters).'
            message_type = 'error'
        elif '@' not in email or '.' not in email:
            message = 'Please enter a valid email address.'
            message_type = 'error'
        else:
            message = f'Thank you, {name}! Your contact information has been submitted.'
            message_type = 'success'
    return render_template('contact.html', message=message, message_type=message_type)