# Learn Docker From Apna College 🚢  

Welcome to the **Learn Docker From Apna College** repository! This repository contains notes, code snippets, and hands-on exercises to help you learn **Docker** from scratch, focusing on deploying a **Django application** inside a Docker container.  

---

## 📌 What is Docker?  
Docker is an **open-source platform** that allows developers to **build, ship, and run** applications in **containers**. Containers are lightweight, portable, and ensure that applications work the same way across different environments.  

---

## 🚀 Why Use Docker?  
✅ **Portability** – Works across different OS and machines  
✅ **Lightweight** – Uses fewer resources than virtual machines  
✅ **Fast Deployment** – Quickly start, stop, and scale applications  
✅ **Consistency** – Ensures the same environment for development, testing, and production  
✅ **Microservices-Friendly** – Works well with modern architectures  

---

## 📂 Folder Structure  
```
/  
├── django_project/       # Django project folder  
│   ├── manage.py  
│   ├── django_app/       # Django app  
│   ├── settings.py       # Django settings  
│   ├── urls.py           # URL configurations  
│   └── views.py          # Views  
├── Dockerfile            # Dockerfile for Django  
├── docker-compose.yml    # Docker Compose file  
├── requirements.txt      # Python dependencies  
└── README.md             # This documentation  
```  

---

## 🛠️ Installing Docker  

### **Step 1: Install Docker**  
Download and install **Docker Desktop** based on your OS:  
🔹 [Windows](https://docs.docker.com/desktop/install/windows-install/)  
🔹 [Mac](https://docs.docker.com/desktop/install/mac-install/)  
🔹 [Linux](https://docs.docker.com/engine/install/)  

### **Step 2: Verify Installation**  
Run the following command in your terminal:  
```bash
docker --version
```
If Docker is installed correctly, you will see a version number.  

### **Step 3: Run Your First Docker Container**  
Test Docker installation by running:  
```bash
docker run hello-world
```
This will pull and run the `hello-world` container, confirming Docker is working correctly.  

---

## 📝 Writing a Dockerfile for Django  

A **Dockerfile** is a script that contains instructions to create a Docker image.  

### **1️⃣ Create a `Dockerfile`**  
```Dockerfile
# Use an official Python image
FROM python:3.9  

# Set the working directory
WORKDIR /app  

# Copy requirements file and install dependencies
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy the Django project files
COPY . .  

# Expose the application port
EXPOSE 8000  

# Run Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### **2️⃣ Create `requirements.txt`**  
Add the required dependencies in a file named `requirements.txt`:  
```
Django>=3.2
gunicorn
```

### **3️⃣ Build the Docker Image**  
```bash
docker build -t django-app .
```

### **4️⃣ Run the Container**  
```bash
docker run -p 8000:8000 django-app
```
- The **Django app** will now be accessible at **http://localhost:8000**.  

---

## 🔗 Using Docker Compose for Django & PostgreSQL  

**Docker Compose** allows you to define and run **multi-container applications**. Let's create a **Django + PostgreSQL** setup.  

### **1️⃣ Create `docker-compose.yml`**  
```yaml
version: '3'

services:
  db:
    image: postgres
    restart: always
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web:
    build: .
    depends_on:
      - db
    ports:
      - "8000:8000"
    environment:
      - DEBUG=True
      - DATABASE_URL=postgres://myuser:mypassword@db:5432/mydb
    volumes:
      - .:/app

volumes:
  postgres_data:
```

### **2️⃣ Run with Compose**  
```bash
docker-compose up -d
```
- `-d` → Runs in **detached mode**  
- The **Django app** will connect to the PostgreSQL database inside a container.  

---

## 🐳 Basic Docker Commands  

| Command | Description |
|---------|-------------|
| `docker --version` | Check installed Docker version |
| `docker pull <image>` | Download a Docker image from Docker Hub |
| `docker images` | List all downloaded images |
| `docker run <image>` | Run a container from an image |
| `docker ps` | Show running containers |
| `docker ps -a` | Show all containers (running & stopped) |
| `docker stop <container_id>` | Stop a running container |
| `docker rm <container_id>` | Remove a container |
| `docker rmi <image_id>` | Remove an image |
| `docker logs <container_id>` | View container logs |

---

## 📦 Docker Volumes (Persistent Data)  

Docker containers are **ephemeral** (temporary). Data is lost when a container is removed. **Volumes** solve this issue by persisting data.  

### **Create a Volume**  
```bash
docker volume create my_volume
```

### **Use a Volume in a Container**  
```bash
docker run -v my_volume:/app/data ubuntu
```
This mounts `my_volume` inside the container at `/app/data`.  

---

## 🚀 Deploying Django with Docker  

### **1. Push an Image to Docker Hub**  
```bash
docker tag django-app username/django-app  
docker push username/django-app
```

### **2. Run on Another Machine**  
```bash
docker pull username/django-app  
docker run -d -p 8000:8000 username/django-app
```

---

## 🤝 Contributing  

Feel free to contribute by adding more examples, fixing issues, or improving documentation!  

---

## 📜 License  

This project is for **learning purposes**. Feel free to use and modify it!  

---

## 🌟 Resources & Further Learning  

📖 [Official Docker Docs](https://docs.docker.com/)  
📖 [Docker Hub](https://hub.docker.com/)  
📖 [Docker Cheat Sheet](https://github.com/wsargent/docker-cheat-sheet)  
📖 [Django + Docker Docs](https://docs.docker.com/samples/django/)  

