from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routes.customer_routes import customer_endpoints
from routes.common_routes import common_endpoints
from utils.urls_validators import error_formatters

app = FastAPI()

# Include routers
app.include_router(common_endpoints)
app.include_router(customer_endpoints)

# CORS configuration
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
)

# Exception handler for RequestValidationError
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Determine if there's a specific formatter for the endpoint URL
    format_function = error_formatters.get(request.url.path, None)
    
    if format_function:
        formatted_errors = format_function(exc.errors())
    else:
        formatted_errors = exc.errors()  # Default formatting
    
    # Return JSONResponse with formatted errors and status code 422
    return JSONResponse(
        status_code=422,
        content={"detail": formatted_errors}
    )

