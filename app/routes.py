from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Expense, ExpenseCreate, ExpenseUpdate, Summary

router = APIRouter()

# In-memory storage
expenses_db: dict = {}
counter: int = 0


def reset_db():
    """Used by tests to reset state"""
    global expenses_db, counter
    expenses_db = {}
    counter = 0


@router.get("/expenses", response_model=List[Expense], tags=["Expenses"])
def get_all_expenses():
    """Fetch all expenses"""
    return list(expenses_db.values())


@router.post("/expenses", response_model=Expense, status_code=201, tags=["Expenses"])
def create_expense(expense: ExpenseCreate):
    """Create a new expense"""
    global counter
    counter += 1
    new_expense = Expense(
        id=counter,
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        description=expense.description
    )
    expenses_db[counter] = new_expense
    return new_expense


@router.get("/expenses/summary", response_model=Summary, tags=["Summary"])
def get_summary():
    """Get total spending summary grouped by category"""
    total_amount = sum(e.amount for e in expenses_db.values())
    by_category = {}
    for e in expenses_db.values():
        by_category[e.category] = round(by_category.get(e.category, 0) + e.amount, 2)
    return Summary(
        total_expenses=len(expenses_db),
        total_amount=round(total_amount, 2),
        by_category=by_category
    )


@router.get("/expenses/{expense_id}", response_model=Expense, tags=["Expenses"])
def get_expense(expense_id: int):
    """Get a single expense by ID"""
    if expense_id not in expenses_db:
        raise HTTPException(status_code=404, detail=f"Expense with id {expense_id} not found")
    return expenses_db[expense_id]


@router.put("/expenses/{expense_id}", response_model=Expense, tags=["Expenses"])
def update_expense(expense_id: int, expense: ExpenseCreate):
    """Fully replace an expense"""
    if expense_id not in expenses_db:
        raise HTTPException(status_code=404, detail=f"Expense with id {expense_id} not found")
    updated = Expense(
        id=expense_id,
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        description=expense.description
    )
    expenses_db[expense_id] = updated
    return updated


@router.patch("/expenses/{expense_id}", response_model=Expense, tags=["Expenses"])
def partial_update_expense(expense_id: int, expense: ExpenseUpdate):
    """Partially update an expense"""
    if expense_id not in expenses_db:
        raise HTTPException(status_code=404, detail=f"Expense with id {expense_id} not found")
    existing = expenses_db[expense_id]
    updated_data = existing.model_dump()
    patch_data = expense.model_dump(exclude_unset=True)
    updated_data.update(patch_data)
    expenses_db[expense_id] = Expense(**updated_data)
    return expenses_db[expense_id]


@router.delete("/expenses/{expense_id}", tags=["Expenses"])
def delete_expense(expense_id: int):
    """Delete an expense by ID"""
    if expense_id not in expenses_db:
        raise HTTPException(status_code=404, detail=f"Expense with id {expense_id} not found")
    del expenses_db[expense_id]
    return {"message": f"Expense {expense_id} deleted successfully"}
