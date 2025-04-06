from fastapi import FastAPI
from app.models import LocationQuery, PropertyListResponse
from app.logic import find_nearby_properties

app = FastAPI()

'''
you should pass in this json format to my api '/nearest-properties' that is 
{
 "location":the customer requirements or the message of customer
}

and the run command after setting up virtual environment is 

uvicorn app.main:app --reload


'''
@app.get("/",)
async def serverrunning():
    print("ROUTE HIT")
    return  "Server is Running and to Run this Project add '/nearest-properties' and pass 'location' as json format  "


@app.post("/nearest-properties", response_model=PropertyListResponse)
async def get_nearest_properties(query: LocationQuery):
    print("DJNEN")
    return await find_nearby_properties(query.location)