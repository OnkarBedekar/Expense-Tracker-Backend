from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import User, Expense
from schemas import UserCreate, ExpenseCreate, UserUpdate, PasswordUpdate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Retrieve user by username
async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).where(User.username == username))
    return result.scalars().first()

# Retrieve user by email
async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()

# Retrieve user by ID
async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()

# Create a new user (with email)
async def create_user(db: AsyncSession, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

# Update user profile
async def update_user(db: AsyncSession, user_id: int, user_data: UserUpdate):
    db_user = await get_user_by_id(db, user_id)
    if db_user:
        for key, value in user_data.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        await db.commit()
        await db.refresh(db_user)
    return db_user

# Update user password
async def update_password(db: AsyncSession, user_id: int, password_data: PasswordUpdate):
    db_user = await get_user_by_id(db, user_id)
    if db_user and verify_password(password_data.current_password, db_user.hashed_password):
        db_user.hashed_password = get_password_hash(password_data.new_password)
        await db.commit()
        await db.refresh(db_user)
        return True
    return False

# Expense CRUD operations
async def create_expense(db: AsyncSession, expense: ExpenseCreate, user_id: int):
    db_expense = Expense(**expense.dict(), user_id=user_id)
    db.add(db_expense)
    await db.commit()
    await db.refresh(db_expense)
    return db_expense

async def get_expenses(db: AsyncSession, user_id: int):
    result = await db.execute(select(Expense).where(Expense.user_id == user_id))
    return result.scalars().all()

async def get_expense(db: AsyncSession, expense_id: int, user_id: int):
    result = await db.execute(
        select(Expense).where(Expense.id == expense_id, Expense.user_id == user_id)
    )
    return result.scalars().first()

async def update_expense(db: AsyncSession, expense_id: int, expense_data: ExpenseCreate, user_id: int):
    expense = await get_expense(db, expense_id, user_id)
    if expense:
        for key, value in expense_data.dict().items():
            setattr(expense, key, value)
        await db.commit()
        await db.refresh(expense)
    return expense

async def delete_expense(db: AsyncSession, expense_id: int, user_id: int):
    expense = await get_expense(db, expense_id, user_id)
    if expense:
        await db.delete(expense)
        await db.commit()
    return expense
