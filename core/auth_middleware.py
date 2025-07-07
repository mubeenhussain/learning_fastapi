from fastapi import Request, status
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
from core.security import SECRET_KEY, ALGORITHM

async def auth_middleware(request: Request, call_next):
    # List of public endpoints that don't require authentication
    # if request.url.path.startswith("/auth/") or request.url.path.startswith("/docs") or request.url.path.startswith("/openapi.json"):
    if "auth" not in request.url.path:
        return await call_next(request)

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Not authenticated"},
        )
    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        request.state.user = payload.get("sub")
    except JWTError:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Invalid token"},
        )
    return await call_next(request)