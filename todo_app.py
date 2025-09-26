"""
TodoApp - Main application class for managing multiple todo lists
"""
import json
import os
from typing import List, Optional, Dict
from todo_list import TodoList
from todo_item import TodoItem


class TodoApp:
    """Main application class for managing multiple todo lists with persistence"""
    
    def __init__(self, data_file: str = "todo_data.json"):
        """
        Initialize the TodoApp
        
        Args:
            data_file (str): Path to the JSON file for saving/loading data
        """
        self.data_file = data_file
        self.lists: Dict[str, TodoList] = {}
        self.current_list_name: Optional[str] = None
        self.load_data()
    
    def create_list(self, name: str) -> bool:
        """
        Create a new todo list
        
        Args:
            name (str): Name of the new list
            
        Returns:
            bool: True if list was created, False if name already exists
        """
        if name in self.lists:
            return False
        
        self.lists[name] = TodoList(name)
        if self.current_list_name is None:
            self.current_list_name = name
        return True
    
    def delete_list(self, name: str) -> bool:
        """
        Delete a todo list
        
        Args:
            name (str): Name of the list to delete
            
        Returns:
            bool: True if list was deleted, False if list doesn't exist
        """
        if name not in self.lists:
            return False
        
        del self.lists[name]
        
        # If we deleted the current list, set current to first available or None
        if self.current_list_name == name:
            self.current_list_name = next(iter(self.lists.keys())) if self.lists else None
        
        return True
    
    def switch_list(self, name: str) -> bool:
        """
        Switch to a different todo list
        
        Args:
            name (str): Name of the list to switch to
            
        Returns:
            bool: True if switched successfully, False if list doesn't exist
        """
        if name in self.lists:
            self.current_list_name = name
            return True
        return False
    
    def get_current_list(self) -> Optional[TodoList]:
        """Get the currently active todo list"""
        if self.current_list_name and self.current_list_name in self.lists:
            return self.lists[self.current_list_name]
        return None
    
    def get_list_names(self) -> List[str]:
        """Get all todo list names"""
        return list(self.lists.keys())
    
    def add_item(self, title: str, list_name: Optional[str] = None) -> bool:
        """
        Add a todo item to a list
        
        Args:
            title (str): Title of the todo item
            list_name (Optional[str]): Name of list to add to (uses current if None)
            
        Returns:
            bool: True if item was added, False if no list available
        """
        target_list = None
        
        if list_name:
            target_list = self.lists.get(list_name)
        else:
            target_list = self.get_current_list()
        
        if target_list:
            target_list.add_item(title)
            return True
        return False
    
    def complete_item(self, index: int, list_name: Optional[str] = None) -> bool:
        """
        Mark a todo item as complete
        
        Args:
            index (int): Index of the item (1-based for user interface)
            list_name (Optional[str]): Name of list (uses current if None)
            
        Returns:
            bool: True if item was completed, False otherwise
        """
        target_list = None
        
        if list_name:
            target_list = self.lists.get(list_name)
        else:
            target_list = self.get_current_list()
        
        if target_list:
            # Convert from 1-based to 0-based index
            return target_list.complete_item(index - 1)
        return False
    
    def uncomplete_item(self, index: int, list_name: Optional[str] = None) -> bool:
        """
        Mark a todo item as incomplete
        
        Args:
            index (int): Index of the item (1-based for user interface)
            list_name (Optional[str]): Name of list (uses current if None)
            
        Returns:
            bool: True if item was marked incomplete, False otherwise
        """
        target_list = None
        
        if list_name:
            target_list = self.lists.get(list_name)
        else:
            target_list = self.get_current_list()
        
        if target_list:
            # Convert from 1-based to 0-based index
            return target_list.uncomplete_item(index - 1)
        return False
    
    def remove_item(self, index: int, list_name: Optional[str] = None) -> bool:
        """
        Remove a todo item from a list
        
        Args:
            index (int): Index of the item (1-based for user interface)
            list_name (Optional[str]): Name of list (uses current if None)
            
        Returns:
            bool: True if item was removed, False otherwise
        """
        target_list = None
        
        if list_name:
            target_list = self.lists.get(list_name)
        else:
            target_list = self.get_current_list()
        
        if target_list:
            # Convert from 1-based to 0-based index
            return target_list.remove_item(index - 1)
        return False
    
    def save_data(self) -> bool:
        """
        Save all todo data to the JSON file
        
        Returns:
            bool: True if saved successfully, False otherwise
        """
        try:
            data = {
                'current_list_name': self.current_list_name,
                'lists': {name: todo_list.to_dict() for name, todo_list in self.lists.items()}
            }
            
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_data(self) -> bool:
        """
        Load todo data from the JSON file
        
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        if not os.path.exists(self.data_file):
            return False
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.current_list_name = data.get('current_list_name')
            self.lists = {}
            
            for name, list_data in data.get('lists', {}).items():
                self.lists[name] = TodoList.from_dict(list_data)
            
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def get_summary(self) -> str:
        """Get a summary of all todo lists"""
        if not self.lists:
            return "No todo lists found. Create your first list to get started!"
        
        output = ["=== Todo Lists Summary ===\n"]
        
        for name, todo_list in self.lists.items():
            stats = todo_list.get_item_count()
            current_marker = " (current)" if name == self.current_list_name else ""
            output.append(f"• {name}{current_marker}: {stats['completed']}/{stats['total']} completed")
        
        return "\n".join(output)
    
    def display_current_list(self, show_completed: bool = True) -> str:
        """Display the current todo list"""
        current_list = self.get_current_list()
        if current_list:
            return current_list.display(show_completed)
        else:
            return "No current list selected. Create a list or switch to an existing one."