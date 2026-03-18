"""API built using FastAPI to connect a Python application to a PostgreSQL database hosted in the cloud."""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from app.config import settings
from app.database import check_database_connection, get_database_time

app = FastAPI(
    title="FastAPI Render AlwaysData API",
    version="1.0.0",
    description="FastAPI service deployed on Render with PostgreSQL hosted on AlwaysData.",
)


@app.get("/", tags=["Root"])
def root() -> dict:
    """
    Basic endpoint to verify the API is running.
    """
    return {
        "message": "API running successfully",
        "environment": settings.environment,
    }


@app.get("/health", tags=["Health"])
def health() -> JSONResponse:
    """
    Health endpoint for monitoring and Render verification.
    """
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "service": "fastapi-render-alwaysdata",
        },
    )


@app.get("/db-check", tags=["Database"])
def db_check() -> dict:
    """
    Validate database connectivity.
    """
    is_connected = check_database_connection()

    if not is_connected:
        raise HTTPException(
            status_code=500,
            detail="Database connection failed.",
        )

    return {
        "status": "ok",
        "database_connection": "successful",
    }


@app.get("/db-time", tags=["Database"])
def db_time() -> dict:
    """
    Return current database time from PostgreSQL.
    """
    db_time_value = get_database_time()

    if db_time_value is None:
        raise HTTPException(
            status_code=500,
            detail="Could not fetch database time.",
        )

    return {
        "status": "ok",
        "database_time": db_time_value.isoformat(),
    }