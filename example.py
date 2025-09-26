"""
Example usage of the Todo List App
This file demonstrates how to use the TodoApp programmatically
"""

from todo_app import TodoApp
from datetime import datetime

def example_usage():
    """Demonstrate the todo app functionality"""
    
    print("🗂️  Todo List App - Example Usage")
    print("=" * 40)
    
    # Create the app instance
    app = TodoApp("example_data.json")
    
    # Create some lists
    print("\n📋 Creating Lists...")
    app.create_list("Work")
    app.create_list("Personal") 
    app.create_list("Shopping")
    
    print("Created lists:", app.get_list_names())
    
    # Add items to different lists
    print("\n📝 Adding Items...")
    
    # Add to Work list
    app.switch_list("Work")
    app.add_item("Review quarterly reports")
    app.add_item("Prepare presentation for Monday")
    app.add_item("Schedule team meeting")
    app.add_item("Update project timeline")
    
    # Add to Personal list
    app.switch_list("Personal")
    app.add_item("Call dentist for appointment")
    app.add_item("Pick up dry cleaning")
    app.add_item("Plan weekend trip")
    
    # Add to Shopping list
    app.switch_list("Shopping")
    app.add_item("Buy groceries")
    app.add_item("Get birthday gift for mom")
    app.add_item("Pick up prescription")
    
    # Show summary
    print("\n📊 Summary:")
    print(app.get_summary())
    
    # Complete some items
    print("\n✅ Completing Some Tasks...")
    
    # Complete work items
    app.switch_list("Work")
    app.complete_item(2)  # Prepare presentation
    app.complete_item(3)  # Schedule team meeting
    
    # Complete personal items
    app.switch_list("Personal") 
    app.complete_item(1)  # Call dentist
    
    # Complete shopping items
    app.switch_list("Shopping")
    app.complete_item(1)  # Buy groceries
    app.complete_item(3)  # Pick up prescription
    
    # Show each list
    print("\n📋 Work List:")
    app.switch_list("Work")
    print(app.display_current_list())
    
    print("\n📋 Personal List:")
    app.switch_list("Personal")
    print(app.display_current_list())
    
    print("\n📋 Shopping List:")
    app.switch_list("Shopping")
    print(app.display_current_list())
    
    # Show final summary
    print("\n📊 Final Summary:")
    print(app.get_summary())
    
    # Save the data
    print("\n💾 Saving Data...")
    if app.save_data():
        print("✅ Data saved to example_data.json")
    else:
        print("❌ Failed to save data")
    
    # Demonstrate loading
    print("\n📂 Testing Data Persistence...")
    new_app = TodoApp("example_data.json")
    print("Loaded lists:", new_app.get_list_names())
    print("Current list:", new_app.current_list_name)
    
    return app

def demonstrate_individual_classes():
    """Show how individual classes work"""
    
    print("\n\n🧩 Individual Class Examples")
    print("=" * 40)
    
    # TodoItem examples
    print("\n📌 TodoItem Examples:")
    from todo_item import TodoItem
    
    item1 = TodoItem("Learn Python")
    print(f"New item: {item1}")
    
    item1.mark_complete()
    print(f"After completion: {item1}")
    
    item1.mark_incomplete()
    print(f"After marking incomplete: {item1}")
    
    # TodoList examples  
    print("\n📝 TodoList Examples:")
    from todo_list import TodoList
    
    my_list = TodoList("Learning Goals")
    my_list.add_item("Learn Python basics")
    my_list.add_item("Build a project") 
    my_list.add_item("Deploy to production")
    
    print(my_list.display(show_completed=False))
    
    # Complete middle item
    my_list.complete_item(1)  # 0-based index
    print("After completing item 2:")
    print(my_list.display())
    
    stats = my_list.get_item_count()
    print(f"Statistics: {stats}")

if __name__ == "__main__":
    # Run the main example
    app = example_usage()
    
    # Run individual class examples
    demonstrate_individual_classes()
    
    print("\n\n🎉 Example completed! Check out the main.py file to use the interactive CLI.")