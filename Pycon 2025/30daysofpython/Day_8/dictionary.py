#empty dictionary
dog= {}

#adding informations
dog= {
    'name' : 'Max', 
    'Color': 'Black', 
    'breeds' : 'German Sherpherd', 
    'legs' : 'left and right', 
    'age' : 2
    
}

#student dictionnary
student= {
    'first_name' : 'Cedric',
    'last_name': 'AMOUZOU-ABLO',
    'gender': 'Male',
    'age': 19,
    'marital_status': 'Single',
    'country': 'TOGO',
    'skills': ['Designer', 'Web Developement', 'Digital Marketing', 'Figma', 'WordPress'],
    'city': 'Lome',
    'address': 'Somewhere'
   
}

#length of student dictionary
print("Length of students dictionary: ", len(student), "\n")

#Skills values
print("The skills values: ", student['skills'], "\n")
print("The data type of skills is ", type(student['skills']), "\n")

#modifing of skills values
student['skills'].append(['HTML', 'CSS', 'Javascript'])

#Getting of dictionary keys
print("The student dictionary keys are: ", student.keys(), "\n")

#Getting of dictionary values
print("The student dictionary values are: ", student.values(), "\n")

#changing the student dictionary to list of tuples
student_list= student.items()
print("List of tuple from student dictionary: ", student_list, "\n")

#Deleting one of item in dictionary
student.popitem()

#Deleting of the dog dictionary
del dog







