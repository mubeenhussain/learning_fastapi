from fastapi import FastAPI
from database import Base,engine
from routers import auth,cart,product
from core.auth_middleware import auth_middleware
import httpx  # async HTTP client

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.middleware("http")(auth_middleware)


app.include_router(cart.router, prefix="/api",tags=["Cart"])
app.include_router(product.router, prefix="/api",tags=["Product"])
app.include_router(auth.router, prefix="/api",tags=["Authentication"])

# if __name__ == "__main__":
#     app = app()
#     app.run(host="0.0.0.0", port=5000, debug=True)