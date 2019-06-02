import requests
import json
import os

base_url = "http://saral.navgurukul.org/api/courses" 

def request_write(url):
    url_data = requests.get(url)
    with open("cashing_data.json","w") as fs:
        fs.write(url_data.text)
    return url_data.json()
#write = request_write(base_url)

def request_read(url_data):
    with open("cashing_data.json","r") as fs:
        read = fs.read()
        read_data = json.loads(read)
    return read_data
#read_new = request_read(write)

course_id_list = []
def saral_courses(read_data):
        index = 0
        while index < (len(read_data['availableCourses'])):
                courses = read_data['availableCourses'][index]
                courses_name = courses['name']
                courses_id = courses['id']
                course_id_list.append(courses['id'])
                print index+1,courses_name,courses_id
                index = index + 1
        return course_id_list



if os.path.exists("cashing_data.json"):
    data_load = request_read("cashing_data.json")
    saral_courses(data_load)
    # print "hijhik"
else:
    requests.get(base_url)
    data_load = request_read("cashing_data.json")
    saral_courses(data_load)
    # print "h*******************************8"

user_exercise = input("enter you")
user_ex = course_id_list[user_exercise - 1]
#print user_ex

exercise_url = base_url+"/"+str(user_ex)+"/exercises"
#print exercise_url

def exercise_write(exercise_url):
    ex_url_data = requests.get(exercise_url)
    print ex_url_data
    with open("exercise"+str(user_ex)+".json","w") as fs:
        fs.write(ex_url_data.text)
    return ex_url_data.json()
# get_data = exercise_write(exercise_url)
#print get_data

def exercise_read(ex_url_data):
    with open("exercise"+str(user_ex)+".json","r") as fs:
        read_ex = fs.read()
        read_data_ex = json.loads(read_ex)
    return read_data_ex
# read_call = exercise_read(get_data)

def exercises(read_data_ex):
    # print read_data_ex
    index = 0
    while index < (len(read_data_ex['data'])):
        exercise = read_data_ex['data'][index]
        ex_name = exercise['name']
        print index+1,ex_name
        index = index+1
    return ex_name
# exercises(read_call)

if os.path.exists( "exercise_"+str(user_ex)+".json"):
    data_load_new = exercise_read("exercise_"+str(user_ex)+".json")
    exercises(data_load_new)
    print "hijhik"
else:
    requests.get(base_url)
    data_load_new = exercise_read("exercise_"+str(user_ex)+".json")
    exercises(data_load_new)
    print "h*******************************8"

    





        