import asyncio
from datetime import datetime
from typing import List, Optional, Dict

# A dictionary to store to_do items.
class TodoItem:
    def __init__(self, id: int, description: str):
        self.id = id
        self.description = description
        self.created_on = datetime.now()
        self.completed_on: Optional[datetime] = None

    def complete(self):
        self.completed_on = datetime.now()

    def update(self, description: str):
        self.description = description


#  An integer to keep track of the next ID to be assigned to a new to_do item.
class TodoApp:
    def __init__(self):
        self.todos: Dict[int, TodoItem] = {}
        self.next_id = 1

    # A static method to create a new instance of TodoApp
    @staticmethod
    def new():
        return TodoApp()

    # Creates a new to_do item
    async def create(self, description: str) -> TodoItem:
        todo = TodoItem(id=self.next_id, description=description)
        self.todos[self.next_id] = todo
        self.next_id += 1
        return todo

    # Updates the description of an existing to_do item
    async def update(self, todo_id: int, description: str) -> Optional[TodoItem]:
        todo = self.todos.get(todo_id)
        if todo:
            todo.update(description)
        return todo

    # Deletes a to_do item
    async def delete(self, todo_id: int) -> bool:
        if todo_id in self.todos:
            del self.todos[todo_id]
            return True
        return False

    # Marks a to_do item as completed.
    async def complete(self, todo_id: int) -> Optional[TodoItem]:
        todo = self.todos.get(todo_id)
        if todo:
            todo.complete()
        return todo

    # Filters to_do items based on partial text search and completion status
    async def filter(self, text: Optional[str] = None, completed: Optional[bool] = None) -> List[TodoItem]:
        result = list(self.todos.values())
        if text:
            result = [todo for todo in result if text in todo.description]
        if completed is not None:
            if completed:
                result = [todo for todo in result if todo.completed_on is not None]
            else:
                result = [todo for todo in result if todo.completed_on is None]
        return result
