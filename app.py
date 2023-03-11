from flask import Flask, render_template, request, redirect, url_for
from ir_boolean_model import search, PhraseSearch

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        result = search(name)
        
        if not result:
            message = "No Documents found"
        else:
            message = "200"
        return render_template('index.html', result=result, message= message)
    else:
        return render_template('index.html', result=None, message="200")


@app.route('/p_search', methods=['POST'])
def p_search():
    name = request.form['name']
    result = PhraseSearch(name)
    
    if not result:
        message = "No Documents found"
    else:
        message = "200"
        
    return render_template('index.html', p_result=result, p_message=message)
    

@app.route('/p_search', methods=['GET'])
def get_p():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)