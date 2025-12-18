# Setup

Deploy FastApi 0.88.0 on Vercel with Serverless Functions using the Python Runtime.

To auto generate requirements.txt:

```
uv pip compile pyproject.toml -o requirements.txt
```

it's configed in `vercel.json`

# To Run

With uvicorn

```
uv venv
uv pip install -r requirements.txt
unset UV_DEFAULT_INDEX
uv run uvicorn main:app --host 0.0.0.0 --port 8012
```

With Docker Compose

```
docker-compose up
```

With Docker

```
# Build the Docker image
docker build -t deploy-python-fastapi-in-vercel .

# Run the Docker container
docker run -p 8000:8000 deploy-python-fastapi-in-vercel
```

# To Test

```
uv add --dev pytest
uv add --dev pytest-asyncio
uv run pytest
```
