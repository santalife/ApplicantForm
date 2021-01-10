from flask import Flask, render_template, request, redirect, url_for, session
from applicationForm import CreateApplicationForm
import shelve, Applicant
import smtplib
import datetime

app = Flask(__name__)
app.secret_key = 'any_random_string'


@app.route('/')
def home():
    return render_template('home.html')


todayscount = 0


@app.route('/createApplicant', methods=['GET', 'POST'])
def create_applicant():
    # global todayscount
    # x = datetime.datetime.now()
    # currentdate = x.strftime("%d")
    # datelist = []
    # if len(datelist) == 0:
    # datelist.append(currentdate)
    # else:
    # pass

    create_applicant_form = CreateApplicationForm(request.form)

    if request.method == 'POST' and create_applicant_form.validate():
        applicants_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            applicants_dict = db['Applicant']
        except:
            print("Error in retrieving Applicants from storage.db.")

        # parsing parameters into Application Class in Application.py
        applicant = Applicant.Applicant(create_applicant_form.fname.data, create_applicant_form.lname.data,
                                        create_applicant_form.nric.data,
                                        create_applicant_form.email.data, create_applicant_form.age.data,
                                        create_applicant_form.address.data, create_applicant_form.gender.data,
                                        create_applicant_form.nationality.data, create_applicant_form.language.data,
                                        create_applicant_form.phoneno.data, create_applicant_form.quali.data,
                                        create_applicant_form.expe.data, create_applicant_form.comp1.data,
                                        create_applicant_form.posi1.data, create_applicant_form.comp2.data,
                                        create_applicant_form.posi2.data, create_applicant_form.empty.data)

        applicants_dict[applicant.get_applicantid()] = applicant

        db['Applicant'] = applicants_dict

        # if currentdate == datelist[0]:
        # if applicant.get_date() == currentdate:
        # todayscount += 1
        # else:
        # datelist.pop(0)
        # todayscount = 0

        # Automatically Send Email Codes
        sender_email = "nyppolyclinic@gmail.com"
        password = "helloworld123"
        rec_email = create_applicant_form.email.data
        subject = "Application for NYP Polyclinic"
        body = "Hello, we have received your application. Please wait for a few days for us to update you about the status. Thank you."
        message = "Subject: {}\n\n{}".format(subject, body)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("Login Success")
        server.sendmail(sender_email, rec_email, message)
        print("Email has been sent to ", rec_email)
        # Automatically Send Email Codes

        db.close()

        session['applicant_created'] = applicant.get_first_name() + ' ' + applicant.get_last_name()
        return redirect(url_for('create_applicant'))
    return render_template('applicationForm.html', form=create_applicant_form)


@app.route('/retrieveApplicants')
def retrieve_applicants():
    applicants_dict = {}
    db = shelve.open('storage.db', 'r')
    applicants_dict = db['Applicant']
    db.close()

    applicants_list = []

    for key in applicants_dict:
        applicants = applicants_dict.get(key)
        applicants_list.append(applicants)

    return render_template('retrieveApplicants.html', count=len(applicants_list),
                           applicants_list=applicants_list)


@app.route('/updateApplicants/<int:id>/', methods=['GET', 'POST'])
def update_applicants(id):
    update_applicant_form = CreateApplicationForm(request.form)
    if request.method == 'POST' and update_applicant_form.validate():
        applicants_dict = {}
        db = shelve.open('storage.db', 'w')
        applicants_dict = db['Applicant']

        # after submit, setting the updated inputs.
        # problem now is that updated employment does not display
        applicant = applicants_dict.get(id)
        applicant.set_first_name(update_applicant_form.fname.data)
        applicant.set_last_name(update_applicant_form.lname.data)
        applicant.set_nric(update_applicant_form.nric.data)
        applicant.set_email(update_applicant_form.email.data)
        applicant.set_age(update_applicant_form.age.data)
        applicant.set_address(update_applicant_form.address.data)
        applicant.set_gender(update_applicant_form.gender.data)
        applicant.set_nationality(update_applicant_form.nationality.data)
        applicant.set_language(update_applicant_form.language.data)
        applicant.set_phone_number(update_applicant_form.phoneno.data)
        applicant.set_qualification(update_applicant_form.quali.data)
        applicant.set_experience(update_applicant_form.expe.data)
        applicant.set_company1(update_applicant_form.comp1.data)
        applicant.set_postion1(update_applicant_form.posi1.data)
        applicant.set_company2(update_applicant_form.comp2.data)
        applicant.set_postion2(update_applicant_form.posi2.data)
        db['Applicant'] = applicants_dict

        # Automatically Send Email Codes
        sender_email = "nyppolyclinic@gmail.com"
        password = "helloworld123"
        rec_email = applicant.get_email()
        subject = "Application for NYP Polyclinic"
        body = "Hello, we have received your updated application. Please wait for a few days for us to update you about the status. Thank you."
        message = "Subject: {}\n\n{}".format(subject, body)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("Login Success")
        server.sendmail(sender_email, rec_email, message)
        print("Email has been sent to ", rec_email)
        # Automatically Send Email Codes

        db.close()

        session['applicant_updated'] = applicant.get_first_name() + ' ' + applicant.get_last_name()

        return redirect(url_for('home'))

    else:
        applicants_dict = {}
        db = shelve.open('storage.db', 'r')
        applicants_dict = db['Applicant']
        db.close()

        # get data input and place in in the field
        applicant = applicants_dict.get(id)
        update_applicant_form.fname.data = applicant.get_first_name()
        update_applicant_form.lname.data = applicant.get_last_name()
        update_applicant_form.nric.data = applicant.get_user_nric()
        update_applicant_form.email.data = applicant.get_email()
        update_applicant_form.age.data = applicant.get_age()
        update_applicant_form.address.data = applicant.get_address()
        update_applicant_form.gender.data = applicant.get_gender()
        update_applicant_form.nationality.data = applicant.get_nationality()
        update_applicant_form.language.data = applicant.get_language()
        update_applicant_form.phoneno.data = applicant.get_phone_number()
        update_applicant_form.quali.data = applicant.get_qualification()
        update_applicant_form.expe.data = applicant.get_experience()
        update_applicant_form.comp1.data = applicant.get_company1()
        update_applicant_form.posi1.data = applicant.get_position1()
        update_applicant_form.comp2.data = applicant.get_company2()
        update_applicant_form.posi2.data = applicant.get_position2()

        return render_template('updateApplicant.html', form=update_applicant_form)


@app.route('/deleteApplicant/<int:id>', methods=['POST'])
def delete_applicant(id):
    applicants_dict = {}
    db = shelve.open('storage.db', 'w')
    applicants_dict = db['Applicant']

    applicant = applicants_dict.pop(id)

    db['Applicant'] = applicants_dict
    db.close()
    session['applicant_deleted'] = applicant.get_first_name() + ' ' + applicant.get_last_name()
    return redirect(url_for('retrieve_applicants'))


@app.errorhandler(404)
def page_not_handle(e):
    return render_template("error404.html"), 404


if __name__ == '__main__':
    app.run()
