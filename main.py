"""
Command Line Interface for the Todo List App
"""
import sys
from todo_app import TodoApp


class TodoCLI:
    """Command line interface for the Todo App"""
    
    def __init__(self):
        # Use Desktop location for consistency across all versions
        desktop_path = r"C:\Users\stoop\OneDrive\Desktop\todo_data.json"
        self.app = TodoApp(desktop_path)
        self.running = True
    
    def display_help(self):
        """Display help information"""
        help_text = """
=== Todo List App Commands ===

List Management:
  lists                 - Show all lists
  create <name>         - Create a new list
  switch <name>         - Switch to a list
  delete <name>         - Delete a list
  
Item Management:
  add <item>            - Add item to current list
  show                  - Show current list
  show all              - Show current list including completed items
  complete <number>     - Mark item as complete
  uncomplete <number>   - Mark item as incomplete
  remove <number>       - Remove item from list
  
Other:
  summary               - Show summary of all lists
  save                  - Save data to file
  help                  - Show this help
  exit/quit             - Exit the application

Examples:
  create Work
  switch Work
  add "Review project proposal"
  complete 1
        """
        print(help_text)
    
    def display_welcome(self):
        """Display welcome message"""
        print("\n🗂️  Welcome to your Todo List App!")
        print("Type 'help' for commands or 'exit' to quit")
        
        # Show summary if lists exist
        if self.app.lists:
            print("\n" + self.app.get_summary())
            current_list = self.app.get_current_list()
            if current_list:
                print(f"\nCurrent list: {current_list.name}")
        else:
            print("\n💡 Start by creating your first list with: create <name>")
    
    def process_command(self, command_line: str) -> bool:
        """
        Process a command from the user
        
        Args:
            command_line (str): The full command line entered by user
            
        Returns:
            bool: True to continue running, False to exit
        """
        parts = command_line.strip().split()
        if not parts:
            return True
        
        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        # Exit commands
        if command in ['exit', 'quit', 'q']:
            self.app.save_data()
            print("👋 Goodbye! Your data has been saved.")
            return False
        
        # Help
        elif command in ['help', 'h', '?']:
            self.display_help()
        
        # List management
        elif command == 'lists':
            self.cmd_lists()
        
        elif command == 'create':
            self.cmd_create(args)
        
        elif command == 'switch':
            self.cmd_switch(args)
        
        elif command == 'delete':
            self.cmd_delete(args)
        
        # Item management
        elif command == 'add':
            self.cmd_add(args)
        
        elif command == 'show':
            self.cmd_show(args)
        
        elif command in ['complete', 'done']:
            self.cmd_complete(args)
        
        elif command == 'uncomplete':
            self.cmd_uncomplete(args)
        
        elif command in ['remove', 'rm', 'delete']:
            self.cmd_remove(args)
        
        # Other commands
        elif command == 'summary':
            print("\n" + self.app.get_summary())
        
        elif command == 'save':
            if self.app.save_data():
                print("✅ Data saved successfully!")
            else:
                print("❌ Failed to save data.")
        
        else:
            print(f"❌ Unknown command: {command}. Type 'help' for available commands.")
        
        return True
    
    def cmd_lists(self):
        """Show all lists"""
        list_names = self.app.get_list_names()
        if not list_names:
            print("📝 No lists found. Create one with: create <name>")
            return
        
        print("\n📋 Your Lists:")
        for name in list_names:
            current_marker = " ← current" if name == self.app.current_list_name else ""
            stats = self.app.lists[name].get_item_count()
            print(f"  • {name}{current_marker} ({stats['completed']}/{stats['total']} completed)")
    
    def cmd_create(self, args):
        """Create a new list"""
        if not args:
            print("❌ Please provide a name for the list. Example: create Work")
            return
        
        name = " ".join(args)
        if self.app.create_list(name):
            print(f"✅ Created list '{name}' and switched to it.")
        else:
            print(f"❌ List '{name}' already exists.")
    
    def cmd_switch(self, args):
        """Switch to a different list"""
        if not args:
            print("❌ Please specify a list name. Example: switch Work")
            return
        
        name = " ".join(args)
        if self.app.switch_list(name):
            print(f"✅ Switched to list '{name}'")
        else:
            print(f"❌ List '{name}' not found.")
    
    def cmd_delete(self, args):
        """Delete a list"""
        if not args:
            print("❌ Please specify a list name. Example: delete Work")
            return
        
        name = " ".join(args)
        if name not in self.app.lists:
            print(f"❌ List '{name}' not found.")
            return
        
        # Confirm deletion
        stats = self.app.lists[name].get_item_count()
        confirm = input(f"⚠️  Delete list '{name}' with {stats['total']} items? (y/N): ")
        
        if confirm.lower() in ['y', 'yes']:
            if self.app.delete_list(name):
                print(f"✅ Deleted list '{name}'")
            else:
                print(f"❌ Failed to delete list '{name}'")
        else:
            print("❌ Deletion cancelled.")
    
    def cmd_add(self, args):
        """Add an item to the current list"""
        if not args:
            print("❌ Please provide a task description. Example: add Buy groceries")
            return
        
        current_list = self.app.get_current_list()
        if not current_list:
            print("❌ No current list. Create a list first with: create <name>")
            return
        
        title = " ".join(args)
        if self.app.add_item(title):
            print(f"✅ Added '{title}' to {current_list.name}")
        else:
            print("❌ Failed to add item.")
    
    def cmd_show(self, args):
        """Show the current list"""
        current_list = self.app.get_current_list()
        if not current_list:
            print("❌ No current list. Create a list first with: create <name>")
            return
        
        show_completed = len(args) > 0 and args[0].lower() == 'all'
        print(self.app.display_current_list(show_completed))
    
    def cmd_complete(self, args):
        """Mark an item as complete"""
        if not args:
            print("❌ Please provide an item number. Example: complete 1")
            return
        
        try:
            index = int(args[0])
            if self.app.complete_item(index):
                print(f"✅ Marked item #{index} as complete!")
            else:
                print(f"❌ Invalid item number: {index}")
        except ValueError:
            print("❌ Please provide a valid number.")
    
    def cmd_uncomplete(self, args):
        """Mark an item as incomplete"""
        if not args:
            print("❌ Please provide an item number. Example: uncomplete 1")
            return
        
        try:
            index = int(args[0])
            if self.app.uncomplete_item(index):
                print(f"✅ Marked item #{index} as incomplete.")
            else:
                print(f"❌ Invalid item number: {index}")
        except ValueError:
            print("❌ Please provide a valid number.")
    
    def cmd_remove(self, args):
        """Remove an item from the current list"""
        if not args:
            print("❌ Please provide an item number. Example: remove 1")
            return
        
        try:
            index = int(args[0])
            if self.app.remove_item(index):
                print(f"✅ Removed item #{index}")
            else:
                print(f"❌ Invalid item number: {index}")
        except ValueError:
            print("❌ Please provide a valid number.")
    
    def run(self):
        """Main application loop"""
        self.display_welcome()
        
        try:
            while self.running:
                try:
                    # Show current list indicator in prompt
                    current_list_name = self.app.current_list_name or "no list"
                    command = input(f"\n[{current_list_name}] > ").strip()
                    
                    if command:
                        self.running = self.process_command(command)
                    
                except KeyboardInterrupt:
                    print("\n\n👋 Goodbye! Use 'exit' to save your data next time.")
                    break
                except EOFError:
                    print("\n\n👋 Goodbye!")
                    break
                    
        finally:
            # Always try to save on exit
            self.app.save_data()


def main():
    """Entry point for the application"""
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        print("Todo List App - A simple command-line todo manager")
        print("Usage: python main.py")
        print("\nOnce running, type 'help' for available commands.")
        return
    
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()