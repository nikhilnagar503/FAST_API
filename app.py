from fastapi import  FastAPI

from fastapi.responses import JSONResponse
from schema.user_input import User_Input
from model.predict import predict_output

app = FastAPI()


        
@app.post("/predict")
def predict_premimum(data: User_Input):
    user_input = {
        'bmi': data.bmi,  # Computed field
        'age_gp': data.age_gp,  # Note: Changed from 'age_gp' to 'age_group' (see below)
        'lifestyle_risk': data.lifestyle_risk,  # Computed field
        'city_tier': data.city_tier,  # Computed field
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    # Rest of the code...


    try :
        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'response': prediction})
    
    except Exception as e:

        return JSONResponse(status_code=500, content=str(e))