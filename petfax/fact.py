from flask import (Blueprint, render_template, request, redirect)

bp = Blueprint('fact', __name__, url_prefix = '/facts')

@bp.route('/', methods = ['Get', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)

        return redirect('/facts')
    
    return 'This is the facts index'

@bp.route('/new')
def new_fact():
    return render_template('new_fact.html')