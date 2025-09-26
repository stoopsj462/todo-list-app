"""
TodoList class to represent a collection of todo items
"""
from typing import List, Optional
from todo_item import TodoItem


class TodoList:
    """Represents a named list of todo items"""
    
    def __init__(self, name: str, items: Optional[List[TodoItem]] = None):
        """
        Initialize a TodoList
        
        Args:
            name (str): The name of the todo list
            items (Optional[List[TodoItem]]): Initial list of items
        """
        self.name = name
        self.items = items or []
    
    def add_item(self, title: str) -> TodoItem:
        """
        Add a new todo item to the list
        
        Args:
            title (str): The title/description of the todo item
            
        Returns:
            TodoItem: The newly created todo item
        """
        item = TodoItem(title)
        self.items.append(item)
        return item
    
    def remove_item(self, index: int) -> bool:
        """
        Remove a todo item by index
        
        Args:
            index (int): The index of the item to remove (0-based)
            
        Returns:
            bool: True if item was removed, False if index was invalid
        """
        if 0 <= index < len(self.items):
            self.items.pop(index)
            return True
        return False
    
    def complete_item(self, index: int) -> bool:
        """
        Mark a todo item as complete by index
        
        Args:
            index (int): The index of the item to complete (0-based)
            
        Returns:
            bool: True if item was marked complete, False if index was invalid
        """
        if 0 <= index < len(self.items):
            self.items[index].mark_complete()
            return True
        return False
    
    def uncomplete_item(self, index: int) -> bool:
        """
        Mark a todo item as incomplete by index
        
        Args:
            index (int): The index of the item to mark incomplete (0-based)
            
        Returns:
            bool: True if item was marked incomplete, False if index was invalid
        """
        if 0 <= index < len(self.items):
            self.items[index].mark_incomplete()
            return True
        return False
    
    def get_pending_items(self) -> List[TodoItem]:
        """Get all incomplete items"""
        return [item for item in self.items if not item.completed]
    
    def get_completed_items(self) -> List[TodoItem]:
        """Get all completed items"""
        return [item for item in self.items if item.completed]
    
    def get_item_count(self) -> dict:
        """Get count statistics for the list"""
        total = len(self.items)
        completed = len(self.get_completed_items())
        pending = total - completed
        return {
            'total': total,
            'completed': completed,
            'pending': pending
        }
    
    def to_dict(self) -> dict:
        """Convert the TodoList to a dictionary for JSON serialization"""
        return {
            'name': self.name,
            'items': [item.to_dict() for item in self.items]
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'TodoList':
        """Create a TodoList from a dictionary"""
        items = [TodoItem.from_dict(item_data) for item_data in data.get('items', [])]
        return cls(name=data['name'], items=items)
    
    def display(self, show_completed: bool = True) -> str:
        """
        Get a formatted display of the todo list
        
        Args:
            show_completed (bool): Whether to show completed items
            
        Returns:
            str: Formatted string representation of the list
        """
        if not self.items:
            return f"\n=== {self.name} ===\n(No items in this list)\n"
        
        output = [f"\n=== {self.name} ==="]
        
        # Show pending items first
        pending_items = self.get_pending_items()
        if pending_items:
            output.append("\nPending:")
            for i, item in enumerate(self.items):
                if not item.completed:
                    output.append(f"  {i+1}. {item}")
        
        # Show completed items if requested
        if show_completed:
            completed_items = self.get_completed_items()
            if completed_items:
                output.append("\nCompleted:")
                for i, item in enumerate(self.items):
                    if item.completed:
                        output.append(f"  {i+1}. {item}")
        
        # Show statistics
        stats = self.get_item_count()
        output.append(f"\nStats: {stats['completed']}/{stats['total']} completed, {stats['pending']} pending\n")
        
        return "\n".join(output)
    
    def __str__(self) -> str:
        return self.display()
    
    def __repr__(self) -> str:
        return f"TodoList(name='{self.name}', items={len(self.items)} items)"