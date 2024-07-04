from fastapi import FastAPI, Request
from routes.customer_routes import customer_endpoints
from routes.common_routes import common_endpoints
from config.config import customers_collection
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
# from utils.customer_validators import format_validation_errors
from utils.urls_validators import error_formatters


app=FastAPI()

app.include_router(common_endpoints)
app.include_router(customer_endpoints)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):


    format_function = error_formatters.get(request.url.path, None)
    print("idnfas")
    if format_function:
        formatted_errors = format_function(exc.errors())
    else:
        formatted_errors = exc.errors()  # Default formatting
    
    return JSONResponse(
        status_code=422,
        content={"detail": formatted_errors}
    )
    
    print("inisde the validation error>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    try:

        errors = exc.errors()
        format_validation_errors(errors)
        print("errors>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", errors)
    except ValueError as e:
        print(">>>>>>>>>>>>>>", e)
