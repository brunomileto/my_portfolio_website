from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)


@app.route('/')
def init_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page_generator(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            database_object = database.Database(data)
            database_object.write_to_file()
            database_object.wrote_to_csv()
            database_object.write_to_json()
            database_object.firebase_database_writer()
            # database_object.firebase_database_retrieve_data()
            return redirect("thank_you.html")
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again!'

