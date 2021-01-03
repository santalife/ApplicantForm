import datetime


class Person:
    count_id = 0

    def __init__(self, nric, first_name, last_name, gender, age, phone_number, email, password, address):
        Person.count_id += 1
        self.__Person_id = Person.count_id
        self.__nric = nric
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__age = age
        self.__phone_number = phone_number
        self.__email = email
        self.__password = password
        self.__address = address

    def get_Person_id(self):
        return self.__Person_id

    def get_user_nric(self):
        return self.__nric

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_name(self):
        return self.__first_name + " " + self.__last_name

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_address(self):
        return self.__address

    def set_Person_id(self, Person_id):
        self.__Person_id = Person_id

    def set_nric(self, nric):
        self.__nric = nric

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_gender(self, gender):
        self.__gender = gender

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_address(self, address):
        self.__address = address


class Applicant(Person):
    count_id = 0
    x = datetime.datetime.now()

    def __init__(self, first_name, last_name, nric, email, age, address, gender, nationality, language, phonenumber,
                 qualification,
                 experience, company1,
                 position1, company2, position2, empty):
        super().__init__(nric, first_name, last_name, gender, age, phonenumber, email, empty, address, )
        Applicant.count_id += 1
        self.__applicantid = Applicant.count_id
        self.__nationality = nationality
        self.__language = language
        self.__qualification = qualification
        self.__experience = experience
        self.__company1 = company1
        self.__position1 = position1
        self.__company2 = company2
        self.__position2 = position2
        self.__date = Applicant.x.strftime("%x")

    def set_applicantid(self, applicant_id):
        self.__applicantid = applicant_id

    def set_nationality(self, nationality):
        self.__nationality = nationality

    def set_language(self, language):
        self.__language = language

    def set_qualification(self, qualification):
        self.__qualification = qualification

    def set_experience(self, experience):
        while True:
            try:
                experience
            except ValueError:
                print("You can only enter Yes or Null")
                continue
            else:
                self.__experience = experience
                break

    def set_company1(self, company1):
        self.__company1 = company1

    def set_postion1(self, position1):
        self.__position1 = position1

    def set_company2(self, company2):
        self.__company2 = company2

    def set_postion2(self, position2):
        self.__position2 = position2

    def get_applicantid(self):
        return self.__applicantid

    def get_nationality(self):
        return self.__nationality

    def get_language(self):
        return self.__language

    def get_qualification(self):
        return self.__qualification

    def get_experience(self):
        return self.__experience

    def get_company1(self):
        return self.__company1

    def get_position1(self):
        return self.__position1

    def get_company2(self):
        return self.__company2

    def get_position2(self):
        return self.__position2

    def get_date(self):
        return self.__date

    def get_pastemployment(self):
        display = "Company: {} | Position: {} \n\nCompany: {} | Position: {}".format(self.__company1, self.__position1,
                                                                                     self.__company2, self.__position2)
        return display


def display_info(person):
    print("Name: {}".format(person.name))
    print("NRIC: {}".format(person.nric))
    print("Email: {}".format(person.email))
    print("Age: {}".format(person.age))
    print("Address {}".format(person.address))
    print("Gender: {}".format(person.get_gender()))
    print("Phone Number: {}".format(person.get_phonenumber()))
    print("Qualification: {}".format(person.get_qualification()))
    print("Experience: {}".format(person.get_experience()))
    print("Past Employment: {}".format(person.get_pastemploymentlist()))




"""
p1 = Applicant("first_name", "last_name", 'nric', 'email', 'age', 'address', 'gender', 'nationality', 'language',
               'phonenumber',
               'qualification',
               'experience', 'company1',
               'position1', 'company2', 'position2', 'empty')
"""



