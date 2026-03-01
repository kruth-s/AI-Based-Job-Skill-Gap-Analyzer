from fastapi import APIRouter

router = APIRouter()

@router.get("/trends")
def get_demand_trends():
    # placeholder implementation
    return {"trends": []}
