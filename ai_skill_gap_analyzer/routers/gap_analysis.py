from fastapi import APIRouter

router = APIRouter()

@router.post("/evaluate")
def evaluate_gap(user_skills: list, job_requirements: list):
    # placeholder: compute skills missing from job requirements
    missing = [skill for skill in job_requirements if skill not in user_skills]
    return {"missing": missing}
