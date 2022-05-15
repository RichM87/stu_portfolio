from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


# print(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('./WServer/database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')
        # print(file)


def write_to_csv(data):
    with open('./WServer/database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        # print(file)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # error = None
    if request.method == 'POST':
        try:
            # email = request.form['email']
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
        # print(data)
        # print(email)

    else:
        return 'something went wrong'

#     if valid_login(request.form['username'],
#                    request.form['password']):
#         return log_the_user_in(request.form['username'])
#     else:
#         error = 'Invalid username/password'
# # the code below is executed if the request method
# # was GET or the credentials were invalid
# return "form submitted, hooorraaaayyy!!!"

# @app.route("/about.html")
# def about_me():
#     return render_template('about.html')
#
#
# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')
#
#
# @app.route("/services.html")
# def services():
#     return render_template('services.html')
#
# @app.route("/components.html")
# def components():
#     return render_template('components.html')
