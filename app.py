from flask import Flask, render_template, request, redirect, url_for
from ir_boolean_model import search, PhraseSearch, ProximitySearch

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


@app.route('/phrase_search', methods=['POST'])
def phrase_search():
    name = request.form['name']
    result = PhraseSearch(name)
    
    if not result:
        message = "No Documents found"
    else:
        message = "200"
        
    return render_template('index.html', p_result=result, p_message=message)
    

@app.route('/phrase_search', methods=['GET'])
def redirect_phrase():
    return redirect(url_for('index'))


@app.route('/proximity_search', methods=['POST'])
def proximity_search():
    name = request.form['name']
    result = ProximitySearch(name)
    
    if not result:
        message = "No Documents found"
    else:
        message = "200"
        
    return render_template('index.html', prox_result=result, prox_message=message)
    

@app.route('/prox_search', methods=['GET'])
def redirect_proximity():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)