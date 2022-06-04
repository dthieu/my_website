from dataclasses import dataclass
from http import server
from flask import Flask, render_template, url_for, request, redirect

# render_template: render a web page from html file
# request: for check post or get method (request.method == "GET | POST")
# redirect: navigation destination webpage ex: redirect("Goodbye.html")

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_root():
    return render_template('index.html')

# @app.route('/index.html')
# def other():
#     return render_template('index.html')

# @app.route('/home.html')
# def my_home():
#     return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template("about.html")

# @app.route('/contact.html')
# def contact():
#     return render_template("contact.html")

# @app.route('/components.html')
# def components():
#     return render_template("components.html")

# @app.route('/works.html')
# def work():
#     return render_template("works.html")

# Instead write a lot of function as above, just using string:page_name
# It will call corressponding web page html
@app.route('/<string:page_name>')
def my_page(page_name):
    return render_template(page_name)

import csv
DATABASE_FILE_PATH = "database.csv"
FIELD_NAME = ['email', 'subject', 'message']
def write_to_csv(data):
    with open(DATABASE_FILE_PATH, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAME)
        writer.writerow(data)
        


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print("Data: ", data)
            write_to_csv(data)
            return redirect("/submitted.html")
        except:
            return "Did not save to database!"
    else:
        return "Something went wrong. Please try again!"