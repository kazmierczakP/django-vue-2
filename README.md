# django-vue_e-note

## Usage

### frontend

```cd frontend```

```npm run serve```

### backend

```cd backend```

```python manage.py runserver```

### endpoints:

```http://127.0.0.1:8000/api/students/```

```http://localhost:8080/```

example post call:

{
    "StudName": "test",
    "Course": "resdy",
    "Rating": 123
}

### contenerization

```cd backend```

```docker build -t backend_image .```

```docker run --name backend_container -p 8000:8000 -it backend_image```

## Vue

### instalation

```npm install -g @vue/cli```

### create project

```vue create my-project```

```cd my-project```

```npm run serve```

Ctrl+space to autocomplete code

## Django

### instalation

```pip install django```

```pip install djangorestframework```


### create project

```django-admin startproject```

```python manage.py startapp appname```

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py runserver```


### Side notes:

To make requirements.txt use:

```pip list --format=freeze > requirements2.txt ```

Requirements containt ony 3 packages for the purpose of building image.