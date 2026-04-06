from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

from backend.preprocess import preprocess_text
from backend.semantic_analyzer import analyze_semantics
from backend.ir_generator import generate_ir
from backend.pseudocode_generator import generate_pseudocode
from backend.code_generator import generate_code
from backend.analysis.time_complexity import analyze_time_complexity
from backend.analysis.space_complexity import analyze_space_complexity
from backend.analysis.numerical_analysis import analyze_numerical_properties

from backend.auth import (
    signup_user,
    login_user,
    validate_token,
    change_password,
    forgot_password,
    reset_password,
    get_user_by_token
)

app = FastAPI()

# -------------------- CORS --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- MODELS --------------------

class AuthRequest(BaseModel):
    username: str
    password: str

class ChangePasswordRequest(BaseModel):
    username: str
    old_password: str
    new_password: str

class ForgotPasswordRequest(BaseModel):
    username: str

class ResetPasswordRequest(BaseModel):
    reset_token: str
    new_password: str

class AnalyzeRequest(BaseModel):
    text: str

# -------------------- TOKEN DEPENDENCY --------------------

async def verify_token(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="No token provided")

    token = authorization.replace("Bearer ", "") if authorization.startswith("Bearer ") else authorization

    if not validate_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")

    return token

# -------------------- AUTH ROUTES --------------------

@app.post("/signup")
def signup(request: AuthRequest):
    success, response = signup_user(request.username, request.password)

    if not success:
        raise HTTPException(status_code=400, detail=response)

    return {
        "status": "success",
        "message": "User created successfully",
        "token": response
    }

@app.post("/login")
def login(request: AuthRequest):
    success, response = login_user(request.username, request.password)

    if not success:
        raise HTTPException(status_code=401, detail=response)

    return {
        "status": "success",
        "message": "Login successful",
        "token": response
    }

@app.post("/change-password")
def change_password_route(request: ChangePasswordRequest, token: str = Depends(verify_token)):
    success, message = change_password(
        request.username,
        request.old_password,
        request.new_password
    )

    if not success:
        raise HTTPException(status_code=400, detail=message)

    return {
        "status": "success",
        "message": message
    }

@app.post("/forgot-password")
def forgot_password_route(request: ForgotPasswordRequest):
    success, result = forgot_password(request.username)

    if not success:
        raise HTTPException(status_code=404, detail=result)

    return {
        "status": "success",
        "message": "Password reset token generated",
        "reset_token": result
    }

@app.post("/reset-password")
def reset_password_route(request: ResetPasswordRequest):
    success, message = reset_password(request.reset_token, request.new_password)

    if not success:
        raise HTTPException(status_code=400, detail=message)

    return {
        "status": "success",
        "message": message
    }

@app.get("/user-info")
def user_info(token: str = Depends(verify_token)):
    user = get_user_by_token(token)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "status": "success",
        "user": user
    }

@app.get("/validate")
def validate(token: str = Depends(verify_token)):
    return {"valid": True}

# -------------------- ANALYZE ROUTE --------------------

@app.post("/analyze")
def analyze(request: AnalyzeRequest, token: str = Depends(verify_token)):

    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Input text cannot be empty")

    preprocessed = preprocess_text(text)
    semantics = analyze_semantics(preprocessed, original_text=text)

    # ERROR
    if semantics["method_type"] == "unknown":
        return {
            "status": "error",
            "confidence_score": semantics.get("confidence_score", 0),
            "explanation": semantics.get("explanation", "Unable to determine method")
        }

    # AMBIGUOUS
    if semantics["method_type"] == "ambiguous":
        return {
            "status": "ambiguous",
            "confidence_score": semantics.get("confidence_score", 0),
            "explanation": semantics.get("explanation", "Ambiguous mathematical description")
        }

    # SUCCESS PIPELINE
    ir = generate_ir(semantics)
    pseudocode = generate_pseudocode(ir)
    code = generate_code(ir)
    time_complexity = analyze_time_complexity(ir)
    space_complexity = analyze_space_complexity(ir)
    numerical_analysis = analyze_numerical_properties(ir)

    return {
        "status": "success",
        "confidence_score": semantics.get("confidence_score", 1.0),
        "explanation": semantics.get("explanation", ""),
        "intermediate_representation": ir,
        "pseudocode": pseudocode,
        "executable_code": code,
        "time_complexity": time_complexity,
        "space_complexity": space_complexity,
        "numerical_analysis": numerical_analysis
    }