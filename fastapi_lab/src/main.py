from fastapi import FastAPI
from pydantic import BaseModel, Field

from predict import predict_banknote, artifact


app = FastAPI(
    title="Banknote Classification API",
    description="UCI Banknote Classification using Random Forest",
    version="1.0"
)


class BanknoteData(BaseModel):
    variance: float = Field(description="Image variance")
    skewness: float = Field(description="Image skewness")
    curtosis: float = Field(description="Image curtosis")
    entropy: float = Field(description="Image entropy")


class BanknoteResponse(BaseModel):
    prediction: int
    confidence: float


@app.get("/")
def home():
    return {
        "message": "Welcome to the Banknote Classification API"
    }


@app.get("/model-info")
def model_info():
    return {
        "dataset": "UCI Banknote Authentication",
        "model": "Random Forest",
        "features": artifact["features"],
        "test_accuracy": artifact["accuracy"]
    }


@app.post("/predict", response_model=BanknoteResponse)
def predict(data: BanknoteData):

    result = predict_banknote(
        variance=data.variance,
        skewness=data.skewness,
        curtosis=data.curtosis,
        entropy=data.entropy
    )

    return result





    
