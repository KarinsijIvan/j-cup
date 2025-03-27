from fastapi import FastAPI
from routers import user, point, ping,add_estimation,del_estimation
from db.user_db import init_db as init_user_db
from db.point_db import init_db as init_point_db
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

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
app.include_router(addLike.router, prefix="/addLike", tags=["addLike"])
app.include_router(delLike.router, prefix="/delLike", tags=["delLike"])

if __name__=="__main__":
    uvicorn.run(app)