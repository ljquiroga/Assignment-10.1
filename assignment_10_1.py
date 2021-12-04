# Lola Quiroga
# Assignment 10.1 -- Your Own Class

# Acknowledgements: https://www.kite.com/python/answers/how-to-get-a-random-entry-from-a-dictionary-in-python

# My class is called CollegeStudent, which represents a College Student and their
# year of graduation, type of college (public, private), family income level, 
# type of student (in state, out of state, international), their housing status,
# and their mental health status

import time
import random

class CollegeStudent:
    def __init__(self, year, type_college, family_income, type_student, housing_status, mental_health_status):
        self.__year = year
        self.__type_college = type_college
        self.__family_income = family_income
        self.__type_student = type_student
        self.__housing_status = housing_status
        self.__mental_status = mental_health_status
        self.tuition = 0
    def set_tuition(self):
        if self.__type_college == "Private":
            self.tuition += 60000
        elif self.__type_college == "Public":
            self.tuition += 10000
        elif self.__type_college == "UC":
            self.tuition += 35000
        elif self.__type_college == "CSU":
            self.tuition += 12000
        elif self.__type_college == "CC":
            self.tuition += 3000
        else:
            self.tuition += 1000
    def get_tuition(self):
        return self.tuition
    def get_remaining_years(self):
        return(f"You have {4 - int(self.__year)} remaining years left until graduation!")

    def financial_aid(self):
        if self.__family_income == "low" or self.__family_income == "middle":
            print("You qualify for financial aid!")
        else:
            return("You do not qualify for financial aid.")
        if self.__family_income == "low":
            self.tuition -= 25000
            return(f"$25,000 is subtracted from your tuition. Your tuition is now {self.tuition}")
        if self.__family_income == "middle":
            self.tuition -= 10000
            return(f"$10,000 is subtracted from your tuition. Your tuition is now {self.tuition}")

    def increased_tuition(self):
        if((self.__type_student == "international" or self.__type_student == "out of state") and self.tuition != "Private"):
            self.tuition += 10000
    
    def mental_check_in(self):
        self.__therapist_dict = {"Louise": "1122 Univeristy Ave", "Martha": "Zoom Therapist", "Darnell": "Phone call only", "Jaqueline": "8560 Main St.", "Luna": "2255 First Ave."}
        if self.__mental_status == "bad":
            print("Setting you up with a therapist...")
            time.sleep(2)
            self.__l1 = list(self.__therapist_dict.items())
            random_entry = random.choice(self.__l1)
            return(f"Therapist found! It's {random_entry[0]}, {random_entry[1]}")
        elif self.__mental_status == "medium":
            print("Good to hear you aren't doing bad, but it wouldn't hurt to get a therapist so you talk out your problems!")
            time.sleep(1)
            print("Setting you up with therapist...")
            time.sleep(1)
            l1 = list(therapist_dict.items())
            random_entry = random.choice(l1)
            return(f"Therapist found! It's {random_entry[0]}, {random_entry[1]}")
        else:
            print("Good to hear that you are doing good!")
            return None
    def housing_cost(self):
        if self.__housing_status == "on":
            self.__a = input("Are you in a dorm or an apartment? ")
            if self.__a == "dorm":
                self.__b = input("Is it a single, double, triple, quad, or more? ")
                if self.__b == "single":
                    return 6700
                elif self.__b == "double":
                    return 6000
                elif self.__b == "triple":
                    return 5000
                elif self.__b == "quad":
                    return 4000
                else:
                    return 3500
            else:
                self.__c = input("Is it a studio?").title()
                if self.__c == "Yes":
                    return 7000
                else:
                    self.__d = input("Is it a 1 bedroom?").title()
                    if self.__d == "Yes":
                        return 7100
                    else:
                        return 7500
        else:
            return 0
    def total_cost(self):
        self.__h_cost = self.housing_cost()
        return(f"Tuition: ${str(self.tuition + self.__h_cost)}")
def main():
    # DEMO SLAY
    name = input("Hi user! What is your name? ")
    year = input("Hello College Student! What year are you? (1, 2, 3, or 4?): ")
    type_c = input("What type of college are you in? (Public, Private, or CC?): ")
    if type_c == "Public":
        cali_student = input("Is your school in California? (Yes or No?): ")
        if cali_student == "Yes":
            cali_type = input("Is your school a CSU or a UC? ")
            if cali_type == "CSU" or "UC":
                type_c = cali_type
    income = input("What is your family's income level? (Low, middle, or high?): ")
    home = input("Are you in state, out of state, or international? ")
    house = input("Do you live on or off campus? (on or off): ").lower()
    mental = input("How is your mental health? (Good, bad, medium): ").lower()
    user_student = CollegeStudent(year, type_c, income, home, house, mental)
    time.sleep(1.5)
    print(f"Hi, {name}, thank you for all the information. We will now begin assessing.\n")
    time.sleep(1.5)
    print(f"{user_student.get_remaining_years()}\n")
    user_student.set_tuition()
    user_student.increased_tuition() 
    time.sleep(1.5)
    print(f"Your tuition is: {user_student.get_tuition()}.\n")
    time.sleep(1.5)
    print(f"Your financial aid package: {user_student.financial_aid()}\n")
    time.sleep(1.5)
    print(user_student.total_cost())
    print()
    time.sleep(1.5)
    print(f"Mental health status: {mental}, so: ")
    print(user_student.mental_check_in())
    print()
    time.sleep(2)
    print(f"Thanks, {name}, I enjoyed getting to know you. \n\nGOOD LUCK IN COLLEGE!\n")
    # user_student = CollegeStudent(1, "UC", "middle", "in state", "dorm", "bad")
    # user_student.set_tuition()
    # print(user_student.get_tuition())
if __name__ == "__main__":
    main()
