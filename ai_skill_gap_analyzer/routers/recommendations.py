from fastapi import APIRouter

router = APIRouter()

@router.post("/generate")
def generate_recommendations(missing_skills: list):
    # placeholder: map missing skills to resources
    return {"recommendations": []}
