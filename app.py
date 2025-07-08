from fastapi import FastAPI
from database import Base,engine
from routers import auth,task
from core.auth_middleware import auth_middleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.middleware("http")(auth_middleware)

app.include_router(auth.router, prefix="/api",tags=["Authentication"])
app.include_router(task.router ,prefix="/tasks", tags=["Tasks"])

# if __name__ == "__main__":
#     app = app()
#     app.run(host="0.0.0.0", port=5000, debug=True)
    