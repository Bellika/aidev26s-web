from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import httpx
from middlewares.request_logger import log_requests

app = FastAPI()

# Add middleware to log all requests
app.middleware("http")(log_requests)


@app.get('/posts')
async def get_posts(limit: int = Query(default=5, description="Number of posts to fetch")):
    """
    Fetches posts from JSONPlaceholder API and returns them as JSON.
    Also prints data to the CLI.
    """
    print(f"Fetching {limit} posts from API...")

    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://jsonplaceholder.typicode.com/posts?_limit={limit}")
        posts = response.json()

    print(f"\nFetched {len(posts)} posts:")
    for i, post in enumerate(posts, 1):
        print(f"\n{i}. {post['title']}")
        print(f"   Body: {post['body'][:50]}...")

    return posts


@app.get('/')
async def home():
    """
    Home endpoint that returns information about the API.
    """
    print("Home endpoint called!")

    return {
        "message": "Welcome to FastAPI introduction!",
        "endpoints": {
            "/": "This page",
            "/posts?limit=5": "Fetch posts from JSONPlaceholder",
            "/methods": "GET endpoint that says Hello",
            "/greeting/{name}": "Personal greeting",
            "/ping": "Health check",
            "/docs": "Interactive API documentation (Swagger)",
            "/redoc": "API documentation (ReDoc)"
        }
    }


@app.get('/methods')
async def hello_get():
    """
    GET endpoint that returns a greeting.
    """
    print("GET /methods called - returning Hello")
    return JSONResponse(content={"message": "Hello"}, status_code=200)


@app.post('/methods')
async def hello_post():
    """
    POST endpoint that returns a farewell message.
    """
    print("POST /methods called - returning Goodbye")
    return JSONResponse(content={"message": "Goodbye"}, status_code=500)


@app.get('/greeting/{name}')
async def greeting(name: str):
    """
    Path parameter example - greets the user by name.
    """
    message = f"Hello {name}"
    print(f"Greeting {name}")
    return {"message": message}


@app.get('/ping')
async def ping():
    """
    Health check endpoint.
    """
    print("Ping! Server is alive")
    return {"status": "ALIVE"}


@app.post('/echo')
async def echo(data: dict):
    """
    Receives JSON data and echoes it back.
    """
    print(f"Received data: {data}")
    return {"received": data, "message": "Data received!"}


if __name__ == '__main__':
    import uvicorn
    print("\n" + "="*50)
    print("Starting FastAPI server...")
    print("API Docs: http://localhost:8000/docs")
    print("ReDoc: http://localhost:8000/redoc")
    print("="*50 + "\n")
    uvicorn.run(app, host='0.0.0.0', port=8000)
