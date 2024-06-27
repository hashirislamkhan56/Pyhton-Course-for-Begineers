course = 'Pyhton for "Beginners"'
print(course)
course = '''
Dear Hash,

I hope you are doing well. I am writing this email to you.
Thank you
'''
print(course)

course_py = 'Python for Beginners'
#            0123456789
print(course_py[0:6])

course_py = 'Python for Beginners'
#            0123456789
print(course_py[0:4])
course_py = 'Python for Beginners'
#            0123456789
print(course_py[:4])

course_py = 'Python for Beginners'
#            0123456789
print(course_py[0:])

course_py = 'Python for Beginners'
#            0123456789
another = course_py[:]
print(course_py[:])


name = 'jennifer'
#       01234567
print(name[0:-2])

#Formatted Strings
first  = 'Hashir'
last = 'Islam'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder   '
print(message)
print(msg)

#String Method
course_lenght = ('Python for Beginners, '
                 'and i am learning Python. ')
print(len(course_lenght))
print(course_lenght.upper())
print(course_lenght)
print(course_lenght.lower())
print(course_lenght.find('learning'))
print(course_lenght.replace("Beginners","Absolurte Beginner"))
print(course_lenght.replace("P","J"))
print('Python' in course_lenght, 'Learning' in course_lenght)