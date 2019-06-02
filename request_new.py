import requests
import json


saral_url = "http://saral.navgurukul.org/api"
print(saral_url)

def course(link):
    respones = requests.get(link)
    ret = respones.json()
    return ret
    # print (ret)
course(saral_url)

course_url = saral_url+"/"+"courses" 
full_courses = course(course_url)
# print (full_courses)  

course_list = []
def courses_func():
    index = 0
    while index < len(full_courses["availableCourses"]):
        courses_ex = full_courses["availableCourses"][index]
        courses_name = courses_ex["name"]
        courses_id = courses_ex["id"]
        course_list.append(courses_id)
        print str(index)+"",courses_name,courses_id
        index= index +1
courses_func() 

print ("%%%%%%%%%%%%%%%%%%%%%welcome to saral%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
user = int(raw_input("enter your exercise?")) 
user_id = course_list[user-1]

print (user_id)   
print ("%%%%%%%%%%%%%choose your exercise%%%%%%%%%%%%%%%%%%%%%%%")

exercise_url = course_url+"/"+str(user_id)+"/"+'exercises'
exercise_url_1 = course_url+"/"+str(user_id)+"/"+'exercise'
print (exercise_url)
exercise=course(exercise_url)
sub_exercises = []
slug_list =[]

def exercise_func():
    index1 = 0
    while index1 < len(exercise["data"]):
        data_ex = exercise["data"][index1]
        all_exercise = data_ex["parentExerciseId"]
        child_ex = data_ex["childExercises"]
        exercise_id = data_ex["id"]
        sub_exercises.append(child_ex)
        if all_exercise != []:
            exercise_name = data_ex["name"]
            exercise_slug = data_ex["slug"]

            slug_list.append(exercise_slug)    
            print str(index1)+ "",  exercise_name      
            
        index1= index1+1
exercise_func()

print ("%%%%%%%%%%%%%choose your exercise%%%%%%%%%%%%%%%%%%%%%%%")

user1 = int(input("enter your lesson?:-"))
use_ex=slug_list[user1]
all_exercise = slug_list[user1]
print (use_ex)
slug_url = exercise_url_1+"/"+"getBySlug?slug="+str(use_ex)
slug_url_1 = exercise_url_1+"/"+"getBySlug?slug="
print (slug_url)
content = course(slug_url)
content_name = content["content"]
print (content_name)

print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

slug_list1 = []
sub_name = []
def child_func():
    if all_exercise != None:
        if sub_exercises[user1] != []:
            index2 = 0
            while index2 < len(sub_exercises[user1]):
                child_sub_ex = sub_exercises[user1][index2]
                sub_ex_name = child_sub_ex["name"]
                sub_name.append(sub_ex_name)
                sub_ex_slug = child_sub_ex["slug"]
                slug_list1.append(sub_ex_slug)
                print str(index2)+ sub_ex_name
                index2= index2+1
            
child_func() 

print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

user2 = int(raw_input("enter your number"))
sub_content = slug_list1[user2]
content_url = slug_url_1 +str(sub_content)
print(content_url)
content2 = course(content_url)
content_name1 = content2["content"]
print (content_name1) 

print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

def Next_func():
    user_1 = int(input("enter your id"))
    var_1 = slug_list1[user_1]
    url =  slug_url_1 +str(var_1 )
    url_call = course(url)
    content_Next = url_call["content"]
    print (content_Next)


def Previous_func():
        user_2 = int(input("enter your id"))
        var_2 = slug_list1[user_2-1]
        url_1 = slug_url_1 +str(var_2)
        url_call1 = course(url_1)
        content_previous = url_call1['content']
        print (content_previous)



while True:
    user_5 = raw_input("enter your 'n'or 'p'")
    if user_5 == 'n':
            Next_func()
    elif user_5 == 'p':
            Previous_func()
    elif user_5 == 'e':
            print ("exit")
            break