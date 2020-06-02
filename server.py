from flask import Flask, render_template, request, redirect
import my_portfolio_website.database as database

# Standard Flask code
app = Flask(__name__)


@app.route('/')     # Setting the main route
def init_page():
    """
    Just run the render_template function, in the html home page
    :return:
    """
    return render_template('index.html')


@app.route('/<string:page_name>')   # Setting other routes
def html_page_generator(page_name):
    """
    This functions takes the param page_name. It was passed by the variable on the decorator. <string:page_name> gets
    the name of the html archive inside the default folder './templates' and render it.
    :param page_name: the name of the html archive
    :return:
    """
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])     # Setting the form submit route
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            database_object = database.Database(data)
            database_object.write_to_file()
            database_object.wrote_to_csv()
            database_object.write_to_json()
            database_object.firebase_database_writer()
            return redirect("thank_you.html")
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again!'





