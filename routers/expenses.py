from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import ExpenseCreate, ExpenseResponse
from database import get_db
import crud
from auth import get_current_user
from models import User

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.post("/", response_model=ExpenseResponse)
async def create_expense(
    expense: ExpenseCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await crud.create_expense(db, expense, user_id=current_user.id)

@router.get("/", response_model=list[ExpenseResponse])
async def read_expenses(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await crud.get_expenses(db, user_id=current_user.id)

@router.get("/{expense_id}", response_model=ExpenseResponse)
async def read_expense(
    expense_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    expense = await crud.get_expense(db, expense_id, user_id=current_user.id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.put("/{expense_id}", response_model=ExpenseResponse)
async def update_expense(
    expense_id: int,
    expense: ExpenseCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated_expense = await crud.update_expense(db, expense_id, expense, user_id=current_user.id)
    if not updated_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return updated_expense

@router.delete("/{expense_id}", response_model=ExpenseResponse)
async def delete_expense(
    expense_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted_expense = await crud.delete_expense(db, expense_id, user_id=current_user.id)
    if not deleted_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return deleted_expense
