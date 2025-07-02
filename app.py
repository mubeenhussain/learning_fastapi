from fastapi import FastAPI
from database import Base,engine
from routers import auth


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth",tags=["Authentication"])

if __name__ == "__main__":
    app = app()
    app.run(host="0.0.0.0", port=5000, debug=True)
    