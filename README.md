# ToDo API

**Python - 3.10**\
**Flask - 2.2**\
**Flask-SQLAlchemy==3.0.3**

## Steps to Run the Application
____
1. Clone the project
2. Move to the project directory:
    ```
        $ cd todolist_backend_assignment/
    ```
3. Build the docker image:
    ```
        $ docker-compose build
    ```
4. Once the image is built, start the container:
    ```
        $ docker-compose up -d
    ```
5. Navigate to [https://localhost:5000](https://localhost:5000)

## API Endpoints
___

### Get All Tasks (GET)
- `https://localhost:5000`
- `https://localhost:5000/tasks`

### Get Task By ID (GET)
- `https://localhost:5000/tasks/{id}`

### Create New Task (POST)
- `https://localhost:5000/`

### Update a Task By ID (PUT)
- `https://localhost:5000/tasks/update/{id}`

### Delete a Task By ID (DELETE)
- `https://localhost:5000/tasks/delete/{id}`

### Get Task By Completion Status (GET)  
- `https://localhost:5000/tasks/status/{status}`

### Update Task Status By ID (PUT)
- `https://localhost:5000/tasks/status/update/{id}`

