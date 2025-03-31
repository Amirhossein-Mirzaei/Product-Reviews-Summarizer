from fastapi import FastAPI, HTTPException, Request
from cohere_utils import generate_summary_and_pros_cons
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Endpoint for analyzing reviews
@app.post("/analyze_reviews/")
async def analyze_reviews(request: Request):
    try:
        data = await request.json()
        review_text = data.get("review_text")
        cohere_api_key = data.get("cohere_api_key")
        
        if not review_text or not cohere_api_key:
            raise HTTPException(status_code=400, detail="Missing review_text or cohere_api_key")
        
        summary, pros, cons = generate_summary_and_pros_cons(review_text, cohere_api_key)
        
        return {
            "summary": summary,
            "pros": pros,
            "cons": cons
        }
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
