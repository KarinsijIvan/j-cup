from fastapi import APIRouter

router = APIRouter(tags=["Ping"])

@router.get("/ping")
def ping():
    return {"message": "pong"}
