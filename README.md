# Initialization
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. MatchHub.proto
```

# Dockerization

```bash
docker-compose up --build -d
```

# Simple Test
In one terminal:
```bash
docker-compose up -d
```

In the other terminal:
```bash
python client.py
```
