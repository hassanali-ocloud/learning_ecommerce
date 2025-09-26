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

# 4. JWT:
- JWT (Json Web Token): Three parts: <Header>.<Payload>.<Signature>
- Header: Two parts: Alg: Algorithm for sigining, typ: The specific type of token.
-> Header then encoded using base64 to create first part of JWT
- Payload: contains actual data of user and other info along with claims. Three claims:
-> Registered: Predefined claims. Recommended but not  mandatory. Top three claims: ISS, Sub and Exp.
-> ISS: Issuer. This princple identifies the principle that issue the JWT.
-> Sub: Stands for subject. Hold statement about the subject. Must be scoped locally or globally.
-> Exp: JWT Expiration time.
-> Payload also converted to base64.
- Signature: Created using the algo in the header to hash out the ecoded header, encoded payload with a secret.
- https://www.jwt.io/

16 Routing - 009