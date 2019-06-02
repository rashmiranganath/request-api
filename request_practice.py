import requests
import json


saral_url = "http://saral.navgurukul.org/api/courses"
saral_url_data = requests.get(saral_url)
#print saral_url_data.json()

response = saral_url_data.json()
def displayCourses(available_courses):
        i = 0
        while i < len((available_courses["availableCourses"])):
                course = available_courses["availableCourses"][i]["name"]
                print i+1, course
                i = i + 1
        return course
dc=displayCourses(response)


def collect_CourseIds(course_id):   
        i = 0
        while i < len((course_id["availableCourses"])):
                id=course_id["availableCourses"][i]["id"]
                #print i+1,id
                i = i + 1
                return id
collect_CourseIds(response)



def exercises(exercise_user_id):
        exercise_url = saral_url+"/"+str(exercise_user_id)+"/exercises"
        # print exercise_url
        exercise_url_data = requests.get(exercise_url)
        exercise_data=exercise_url_data.json()
        # print exercise_data
        return exercise_data
user_exercises = input("enter your id")
exercises_name = exercises(user_exercises)
# print exercises_name

def exercise(parent_exercise):
        i = 0
        while i < len((parent_exercise["data"])):
                course_exercise = parent_exercise["data"][i]["name"]
                print i+1, course_exercise
                i = i + 1
        return course_exercise
course_data = exercise(exercises_name)
#print course_data


def child_exercise(child):
        #print child
        child_exercise_list=[]
        i = 0
        while i < len((child["data"])):
                child_exercise_data = child["data"][i]
                child_ex=child_exercise_data["childExercises"]
                child_exercise_list.append(child_ex)
                i=i+1
                #print child_exercise_list
        return child_exercise_list
child_exercise1 = child_exercise(exercises_name)

def user_child_exercise(childex,user_child_ex):
        child_ex_data = childex[user_child_ex-1]
        #print child_ex_data
        i = 0
        while i < len((child_ex_data))-1:
                data_child=child_ex_data[i]["name"]
                i = i + 1
                print data_child
        return child_ex_data
user_child_ex = input("enter the childexercise")
ex_child = user_child_exercise(child_exercise1,user_child_ex)
#print ex_child

def slug_info(slug_data,user_slug):
        #print slug_data                                                                                          
        slug_list=[]
        i=0
        while i<len(slug_data):
                slug_storage = slug_data[i]["slug"]
                slug_list.append(slug_storage)
                i = i + 1
        print slug_list
        return slug_list
user_child_slug=input("enter the slug")
slug_variable=slug_info(ex_child,user_child_slug)
# print slug_variable

def id_info(id_data,user_data):
        #print id_data
        id_list = []
        i=0
        while i < len(id_data):
                id_storage = id_data[i]["id"]
                id_list.append(id_storage)
                i = i +1
        #print id_list
        return id_list
user_child_id = input("enter the id")
id_variable = id_info(ex_child,user_child_id)

def slug(slug_new,user_content):
        #print slug_new
        slug_1 = slug_new[user_content-1]
        slug_id = id_variable[user_content-1]

        slug_url = "http://saral.navgurukul.org/api/courses/" +str(slug_id)+"/exercise/getBySlug?slug="+(slug_1)
        print slug_url
        slug_data = requests.get(slug_url)
        # print slug_data.text

        slug_content = slug_data.json()
        content = slug_content["content"]
        print content
        return content
slug_user_content = input ("enter the slug")
slug_new1 = slug(slug_variable,slug_user_content)
# print slug_new1

def up(up_1,up_data):
        print up_data
        if up_1 == "up":
                return displayCourses(response)
                
up_1 = str(raw_input("enter up if u want to:"))
up_variable = up(up_1,dc)

 

def next_slug(slug_new,user_content):
        #print slug_new
        slug_1 = slug_new[user_content-1]
        slug_id = id_variable[user_content-1]

        slug_url = "http://saral.navgurukul.org/api/courses/" +str(slug_id)+"/exercise/getBySlug?slug="+(slug_1+1)
        print slug_url
        slug_data = requests.get(slug_url)
        # print slug_data.text

        slug_content = slug_data.json()
        content = slug_content["content"]
        print content
        return content
slug_user_content = input ("enter the slug")
new1 = slug(slug_variable,slug_user_content)
# print new1:
         

def previous_slug(slug_new,user_content):
        #print slug_new
        slug_1 = slug_new[user_content-1]
        slug_id = id_variable[user_content-1]

        slug_url = "http://saral.navgurukul.org/api/courses/" +str(slug_id)+"/exercise/getBySlug?slug="+(slug_1-1)
        print slug_url
        slug_data = requests.get(slug_url)
        # print slug_data.text

        slug_content = slug_data.json()
        content = slug_content["content"]
        print content
        return content
slug_user_content = input ("enter the slug")
new2 = slug(slug_variable,slug_user_content)
# print slug_new1

while True:
        user_next_previous = str(raw_input("enter n if next or enter p for previous or e for exit"))
        if user_next_previous == "n":
                next_slug(slug_new,user_content)
        elif user_next_previous == "p":
                previous_slug(slug_new,user_content)
        elif user_next_previous == "e":
                print "exit"
                break


 













 












