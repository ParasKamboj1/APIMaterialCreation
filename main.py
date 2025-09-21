from fastapi import FastAPI,HTTPException,Body
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
import pydanticModels as models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

client = MongoClient("mongodb://localhost:27017/")

database = client["MaterialsBandM"]

MODEL_COLLECTION_MAP = {
    "page_one" : (models.PageOneModel,database["page_one"]),
    "page_two" : (models.PageTwoModel,database["page_two"]),
    "page_three" : (models.PageThreeModel,database["page_three"]),
    "page_four" : (models.PageFourModel,database["page_four"]),
    "page_five" : (models.PageFiveModel,database["page_five"]),
    "page_six" : (models.PageSixModel,database["page_six"]),
    "page_seven" : (models.PageSevenModel,database["page_seven"]),
    "page_eight" : (models.PageEightModel,database["page_eight"]),
    "page_nine" : (models.PageNineModel,database["page_nine"])
}

@app.post("/create/{page_name}")
def create_page_data(page_name: str, data: dict = Body(...)):
    if page_name not in MODEL_COLLECTION_MAP:
        raise HTTPException(status_code=400, detail="Invalid Page Name")
    
    model, collection = MODEL_COLLECTION_MAP[page_name]

    # If material not provided → auto-generate
    if not data.get("material"):   # handles None, "" and missing key
        new_material = automatically_generate_id()
        data["material"] = str(new_material)

    validated_data = model(**data).model_dump(exclude_unset=True, exclude_none=True)
    result = collection.insert_one(validated_data)
    
    return {"inserted_data": str(result.inserted_id), "material": data["material"]}


@app.get("/get/completedata/{page_number}")
def get_documents(page_number : str):
    if page_number not in MODEL_COLLECTION_MAP:
        raise HTTPException(status_code=400,detail="Invalid Page Number")
    _,collection = MODEL_COLLECTION_MAP[page_number]
    docs = []
    for d in collection.find():
        d["_id"] = str(d["_id"])
        docs.append(d)
    return docs 

@app.get("/generate/id/")
def automatically_generate_id():
    collection = database["page_one"]
    highest_id_document = collection.find_one(sort=[("id",-1)])

    if highest_id_document:
        highest_id = highest_id_document["id"]
    else:
        highest_id = 0
    return highest_id + 1

@app.put("/update/pagenumber/{page_name2}")
def update_document_partial(page_name2 : str , data : dict = Body(...)):
   if page_name2 not in MODEL_COLLECTION_MAP:
        raise HTTPException(status_code=400,detail="Invalid Page Number")
   model,collection = MODEL_COLLECTION_MAP[page_name2]
   if "id" not in data or "material" not in data:
        raise HTTPException(status_code=400, detail="'id' and 'material' are required to update")
   filter_query = {"id" : data["id"] , "material" : data["material"]}
   validated_data = model(**data).model_dump(exclude_unset = True)
   result = collection.update_one(filter_query,{"$set":validated_data})

   if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Document not found")

   return {"message": "Document updated successfully"}

