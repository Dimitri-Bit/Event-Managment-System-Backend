import asyncio
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from main import app
from database.database import get_db_session
from model.base import Base  # Adjust to import your Base class correctly

# Async MySQL test database configuration
TEST_DATABASE_URL = "mysql+aiomysql://testuser:testpassword@localhost/test_db"
engine = create_async_engine(TEST_DATABASE_URL)
TestingSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="function")
async def db_session():
    # Create all tables in the test database
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # Create a new session for each test
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        await session.close()

@pytest.fixture(scope="function")
async def client(db_session: AsyncSession):
    # Override the get_db_session dependency to use our test database
    async def override_get_db_session():
        try:
            yield db_session
        finally:
            await db_session.close()

    app.dependency_overrides[get_db_session] = override_get_db_session

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

    # Reset the dependency override
    app.dependency_overrides = {}

@pytest.fixture(scope="function")
async def test_data(db_session: AsyncSession):
    # Import your Party model from the model folder
    from model.parties_model import Party  # Adjust to match your actual model path

    # Create test party data
    party1 = Party(id=1, name="Test Party 1")  # Adjust fields to match your model
    party2 = Party(id=2, name="Test Party 2")

    db_session.add(party1)
    db_session.add(party2)
    await db_session.commit()

# Updated test functions using the fixtures - now we need to use pytest.mark.asyncio
@pytest.mark.asyncio
async def test_parties_get_all(client, test_data):
    response = await client.get("/party")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2  # At least our test data should be returned

@pytest.mark.asyncio
async def test_parties_get_by_id(client, test_data):
    response = await client.get("/party/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Test Party 1"
