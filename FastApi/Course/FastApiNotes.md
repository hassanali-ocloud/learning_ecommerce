# 1. General:
- It handles all the server side business logic along with renders the front-end page.
- unicorn books:app --reload
- openai standards for creating apis.
-> localhost:8000/openapi.json
-> localhost:8000/docs
- CRUD: get, post, put, patch, delete

# 2. Status Code:
- 1xx -> Informational response: Request Processing
- 2xx -> Success: Request successfully complete
- 3xx -> Redicrection: Further action must be completed
- 4xx -> Client Errors: An error was caused by the request from the client.
- 5xx -> Server errors: An error has occured on the server.

# 3. Additional Libraries:
- Use pydantic for validation
- 