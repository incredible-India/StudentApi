#validating the userinformation at server side this function will validate the user
def validateStudentInfo(name,age,gender,marks,sid):
    if(len(name.strip()) == 0 or len(name) < 2):
        return {'status': False, 'message': "Name should be grater than 3 chars"}
    elif (marks == "" or int(marks) <=0):
        return {'status': False, 'message': "Marks cannot be blank negative or blank"}
    elif int(age) <= 0 :
        return {'status': False, 'message': "Age Cannot be Negative or negative"}
    elif sid == "" or len(sid.strip()) <= 0:
        return {'status': False, 'message': "Id cannot be blank"}
    else:
        return {'status': True, 'message': "Student Added Successfully"}
        
        
        