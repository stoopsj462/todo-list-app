"""
TodoItem class to represent individual todo items
"""
from datetime import datetime
from typing import Optional


class TodoItem:
    """Represents a single todo item with title, completion status, and completion date"""
    
    def __init__(self, title: str, completed: bool = False, completion_date: Optional[str] = None):
        """
        Initialize a TodoItem
        
        Args:
            title (str): The title/description of the todo item
            completed (bool): Whether the item is completed
            completion_date (Optional[str]): Date when item was completed (ISO format)
        """
        self.title = title
        self.completed = completed
        self.completion_date = completion_date
    
    def mark_complete(self) -> None:
        """Mark the item as complete and set the completion date to now"""
        self.completed = True
        self.completion_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def mark_incomplete(self) -> None:
        """Mark the item as incomplete and clear the completion date"""
        self.completed = False
        self.completion_date = None
    
    def to_dict(self) -> dict:
        """Convert the TodoItem to a dictionary for JSON serialization"""
        return {
            'title': self.title,
            'completed': self.completed,
            'completion_date': self.completion_date
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'TodoItem':
        """Create a TodoItem from a dictionary"""
        return cls(
            title=data['title'],
            completed=data['completed'],
            completion_date=data.get('completion_date')
        )
    
    def __str__(self) -> str:
        """String representation of the todo item"""
        status = "✓" if self.completed else "○"
        if self.completed and self.completion_date:
            return f"{status} {self.title} (Completed: {self.completion_date})"
        else:
            return f"{status} {self.title}"
    
    def __repr__(self) -> str:
        return f"TodoItem(title='{self.title}', completed={self.completed}, completion_date='{self.completion_date}')"