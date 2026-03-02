from fastapi import Request


async def log_requests(request: Request, call_next):
    """
    Middleware that logs incoming requests and outgoing responses.

    This function runs before and after each request:
    - Logs the HTTP method and URL of incoming requests
    - Passes the request to the next handler
    - Logs the response status code
    - Returns the response

    Args:
        request: The incoming HTTP request
        call_next: Function to call the next middleware/handler

    Returns:
        The HTTP response
    """
    # Log incoming request
    print(f"\n{'='*50}")
    print(f"Incoming request: {request.method} {request.url}")
    print(f"{'='*50}")

    # Process the request and get response
    response = await call_next(request)

    # Log response status
    print(f"Response status: {response.status_code}")
    print(f"{'='*50}\n")

    return response
