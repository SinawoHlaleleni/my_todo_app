import pytest
import asyncio
from src.todo_app import TodoApp


@pytest.mark.asyncio
async def test_todo_app():
    app = TodoApp.new()

    # Create a to_do
    todo = await app.create("Write tests")
    assert todo.description == "Write tests"
    assert not todo.completed_on

    # Update the to_do
    updated_todo = await app.update(todo.id, "Write more tests")
    assert updated_todo.description == "Write more tests"

    # Complete the to_do
    completed_todo = await app.complete(todo.id)
    assert completed_todo.completed_on

    # Filter by completed
    completed_todos = await app.filter(completed=True)
    assert len(completed_todos) == 1

    # Delete the to_do
    assert await app.delete(todo.id)

    # Filter by to_do
    remaining_todos = await app.filter()
    assert len(remaining_todos) == 0
