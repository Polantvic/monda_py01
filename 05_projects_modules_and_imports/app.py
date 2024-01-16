from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(name="Studentas"):
    if request.method == "POST":
        if 'name' in request.form:
            name = request.form['name']
    return render_template('index.html', name=name)

app.run()
