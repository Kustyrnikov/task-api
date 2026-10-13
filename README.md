- Python 3.12
- Flask
- Docker

```text
task-api/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
├── data/
│   └── tasks.json
```

```bash
docker build -t task-api:1.0 .
```

```bash
docker run -d --name task-api-container -p 8080:5000 task-api:1.0
```

```text
http://localhost:8080
```

```bash
curl http://localhost:8080/
curl http://localhost:8080/health
curl http://localhost:8080/api/tasks
curl http://localhost:8080/api/tasks/2
```

```bash
docker exec task-api-container cat /app/data/tasks.json
```

```bash
docker stop task-api-container
docker rm task-api-container
```
