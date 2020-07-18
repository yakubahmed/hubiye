from flask import redirect, render_template, request, session, flash
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            flash('SORRY! you have to login first.')
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function