from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class Category(str, Enum):
    food = "food"
    transport = "transport"
    shopping = "shopping"
    bills = "bills"
    entertainment = "entertainment"
    other = "other"


class ExpenseCreate(BaseModel):
    title: str
    amount: float = Field(gt=0, description="Amount must be greater than 0")
    category: Category
    description: Optional[str] = None


class ExpenseUpdate(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = Field(None, gt=0)
    category: Optional[Category] = None
    description: Optional[str] = None


class Expense(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    description: Optional[str] = None


class Summary(BaseModel):
    total_expenses: int
    total_amount: float
    by_category: dict
