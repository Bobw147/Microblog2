from flask import render_template
from app import app, db

# Stop pyliint from complaining about dynamically created members not
# being present when the file is checked
# pylint: disable=E1101
 
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500