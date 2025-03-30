from fastapi import FastAPI
from routers import ping
from db.user_db import init_db as init_user_db
from db.point_db import init_db as init_point_db
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


from routers.user_routers import get_user_from_token, sign_in,sign_up 
from routers.point_routers import add_point, get_point,get_point_list
from routers.estimation_routers import add_estimation, del_estimation



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


app.include_router(get_user_from_token.router)
app.include_router(sign_in.router)
app.include_router(sign_up.router)

app.include_router(add_point.router)
app.include_router(get_point.router)
app.include_router(get_point_list.router)

app.include_router(add_estimation.router)
app.include_router(del_estimation.router)



if __name__=="__main__":
    uvicorn.run(app)