# AlgoWorksTask

1- SignUp: URL: http://127.0.0.1:8000/todoApp/user_signup_view/
Method - Post
Param = { "email":"user@gmail.com", "mobileNumber":7858588481, "username":"user1", "password":"user" }

2- Login: URL: http://127.0.0.1:8000/todoApp/user_login_view/
  Method: POST
  Body Param: { "email":"user@gmail.com", "password":"user" }

3- Add Todo: URL: http://127.0.0.1:8000/todoApp/add_todo/ 
Method: POST
Body Param: { "name":"test2", "end_date":"12-11-2022" }

4- Edit Todo: URL: http://127.0.0.1:8000/todoApp/edit-todo/?id=1
Method: PUT Query Param: { "id":1 }
Body Param: { "name":"test2", "end_date":"12-11-2022" }

5- Delete Todo: URL: http://127.0.0.1:8000/todoApp/delete-todo/?id=1
Method: Delete Query Param: { "id":1 }

Currently i have taken default pagination of DRf, And set the pagination number to 10, So no need to pass pagination parameters in url 
6- List of Todo: URL: http://127.0.0.1:8000/todoApp/todo_list/ Method: GET

Admin can see all the ToDO's list (Set as per page only 10 todo's list)  
7- Admin List of Todo: URL: http://127.0.0.1:8000/todoApp/admin_todo_list/ Method: GET

8- Add comment: URL: http://127.0.0.1:8000/todoApp/add_comment/?id=1
Method: POST 
Body Param:{ "comment":"this is my first comment" } Query Param: { "id":q # where id is todo's primary key }

9- Add Reply: URL: http://127.0.0.1:8000/todoApp/add_reply/?id=1 
Method: POST 
Body Param:{ "reply":"this is my first reply" } Query Param: { "id":1 # where id is comment's primary key }
