from fastapi import FastAPI
from routers import user, point, ping
from db.user_db import init_db as init_user_db
from db.point_db import init_db as init_point_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
init_user_db()
init_point_db()

app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(point.router, prefix="/point", tags=["point"])
app.include_router(ping.router, prefix="", tags=["Ping"])