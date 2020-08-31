import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client.employee_data

def insert():
    emp_id = input('Enter the employee id:')
    emp_name = input('Enter the employee name:')
    emp_age = input('Enter the employee age:')
    emp_gender = input('Enter the employee gender:')

    db.emp.insert_one(
        {
            "id" : emp_id,
            "name" : emp_name,
            "age" : emp_age,
            "gender" : emp_gender
        }
    )
    print('\nData inserted!')

def read():
    emp_col = db.emp.find()
    print('The data present in the Employee database is as follows-')
    for emp in emp_col:
        print(emp)

def update():
    id = input('Enter the id to be updated:')
    name = input('Enter the name to be updated:')
    age = input('Enter the age to be updated:')
    gender = input('Enter the gender to be updated:')

    db.emp.update_one(
        { "id" : id },
        {
            "$set" : {
                "name" : name,
                "age" : age,
                "gender" : gender
            }
        }
    )
    print('\nData updated!')

def delete():
    id = input('Enter the id of the employee to be deleted:')
    db.emp.delete_many({ "id":id })
    print('Deleted successfully!')

def search():
    id = input('Enter the employee id whose details are to be searched:')
    result = db.emp.find_one({ "id":id })
    print(result)


if __name__ == "__main__":
    while(1):
        option = input('\n1. Insert\n2. Read\n3. Update\n4. Delete\n5. Search\n6. Exit\nChoose the appropriate option:')
        if option == '1':
            insert()
        elif option == '2':
            read()
        elif option == '3':
            update()
        elif option == '4':
            delete()
        elif option == '5':
            search()
        elif option == '6':
            exit()
        else:
            print('Invalid selection!')