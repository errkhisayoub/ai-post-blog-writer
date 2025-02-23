from fastapi import APIRouter, HTTPException
from gemini import Gemini

router = APIRouter()


@router.get("/status")
async def status():
    return {"status": "it works"}

@router.get("/write_post")
async def write_post(topic: str):
    try:
        gemini = Gemini()
        response = await gemini.get_gemini_resp(topic=topic)
    except Exception as e:
        print(f"error occured {e}")
        raise HTTPException(404, detail=f"error occured {e}")

    return {"reponse": response}
