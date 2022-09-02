from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models
from .database import SessionLocal, engine
from .config import settings
from .routes import router

models.Base.metadata.create_all(bind=engine)


def create_app():
    app = FastAPI()

    include_middleware(app)
    register_routes(app)
    configure_database(app)

    return app


def include_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_routes(app):
    app.include_router(router)


# Database connection
def configure_database(app):
    @app.on_event("startup")
    async def startup():
        print("Starting db...")
        models.Base.metadata.create_all(bind=engine)

        db = SessionLocal()

        # Create default user if this doesn't exist
        admin_user = (
            db.query(models.User)
            .filter(models.User.email == settings.SUPERUSER_EMAIL)
            .first()
        )

        if not admin_user:
            crud.create_user(
                db=db,
                user=models.User(
                    email=settings.SUPERUSER_EMAIL, password=settings.SUPERUSER_PASSWORD
                ),
            )

    @app.on_event("shutdown")
    async def shutdown():
        print("Shutting down...")
