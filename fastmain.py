from fastapi import FastAPI , status , HTTPException,Request,Depends,Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel
app= FastAPI()


# home page
# @app.get("/")
# def home ():
#     return {"Message":"Hy this is virtual enviroment"}

# # about page
# @app.get("/about")
# def about():
#     return {"Message":" this is about page"}


# # user page
# @app.get("/user")
# def user():
#     return {
#         "user":["ahsan","asad"]
#     }


# @app.get("/user/{user_id}")
# def user(user_id:str):
#     return {"user": user_id}





# # optional parameter
# @app.get("/user")
# def user(name : str=None):
#     return{"name":name}

# default parameter
# @app.get("/myself")
# def user(limit : str="ahsan"):
#     return{"default":limit}

# multiple Query parameter
# @app.get("/skill")
# def user(one : str="python developer",two : str="software engineer + ai engineer"):
#     return{
#         "skill name":one,
#         "sill name 2":two
#         }



# post api 
# @app.post("/register")
# def create(name:str,age:int):
#     return{
#         "name":name,
#         "age":age
#     }


'Pyandatic' 

# class user(BaseModel):
#     name:str
#     age:int
#     email:str

# # @app.post("/register")
# # def create(user:user):
# #     return{
# #         "message":"User data",
# #         "data":user
# #     }


# @app.post("/create")
# def create(User:user):
#     return{
#         "message":"user created...",
#         "data":User
#     }



'Nested Models'
# class address(BaseModel):
#     city:str
#     postcode:int

# class user(BaseModel):
#     name:str
#     age:int
#     Address:address

# @app.post("/data_user")
# def data(User:user):
#     return{
#         "Message":"user data",
#         "data":User

#     }


# todos=[]

# class todo(BaseModel):
#     id:int
#     title:str
#     completed:bool

# @app.post("/todos")
# def creted_todo(Todo:todo):
#     todos.append(Todo)
#     return{
#         "message":"Todo added",
#         "data":Todo
#     }

# @app.get("/todos")
# def craeted():
#     return todos


# @app.get("/todos/{id}")
# def id(id:int):
#     for Todo in todos:
#         if Todo.id == id :
#             return Todo
#     return {"not found"}



# @app.put("/todos/{id}")
# def update(id:int , updated_todo:todo):
#     for index,Todo in enumerate(todos):
#         if Todo.id == id :
#             todos[index] = updated_todo
#             return {
#                 "message":"todo updated..",
#                 "data": updated_todo
#             }
#     return {"not found"}


# @app.delete("/todos/{id}")
# def delete(id:int):
#     for index,Todo in enumerate(todos):
#         if Todo.id == id:
#             todos.pop(index)
#             return{"message":" data deleted"}
#     return {"not found"}



# users = []
# class User (BaseModel):
#     name:str
#     age:int

# @app.post("/user")
# def c_user(user:User):
#     users.append(user)
#     return{
#         "message":"created...",
#         "data": user
#     }

# @app.put("/users/{user_id}")
# def updtad (user_id:int, user:User,notify:bool = False ):
#     if user_id < len(users):
#         users[user_id]=user
#         return {
#             "message":"user updated",
#             "notify": notify,
#             "data":user
#         }
#     return{
#         "messgae":"hy"
#     }



'''   Response Models  '''
#  client ko kiya dikhana ha or kia nhi dikhana hide sensitive data , and return need data to client 

# class reponse(BaseModel):
#     name:str
#     age:int
#     password:str

# class Response_model(BaseModel):
#     name:str
#     age:int

# @app.get("/user", response_model=Response_model)
# def users():
#     return{
#         "name":"ahsan",
#         "age":17,
#         "password":"2345677"

#     }



'''  status code and response  '''

# @app.post("/create_user",status_code=status.HTTP_201_CREATED)
# def create_user():
#     return {
#         "message":"User craeted"
#     }


'''  custom reponse'''

# @app.get("/user")
# def user_create():
#     return {
#         "Status":"Success",
#         "message":"user created",
#         "Data":{
#             "name":"ahsan",
#             "age":17
#         }
#        }


# @app.get("/user/{user_id}")
# def get_id(user_id:int):
#     if user_id != 1 :
#        raise HTTPException(
#            status_code=400,
#            detail="User not found"
#        )
#     return {
#         "id":1,
#         "name":"ahsan"
#     }
    



'''    Exception handling   '''

# @app.get("/user/{id}")
# def users (id:int):
#     if id != 1:
#         raise HTTPException(
#             status_code=404,
#             detail="user not found"
#         )
#     return{
#         "id":1,
#         "name":"Ahsan"
#     }



class Usernotfound(Exception):
    def __init__(self, name:str):
        self.name=name

#  GLobal + Exceptional error handling 

# @app.exception_handler(Usernotfound)
# def User_not_found(request:Request ,exc:Usernotfound):
#     return JSONResponse(
#         status_code=404,
#         content={
#             "status":"Error",
#             "message":f"User {exc.name} not found"
#         }
#     )
    

# @app.get("/users/{name}")
# def get_user(name:str):
#     if name != "ahsan":
#         raise Usernotfound(name)
#     return{
#         "name":name
    # }

'''  Dependency injection  '''
# Dependency Injection is a technique used to execute common logic automatically within your functions


# def logic ():
#     return{
#         "Message":"Depends logic work"
#     }

# @app.get("/home")
# def home (data= Depends(logic)):
#     return data



# def employes():
#     return {
#         "Name":"Ahsan ( Ai Engineer )"
#     }

# @app.get ("/Employe")
# def Employe (data=Depends(employes)):
#     return data

# @app.get ("/dashboad")
# def dashbaord (dash=Depends(employes)):
#     return dash


def auth (token:str = Header(None)):
    if token != "Ahsan":
        raise HTTPException(
            status_code=401,
            detail="unthorized"
        )
    return{
        "User":" Secure Authorized User"
    }
@app.get ("/secure_data")
def secure(security=Depends(auth)):
    return{
        "Message":"User accessed",
        "user":security
    }