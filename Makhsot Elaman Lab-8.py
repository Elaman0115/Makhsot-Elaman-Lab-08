import requests

class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

# Task 1.1: GET Request
post_id = 1
url = f'https://jsonplaceholder.typicode.com/todos/{post_id}'
response = requests.get(url)

print("1.1 GET Request:")
if response.status_code >= 400:
    print(f"Error: {response.status_code}")
else:
    print("Response Content:")
    print(response.json())

# Task 1.2: Create a class "ToDo"
# Task 1.3: Create a new object of class ToDo
new_todo = ToDo(userId=1, id=1, title="Example Todo", completed=False)

# Task 1.4: POST Request
new_todo_dict = {
    "userId": new_todo.userId,
    "title": new_todo.title,
    "completed": new_todo.completed
}

post_response = requests.post('https://jsonplaceholder.typicode.com/todos', json=new_todo_dict)

print("\n1.4 POST Request:")
if post_response.status_code >= 400:
    print(f"Error: {post_response.status_code}")
else:
    print("Response Content:")
    print(post_response.json())

# Task 1.5: Edit some data of your attributes of your todo item
new_todo.title = "Updated Todo"
new_todo.completed = True

# Task 1.6: PUT Request
put_url = f'https://jsonplaceholder.typicode.com/todos/{new_todo.id}'
put_response = requests.put(put_url, json=new_todo_dict)

print("\n1.6 PUT Request:")
if put_response.status_code >= 400:
    print(f"Error: {put_response.status_code}")
else:
    print("Response Content:")
    print(put_response.json())
