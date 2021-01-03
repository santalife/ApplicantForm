from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, IntegerField


class CreateApplicationForm(Form):
    fname = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    lname = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    nric = StringField('NRIC / FIN', [validators.Length(min=9, max=9,
                                                        message="NRIC/FIN should only consists of 2 Letters and 7 digits. e.g.S1234567A"),
                                      validators.DataRequired()])  # need to validate
    email = StringField('Email', [validators.Length(min=1, max=150), validators.DataRequired()])
    age = IntegerField('Age', [validators.number_range(min=1, max=150), validators.DataRequired()])
    address = StringField('Address', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()],
                         choices=[('', 'Select'), ('Male', 'Male'), ('Female', 'Female')], default='')
    nationality = StringField('Nationality', [validators.Length(min=1, max=150), validators.DataRequired()])
    language = StringField('Language', [validators.Length(min=1, max=150), validators.DataRequired()])
    phoneno = StringField('Phone Number',
                          [validators.Length(min=8, max=8, message="Singapore Phone Number must be 8 numbers only"),
                           validators.DataRequired()])  # need to validate
    quali = SelectField('Highest Qualification', [validators.DataRequired()],
                        choices=[('', 'Select'), ("O'Levels", "O'Levels"), ("N'Levels", "N'Levels"),
                                 ("A'Levels", "A'Levels"), ('Diploma', 'Diploma'), ('Bachelor', 'Bachelor'),
                                 ('Master', 'Master')], default='')
    expe = RadioField('Experience in Healthcare Industry', choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes')
    comp1 = StringField('Company', [validators.Length(min=1, max=150), validators.DataRequired()])
    posi1 = StringField('Position', [validators.Length(min=1, max=150), validators.DataRequired()])
    comp2 = StringField('Company (optional)', [validators.Length(min=1, max=150), validators.optional()])
    posi2 = StringField('Position (optional)', [validators.Length(min=1, max=150), validators.optional()])
    empty = StringField('empty', [validators.Length(min=1, max=150), validators.optional()])

# name=input("Enter Name: ")
# nric=input("Enter Nric: ")
# email=input("Enter Email")
# age=input("Enter Age")
# address=input("Enter address")
# gender=input("Enter Gender")
# phonenumber=input("Enter Phone Number")
# qualification=input("Enter Qualification")
# experience=input("Enter Experience")
# company=input("Enter company")
# position=input("Enter Position")

"""
name = "Ewan"
nric = "T0315361J"
email = "kaivert@Hotmail.com"
age = 17
address = "Eunos"
gender = "M"
phonenumber = 82661667
qualification = "O'levels"
experience = "null"
company = "18 Chefs"
position = "Server/Runner"
"""
