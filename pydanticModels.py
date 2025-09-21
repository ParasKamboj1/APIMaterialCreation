from pydantic import BaseModel, Field
from typing import Annotated, Optional

class PageOneModel(BaseModel):
    id: Optional[Annotated[int, Field(description="Enter ID", examples=["101"])]] = None
    material: Optional[Annotated[str, Field(description="Enter Material", examples=["Water Bottle"])]] = None
    materialType: Optional[Annotated[str, Field(description="Enter Material Type", examples=["Steel"])]] = None
    industrySector: Optional[Annotated[str, Field(description="Enter Industry Sector", examples=["Manufacturer"])]] = None

class PageTwoModel(BaseModel):
    id: Optional[Annotated[int, Field(description="Enter ID", examples=["101"])]] = None
    material: Optional[Annotated[str, Field(description="Enter Material", examples=["Water Bottle"])]] = None
    qtyStructure: Optional[Annotated[str, Field(description="Enter qtyStructure", examples=["testing"])]] = None

class PageThreeModel(BaseModel):
    id: Optional[Annotated[int, Field(description="Enter ID", examples=["101"])]] = None
    material: Optional[Annotated[str, Field(description="Enter Material", examples=["Water Bottle"])]] = None
    currency: Optional[Annotated[str, Field(description="Enter Currency", examples=["INR"])]] = None
    priceControl: Optional[Annotated[str, Field(description="Enter Price Control", examples=["price control"])]] = None

class PageFourModel(BaseModel):
    id: Optional[Annotated[int, Field(description="Enter ID", examples=["101"])]] = None
    material: Optional[Annotated[str, Field(description="Enter Material", examples=["Water Bottle"])]] = None
    description: Optional[Annotated[str, Field(description="Enter Description", examples=["hello I am going to create material"])]] = None
    baseUnitOfMeasure: Optional[Annotated[str, Field(description="Enter Base Unit Of Measure", examples=["KG"])]] = None

class PageFiveModel(BaseModel):
    id: Optional[Annotated[int, Field(description="Enter ID", examples=["101"])]] = None
    material: Optional[Annotated[str, Field(description="Enter Material", examples=["Water Bottle"])]] = None
    itemCategoryGroup: Optional[Annotated[str, Field(description="Enter Item Category Group", examples=["group 34"])]] = None

class PageSixModel(BaseModel):
    id: Optional[Annotated[int, Field(description="Enter ID", examples=["101"])]] = None
    material: Optional[Annotated[str, Field(description="Enter Material", examples=["Water Bottle"])]] = None
    salesOrg: Optional[Annotated[str, Field(description="Enter SalesOrg", examples=["101"])]] = None
    distriChannel: Optional[Annotated[str, Field(description="Enter Distri Channel", examples=["testing districhannel"])]] = None
    baseUnitOfMeasure: Optional[Annotated[str, Field(description="Enter BaseUnitOfMeasure", examples="KG")]] = None
    taxClassification: Optional[Annotated[str, Field(description="Enter Tax Classification", examples=["taxClassification"])]] = None

class PageSevenModel(BaseModel):
    id: Optional[Annotated[int, Field(description="Enter ID", examples="101")]] = None
    material: Optional[Annotated[str, Field(description="Enter Material", examples=["Water Bottle"])]] = None
    plant: Optional[Annotated[str, Field(description="Enter Plant", examples="10451")]] = None
    availabilityCheck: Optional[Annotated[str, Field(description="Enter Availability Check", examples=["true"])]] = None
    baseUnitOfMeasure: Optional[Annotated[str, Field(description="Enter BaseUnitOfMeasure", examples="KG")]] = None

class PageEightModel(BaseModel):
    id: Optional[Annotated[int, Field(description="Enter ID", examples="101")]] = None
    material: Optional[Annotated[str, Field(description="Enter Material", examples=["Water Bottle"])]] = None
    procurementType: Optional[Annotated[str, Field(description="Enter Procurement Type", examples="integer")]] = None
    inhouseProduction: Optional[Annotated[str, Field(description="Enter InhouseProduction", examples=["Inhouse Production"])]] = None

class PageNineModel(BaseModel):
    id: Optional[Annotated[int, Field(description="Enter ID", examples="101")]] = None
    material: Optional[Annotated[str, Field(description="Enter Material", examples=["Water Bottle"])]] = None
    mrpType: Optional[Annotated[str, Field(description="Enter mrpType", examples="mrptype")]] = None
    reorderPoint: Optional[Annotated[str, Field(description="Enter Reorder Point", examples=["ReorderPoint"])]] = None
    fixedLotSize: Optional[Annotated[str, Field(description="Enter FixedLot Size", examples="101")]] = None
    mrpController: Optional[Annotated[str, Field(description="Enter MRP Controller", examples=["MRP Controller"])]] = None
    maximumStockLevel: Optional[Annotated[str, Field(description="Enter Maximum Stock Level", examples="101")]] = None
    planningtimefence: Optional[Annotated[str, Field(description="Enter Planning Time Fence", examples=["Planning Time Fence"])]] = None
    lotSizingProcedure: Optional[Annotated[str, Field(description="Lot Sizing Procedure", examples="10149r4fduh")]] = None
