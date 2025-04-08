from fastapi import FastAPI
from routers import ping
from db.user_db import init_db as init_user_db
from db.point_db import init_db as init_point_db
from db.estimation_db import init_db as init_estimation_db
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


from routers.user_routers import get_user_from_token, sign_in,sign_up 
from routers.point_routers import add_point, get_point,get_point_list
from routers.estimation_routers import add_estimation, del_estimation, get_user_estimation
from routers.proposal_routers import add_proposal, get_proposal, get_proposal_list
from routers.route_routers import add_route, get_route, get_route_list
from routers.all_types import del_by_id, get_all



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
init_estimation_db()

app.include_router(ping.router)

app.include_router(get_user_from_token.router)
app.include_router(sign_in.router)
app.include_router(sign_up.router)

app.include_router(get_all.router)
app.include_router(del_by_id.router)

app.include_router(add_point.router)
app.include_router(get_point.router)
app.include_router(get_point_list.router)
app.include_router(get_all.router)

app.include_router(add_proposal.router)
app.include_router(get_proposal.router)
app.include_router(get_proposal_list.router)

app.include_router(add_route.router)
app.include_router(get_route.router)
app.include_router(get_route_list.router)

app.include_router(add_estimation.router)
app.include_router(del_estimation.router)
app.include_router(get_user_estimation.router)


if __name__=="__main__":
    uvicorn.run(app)