from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
# get all departments stored in the database. Print each on a new line
    # create a variable to store get_all() result    
    departments = Department.get_all() 
    # loop over every department in departments
    for department in departments:
        #and print them
        print(department)   


def find_department_by_name():
    #create variable to print enter name query
    name = input("Enter the department's name: ")
    # create variable to store named department
    department = Department.find_by_name(name)
    #print department if it exists
    print(department) if department else print(
        #else print not found message
        f'Department {name} not found'
    )


def find_department_by_id():
    #create variable to print name query
    id_ = input("Enter Department Id: ")
    #create variable to store found id
    department_id = Department.find_by_id(id_)
    # print department if it exists:
    print(department_id) if department_id else print(
    #else print no id found message
        f'Department {id_} not found'
    )


def create_department():
    # create variable to print prompts for name/location
    name = input("Enter Department name: ")
    location = input("Enter Department location: ")
    #create try/except block in case of exception
    try:
        #try creating department with name/location
        department = Department.create(name, location)
        #print success if successful
        print(f'Success: {department}')
    #create exception for try 
    except Exception as exc:
        #print the exception error
        print("Error creating department: ", exc)



def update_department():
    #create variable for input asking for id
    id_ = input("Enter the department's id: ")
    #check if id exists
    if department := Department.find_by_id(id_):
        #try name/location input
        try:
            name = input("enter the department's new name: ")
            # give department.name a name variable
            department.name = name
            location = input("enter the department's new location: ")
            # give department.location a location variable
            department.location = location

            #run update method
            department.update()
            #print if successful
            print(f'Success: {department}')
        #create exception if error
        except Exception as exc:
            #print err exception
            print("Error updating department: ", exc)
        #print else not found
    else:
        print(f'Department {id_} not found')


def delete_department():
    #prompt for id
    id_ = input("Enter Department Id: ")
    #If Id exists, store it
    if department := Department.find_by_id(id_):
        #delete it
        department.delete()
        #print success
        print(f'Department {id} deleted')
    #else print not found
    else:
        print(f'Department {id_} not found')
    


# You'll implement the employee functions in the lab

def list_employees():
    pass


def find_employee_by_name():
    pass


def find_employee_by_id():
    pass


def create_employee():
    pass


def update_employee():
    pass


def delete_employee():
    pass


def list_department_employees():
    pass