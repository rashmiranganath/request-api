import requests
import json
import os


course_url = "http://saral.navgurukul.org/api/courses"


def request(url):
        response = requests.get(url)
        with open("coursesData.json","w") as file:
                file.write(response.content)
        return response.json()
#print(request(course_url))


def read_file(f_read):
        with open("coursesData.json","r") as file:
                data_read = file.read()
                # print data_read
                data_load = json.loads(data_read)
                # print data_load
        return(data_load)
#print(read_file())


coursesIdList = []
def saral_courses(data_load):
        index = 0
        while index < (len(data_load['availableCourses'])):
                courses = data_load['availableCourses'][index]
                courses_name = courses['name']
                coursesId = courses['id']
                coursesIdList.append(coursesId)
                print index+1,"*",courses_name,coursesId
                index = index + 1
        return coursesId
#saral_courses()


def file_courses_fun():
        if os.path.exists("coursesData.json"):
                data_load = read_file("coursesData.json")
                saral_courses(data_load)
                print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        else:
                request(course_url)
                data_load = read_file("coursesData.json")
                saral_courses(data_load)
                print "########################################"
file_courses_fun()


user_exercises = int(raw_input("enter your id"))
select_courses = coursesIdList[user_exercises - 1]
# print select_courses
exercise_url = course_url+"/"+str(select_courses)+"/exercises"
# print exercise_url
def exercises(user_id):
        # print user_id
        exercise_data = requests.get(user_id)
        #print (exercise_data)
        with open("exercises_"+str(select_courses)+".json","w") as file:
                file.write(exercise_data.content)
        exercise_response = exercise_data.json()
        #print (exercise_response)
        return (exercise_response)
exercises_name = exercises(exercise_url)
# print exercises_name


def exercise_read(f_read):
        with open("exercises_"+str(select_courses)+".json","r") as file:
                data_read = file.read()
                # print data_read
                data_load_new = json.loads(data_read)
                # print data_load
        return(data_load_new)

child_excercise_list = []
def exercise_name_func(data_1):
        print data_1
        #child_excercise_list=[]
        i = 0
        while i < len((data_1["data"])):
                # print data_1
                course_exercise = data_1["data"][i]["name"]
                child_ex_data= data_1["data"][i]
                child_ex = child_ex_data["childExercises"]
                child_excercise_list.append(child_ex)
                print i+1, "*",course_exercise
                i = i + 1
        # print child_excercise_list
        print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        user_child = input("enter the childexcercise")
        child_excercise_user = child_excercise_list[user_child-1]
        #print child_excercise_user
        i = 0
        while i < len(child_excercise_user):
                child_id=child_excercise_user[i]["name"]
                print i+1,child_id
                i=i+1
# exercise_name(data_load_new)

if os.path.exists("exercises_"+str(select_courses)+".json"):
        data_load = exercise_read("exercises_"+str(select_courses)+".json")
        exercise_name_func(data_load)
        print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
else:
        exercises(exercise_url)
        data_load = exercise_read("exercises_"+str(select_courses)+".json")
        exercise_name_func(data_load)
        print "########################################"


