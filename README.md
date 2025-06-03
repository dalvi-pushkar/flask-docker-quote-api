# 🧠 Motivational Quote API Using (Flask + Docker)

A simple, inspirational REST API built using Python Flask and containerized with Docker.  
This API serves a random motivational quote every time you hit the `/quote` endpoint.

---

## 🚀 Features

- 🔥 Get a new quote every request  
- 🐳 Dockerized — run anywhere, easily  
- ⚡ Lightweight and fast

---

## 🛠️ Tech Stack

- Python 3.11  
- Flask  
- Docker  

---

## 📦 How to Run with Docker

### 1. Clone this repo

```bash
git clone https://github.com/dalvi-pushkar/flask-docker-quote-api.git
cd flask-docker-quote-api
````

### 2. Build the Docker image

```bash
docker build -t quote-api .
```

### 3. Run the container

```bash
docker run -d -p 5000:5000 quote-api
```

### 4. Open in your browser:

[http://localhost:5000/quote](http://localhost:5000/quote)

---

## 📤 Sample Response

```json
{
  "quote": "It's not who I am underneath, but what I do that defines me."
}
```

---

## 🙌 Author

Made with ☕ by Dalvi Pushkar
