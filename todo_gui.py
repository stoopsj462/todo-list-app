"""
Modern GUI version of the Todo List App using tkinter with custom styling
"""
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from todo_app import TodoApp
from datetime import datetime
import platform


class ModernTheme:
    """Modern color theme configuration"""
    # Light theme colors
    LIGHT = {
        'bg_primary': '#FFFFFF',        # Main background
        'bg_secondary': '#F8FAFC',      # Secondary background
        'bg_card': '#FFFFFF',           # Card background
        'bg_hover': '#F1F5F9',          # Hover background
        'bg_active': '#E2E8F0',         # Active background
        'text_primary': '#1E293B',      # Primary text
        'text_secondary': '#64748B',    # Secondary text
        'text_muted': '#94A3B8',        # Muted text
        'accent_primary': '#3B82F6',    # Primary accent (blue)
        'accent_success': '#10B981',    # Success color (green)
        'accent_warning': '#F59E0B',    # Warning color (amber)
        'accent_error': '#EF4444',      # Error color (red)
        'border_light': '#E2E8F0',      # Light border
        'border_medium': '#CBD5E1',     # Medium border
        'shadow': '#00000010',          # Subtle shadow
    }
    
    # Dark theme colors
    DARK = {
        'bg_primary': '#0F172A',        # Main background
        'bg_secondary': '#1E293B',      # Secondary background
        'bg_card': '#334155',           # Card background
        'bg_hover': '#475569',          # Hover background
        'bg_active': '#64748B',         # Active background
        'text_primary': '#F1F5F9',      # Primary text
        'text_secondary': '#CBD5E1',    # Secondary text
        'text_muted': '#94A3B8',        # Muted text
        'accent_primary': '#60A5FA',    # Primary accent (blue)
        'accent_success': '#34D399',    # Success color (green)
        'accent_warning': '#FBBF24',    # Warning color (amber)
        'accent_error': '#F87171',      # Error color (red)
        'border_light': '#475569',      # Light border
        'border_medium': '#64748B',     # Medium border
        'shadow': '#00000040',          # Darker shadow
    }


class TodoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Todo List App")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        
        # Theme management
        self.is_dark_mode = False
        self.current_theme = ModernTheme.LIGHT
        
        # Configure window
        self.setup_window_styling()
        
        # Initialize the todo app - use Desktop location for consistency
        desktop_path = r"C:\Users\stoop\OneDrive\Desktop\todo_data.json"
        self.app = TodoApp(desktop_path)
        
        # Setup custom styling before UI
        self.setup_custom_styles()
        
        self.setup_ui()
        self.refresh_display()
    
    def setup_window_styling(self):
        """Configure modern window styling"""
        self.root.configure(bg=self.current_theme['bg_primary'])
        
        # Try to set window icon (optional - will fail gracefully if no icon)
        try:
            # You can add an icon file later if desired
            pass
        except:
            pass
    
    def setup_custom_styles(self):
        """Setup modern custom ttk styles"""
        style = ttk.Style()
        
        # Use a theme that supports better customization
        try:
            style.theme_use('clam')  # Better base theme for customization
        except:
            pass  # Fall back to default theme
        
        # Configure modern button style
        style.configure('Modern.TButton',
                       background=self.current_theme['accent_primary'],
                       foreground='white',
                       borderwidth=1,
                       relief='solid',
                       focuscolor='none',
                       padding=(12, 6),
                       font=('Segoe UI', 9, 'normal'))
        
        style.map('Modern.TButton',
                 background=[('active', '#2563EB'), ('pressed', '#1D4ED8')],
                 foreground=[('active', 'white'), ('pressed', 'white')],
                 bordercolor=[('active', '#1E40AF')])
        
        # Configure success button style
        style.configure('Success.TButton',
                       background='#059669',
                       foreground='white',
                       borderwidth=1,
                       relief='solid',
                       focuscolor='none',
                       padding=(12, 6),
                       font=('Segoe UI', 9, 'normal'))
        
        style.map('Success.TButton',
                 background=[('active', '#047857'), ('pressed', '#065F46')],
                 foreground=[('active', 'white'), ('pressed', 'white')])
        
        # Configure warning button style
        style.configure('Warning.TButton',
                       background='#D97706',
                       foreground='white',
                       borderwidth=1,
                       relief='solid',
                       focuscolor='none',
                       padding=(12, 6),
                       font=('Segoe UI', 9, 'normal'))
        
        style.map('Warning.TButton',
                 background=[('active', '#B45309'), ('pressed', '#92400E')],
                 foreground=[('active', 'white'), ('pressed', 'white')])
        
        # Configure danger button style
        style.configure('Danger.TButton',
                       background='#DC2626',
                       foreground='white',
                       borderwidth=1,
                       relief='solid',
                       focuscolor='none',
                       padding=(12, 6),
                       font=('Segoe UI', 9, 'normal'))
        
        style.map('Danger.TButton',
                 background=[('active', '#B91C1C'), ('pressed', '#991B1B')],
                 foreground=[('active', 'white'), ('pressed', 'white')])
        
        # Configure modern frame style
        style.configure('Card.TFrame',
                       background=self.current_theme['bg_card'],
                       borderwidth=1,
                       relief='solid',
                       bordercolor=self.current_theme['border_light'])
        
        # Configure modern label frame
        style.configure('Modern.TLabelframe',
                       background=self.current_theme['bg_card'],
                       borderwidth=1,
                       relief='solid',
                       bordercolor=self.current_theme['border_light'])
        
        # Configure modern label frame label
        style.configure('Modern.TLabelframe.Label',
                       background=self.current_theme['bg_card'],
                       foreground=self.current_theme['text_primary'],
                       font=('Segoe UI', 10, 'bold'))
        
        # Configure modern entry style
        style.configure('Modern.TEntry',
                       fieldbackground=self.current_theme['bg_secondary'],
                       foreground=self.current_theme['text_primary'],
                       borderwidth=1,
                       relief='solid',
                       bordercolor=self.current_theme['border_medium'],
                       insertcolor=self.current_theme['text_primary'],
                       padding=8,
                       font=('Segoe UI', 10))
        
        # Configure modern combobox style
        style.configure('Modern.TCombobox',
                       fieldbackground=self.current_theme['bg_secondary'],
                       foreground=self.current_theme['text_primary'],
                       borderwidth=1,
                       relief='solid',
                       bordercolor=self.current_theme['border_medium'],
                       padding=8,
                       font=('Segoe UI', 10))
        
        # Configure modern treeview styles
        style.configure('Modern.Treeview',
                       background=self.current_theme['bg_card'],
                       foreground=self.current_theme['text_primary'],
                       fieldbackground=self.current_theme['bg_card'],
                       borderwidth=1,
                       relief='solid')
        
        style.configure('Modern.Treeview.Heading',
                       background=self.current_theme['bg_secondary'],
                       foreground=self.current_theme['text_primary'],
                       borderwidth=1,
                       relief='solid',
                       font=('Segoe UI', 9, 'bold'))
        
        style.map('Modern.Treeview',
                 background=[('selected', self.current_theme['accent_primary']),
                           ('focus', self.current_theme['bg_hover'])],
                 foreground=[('selected', 'white')])
        
        style.map('Modern.Treeview.Heading',
                 background=[('active', self.current_theme['bg_hover'])])
    
    def setup_ui(self):
        """Set up the modern user interface"""
        
        # Main container
        main_container = tk.Frame(self.root, bg=self.current_theme['bg_primary'])
        main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header section
        header_frame = tk.Frame(main_container, bg=self.current_theme['bg_primary'])
        header_frame.pack(fill='x', pady=(0, 20))
        
        # Title with modern typography
        title_frame = tk.Frame(header_frame, bg=self.current_theme['bg_primary'])
        title_frame.pack(side='left')
        
        title_label = tk.Label(title_frame, 
                             text="✨ Todo List App", 
                             font=('Segoe UI', 24, 'bold'),
                             fg=self.current_theme['text_primary'],
                             bg=self.current_theme['bg_primary'])
        title_label.pack(anchor='w')
        
        subtitle_label = tk.Label(title_frame,
                                text="Organize your tasks with style",
                                font=('Segoe UI', 11),
                                fg=self.current_theme['text_secondary'],
                                bg=self.current_theme['bg_primary'])
        subtitle_label.pack(anchor='w')
        
        # Theme toggle button in header
        theme_frame = tk.Frame(header_frame, bg=self.current_theme['bg_primary'])
        theme_frame.pack(side='right')
        
        self.theme_button = ttk.Button(theme_frame, text="🌙 Dark Mode", command=self.toggle_theme,
                                     style='Modern.TButton')
        self.theme_button.pack()
        
        # List management card
        list_card = tk.Frame(main_container, bg=self.current_theme['bg_card'], 
                           relief='solid', bd=1, highlightbackground=self.current_theme['border_light'])
        list_card.pack(fill='x', pady=(0, 15))
        
        list_inner = tk.Frame(list_card, bg=self.current_theme['bg_card'])
        list_inner.pack(fill='x', padx=20, pady=15)
        
        # List management title
        list_title = tk.Label(list_inner, text="📋 List Management", 
                            font=('Segoe UI', 12, 'bold'),
                            fg=self.current_theme['text_primary'],
                            bg=self.current_theme['bg_card'])
        list_title.pack(anchor='w', pady=(0, 10))
        
        # List controls frame
        list_controls = tk.Frame(list_inner, bg=self.current_theme['bg_card'])
        list_controls.pack(fill='x')
        
        # List selection
        select_frame = tk.Frame(list_controls, bg=self.current_theme['bg_card'])
        select_frame.pack(side='left', fill='x', expand=True)
        
        tk.Label(select_frame, text="Current List:", 
               font=('Segoe UI', 10),
               fg=self.current_theme['text_secondary'],
               bg=self.current_theme['bg_card']).pack(side='left', padx=(0, 10))
        
        self.list_var = tk.StringVar()
        self.list_combo = ttk.Combobox(select_frame, textvariable=self.list_var, 
                                     state="readonly", style='Modern.TCombobox',
                                     font=('Segoe UI', 10))
        self.list_combo.pack(side='left', fill='x', expand=True, padx=(0, 15))
        self.list_combo.bind("<<ComboboxSelected>>", self.on_list_changed)
        
        # List buttons
        buttons_frame = tk.Frame(list_controls, bg=self.current_theme['bg_card'])
        buttons_frame.pack(side='right')
        
        ttk.Button(buttons_frame, text="➕ New List", command=self.new_list,
                  style='Modern.TButton').pack(side='left', padx=(0, 10))
        ttk.Button(buttons_frame, text="🗑️ Delete List", command=self.delete_list,
                  style='Danger.TButton').pack(side='left')
        
        # Main content area
        content_container = tk.Frame(main_container, bg=self.current_theme['bg_primary'])
        content_container.pack(fill='both', expand=True)
        
        # Left panel - Todo items
        left_panel = tk.Frame(content_container, bg=self.current_theme['bg_card'],
                            relief='solid', bd=1, highlightbackground=self.current_theme['border_light'])
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        left_inner = tk.Frame(left_panel, bg=self.current_theme['bg_card'])
        left_inner.pack(fill='both', expand=True, padx=20, pady=15)
        
        # Todo items section title
        items_title = tk.Label(left_inner, text="📝 Todo Items", 
                             font=('Segoe UI', 12, 'bold'),
                             fg=self.current_theme['text_primary'],
                             bg=self.current_theme['bg_card'])
        items_title.pack(anchor='w', pady=(0, 15))
        
        # Add item section
        add_section = tk.Frame(left_inner, bg=self.current_theme['bg_secondary'],
                             relief='solid', bd=1, highlightbackground=self.current_theme['border_light'])
        add_section.pack(fill='x', pady=(0, 15))
        
        add_inner = tk.Frame(add_section, bg=self.current_theme['bg_secondary'])
        add_inner.pack(fill='x', padx=15, pady=12)
        
        add_label = tk.Label(add_inner, text="Add new task:", 
                           font=('Segoe UI', 9),
                           fg=self.current_theme['text_secondary'],
                           bg=self.current_theme['bg_secondary'])
        add_label.pack(anchor='w', pady=(0, 5))
        
        add_controls = tk.Frame(add_inner, bg=self.current_theme['bg_secondary'])
        add_controls.pack(fill='x')
        
        self.new_item_var = tk.StringVar()
        self.new_item_entry = ttk.Entry(add_controls, textvariable=self.new_item_var, 
                                      font=('Segoe UI', 10), style='Modern.TEntry')
        self.new_item_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
        self.new_item_entry.bind("<Return>", lambda e: self.add_item())
        
        ttk.Button(add_controls, text="➕ Add Task", command=self.add_item,
                  style='Success.TButton').pack(side='right')
        
        # Items treeview container
        tree_container = tk.Frame(left_inner, bg=self.current_theme['bg_card'])
        tree_container.pack(fill='both', expand=True)
        
        # Items treeview with modern styling
        columns = ("Status", "Item", "Completed Date")
        self.tree = ttk.Treeview(tree_container, columns=columns, show="tree headings", 
                               height=15, selectmode='browse', style='Modern.Treeview')
        self.tree.pack(side='left', fill='both', expand=True)
        
        # Configure columns with modern headers
        self.tree.heading("#0", text="")
        self.tree.column("#0", width=40, minwidth=40)
        self.tree.heading("Status", text="✓")
        self.tree.column("Status", width=50, minwidth=50, anchor='center')
        self.tree.heading("Item", text="Task Description")
        self.tree.column("Item", width=400, minwidth=200)
        self.tree.heading("Completed Date", text="Completed")
        self.tree.column("Completed Date", width=140, minwidth=100, anchor='center')
        
        # Modern scrollbar for treeview
        scrollbar = ttk.Scrollbar(tree_container, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Add interactive effects
        self.tree.bind('<Motion>', self.on_tree_motion)
        self.tree.bind('<Button-1>', self.on_tree_click)
        self.tree.bind('<Double-1>', self.on_tree_double_click)
        
        # Right panel - Actions and Statistics
        right_panel = tk.Frame(content_container, bg=self.current_theme['bg_card'],
                             relief='solid', bd=1, highlightbackground=self.current_theme['border_light'])
        right_panel.pack(side='right', fill='y', padx=(10, 0))
        
        right_inner = tk.Frame(right_panel, bg=self.current_theme['bg_card'])
        right_inner.pack(fill='both', expand=True, padx=20, pady=15)
        
        # Actions section title
        actions_title = tk.Label(right_inner, text="⚡ Actions", 
                               font=('Segoe UI', 12, 'bold'),
                               fg=self.current_theme['text_primary'],
                               bg=self.current_theme['bg_card'])
        actions_title.pack(anchor='w', pady=(0, 15))
        
        # Action buttons with modern styling
        buttons_container = tk.Frame(right_inner, bg=self.current_theme['bg_card'])
        buttons_container.pack(fill='x', pady=(0, 20))
        
        ttk.Button(buttons_container, text="✅ Complete Task", command=self.complete_item, 
                  style='Success.TButton', width=18).pack(fill='x', pady=3)
        ttk.Button(buttons_container, text="↩️ Mark Incomplete", command=self.uncomplete_item, 
                  style='Warning.TButton', width=18).pack(fill='x', pady=3)
        ttk.Button(buttons_container, text="🗑️ Remove Task", command=self.remove_item, 
                  style='Danger.TButton', width=18).pack(fill='x', pady=3)
        
        # Separator
        separator = tk.Frame(right_inner, bg=self.current_theme['border_light'], height=1)
        separator.pack(fill='x', pady=15)
        
        # Additional buttons container
        utility_buttons = tk.Frame(right_inner, bg=self.current_theme['bg_card'])
        utility_buttons.pack(fill='x', pady=(0, 20))
        
        ttk.Button(utility_buttons, text="🔄 Refresh View", command=self.refresh_display, 
                  style='Modern.TButton', width=18).pack(fill='x', pady=3)
        ttk.Button(utility_buttons, text="💾 Save Data", command=self.save_data, 
                  style='Modern.TButton', width=18).pack(fill='x', pady=3)
        
        # Statistics card
        stats_card = tk.Frame(right_inner, bg=self.current_theme['bg_secondary'],
                            relief='solid', bd=1, highlightbackground=self.current_theme['border_light'])
        stats_card.pack(fill='x', pady=(10, 0))
        
        stats_inner = tk.Frame(stats_card, bg=self.current_theme['bg_secondary'])
        stats_inner.pack(fill='x', padx=15, pady=12)
        
        stats_title = tk.Label(stats_inner, text="📊 Statistics", 
                             font=('Segoe UI', 10, 'bold'),
                             fg=self.current_theme['text_primary'],
                             bg=self.current_theme['bg_secondary'])
        stats_title.pack(anchor='w', pady=(0, 8))
        
        self.stats_label = tk.Label(stats_inner, text="No list selected", 
                                  font=('Segoe UI', 9),
                                  fg=self.current_theme['text_secondary'],
                                  bg=self.current_theme['bg_secondary'])
        self.stats_label.pack(anchor='w')
        
        # Modern status bar
        self.status_var = tk.StringVar()
        self.status_var.set("✨ Ready - Welcome to your modern todo list!")
        status_bar = tk.Frame(main_container, bg=self.current_theme['bg_secondary'], height=30)
        status_bar.pack(fill='x', pady=(15, 0))
        
        status_label = tk.Label(status_bar, textvariable=self.status_var, 
                              font=('Segoe UI', 9),
                              fg=self.current_theme['text_secondary'],
                              bg=self.current_theme['bg_secondary'],
                              anchor='w')
        status_label.pack(side='left', padx=15, pady=8)
    
    def toggle_theme(self):
        """Toggle between light and dark themes"""
        self.is_dark_mode = not self.is_dark_mode
        self.current_theme = ModernTheme.DARK if self.is_dark_mode else ModernTheme.LIGHT
        
        # Update theme button text
        self.theme_button.configure(text="☀️ Light Mode" if self.is_dark_mode else "🌙 Dark Mode")
        
        # Recreate the UI with new theme
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.setup_custom_styles()
        self.setup_ui()
        self.refresh_display()
        
        theme_name = "Dark" if self.is_dark_mode else "Light"
        self.status_var.set(f"🎨 Switched to {theme_name} mode")
    
    def on_tree_motion(self, event):
        """Handle mouse motion over treeview for hover effects"""
        item = self.tree.identify_row(event.y)
        if item:
            # Update status to show item preview on hover
            item_values = self.tree.item(item, 'values')
            if len(item_values) >= 2:
                task_text = item_values[1]
                self.status_var.set(f"📋 Hover: {task_text[:50]}...")
    
    def on_tree_click(self, event):
        """Handle single click on treeview"""
        item = self.tree.identify_row(event.y)
        if item:
            item_values = self.tree.item(item, 'values')
            if len(item_values) >= 2:
                task_text = item_values[1]
                self.status_var.set(f"✨ Selected: {task_text}")
    
    def on_tree_double_click(self, event):
        """Handle double click to quickly complete/uncomplete items"""
        index = self.get_selected_item_index()
        if index is None:
            return
        
        current_list = self.app.get_current_list()
        if current_list and index <= len(current_list.items):
            item = current_list.items[index-1]
            if item.completed:
                self.uncomplete_item()
            else:
                self.complete_item()
    
    def refresh_display(self):
        """Refresh all displays"""
        self.refresh_lists()
        self.refresh_items()
        self.refresh_stats()
    
    def refresh_lists(self):
        """Refresh the list combo box"""
        lists = self.app.get_list_names()
        self.list_combo['values'] = lists
        
        if self.app.current_list_name:
            self.list_var.set(self.app.current_list_name)
        elif lists:
            self.list_var.set(lists[0])
            self.app.switch_list(lists[0])
        else:
            self.list_var.set("")
    
    def refresh_items(self):
        """Refresh the items tree view with modern styling"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        current_list = self.app.get_current_list()
        if current_list:
            for i, item in enumerate(current_list.items):
                # Modern status indicators
                if item.completed:
                    status = "✅"
                    item_text = f"✓ {item.title}"
                else:
                    status = "⭕"
                    item_text = item.title
                
                completed_date = item.completion_date if item.completed else ""
                
                # Insert item with enhanced formatting
                item_id = self.tree.insert("", "end", text=f"#{i+1:02d}", 
                                         values=(status, item_text, completed_date))
                
                # Apply tags for completed items (for future styling)
                if item.completed:
                    self.tree.set(item_id, "Status", "✅")
                    # Could add tags here for different styling if needed
                    # self.tree.item(item_id, tags=['completed'])
    
    def refresh_stats(self):
        """Refresh the statistics display with modern formatting"""
        current_list = self.app.get_current_list()
        if current_list:
            stats = current_list.get_item_count()
            
            # Calculate completion percentage
            if stats['total'] > 0:
                completion_rate = (stats['completed'] / stats['total']) * 100
                progress_bar = "█" * int(completion_rate / 10) + "░" * (10 - int(completion_rate / 10))
                
                stats_text = (f"📊 Total Tasks: {stats['total']}\n"
                            f"✅ Completed: {stats['completed']}\n"
                            f"⏳ Pending: {stats['pending']}\n"
                            f"📈 Progress: {completion_rate:.1f}%\n"
                            f"{progress_bar}")
            else:
                stats_text = "📝 No tasks yet\nCreate your first task!"
                
            self.stats_label.config(text=stats_text)
        else:
            self.stats_label.config(text="🔍 No list selected\nSelect or create a list to start")
    
    def on_list_changed(self, event=None):
        """Handle list selection change"""
        selected_list = self.list_var.get()
        if selected_list:
            self.app.switch_list(selected_list)
            self.refresh_items()
            self.refresh_stats()
            self.status_var.set(f"📂 Switched to list: {selected_list}")
    
    def new_list(self):
        """Create a new todo list"""
        name = simpledialog.askstring("New List", "Enter list name:")
        if name:
            if self.app.create_list(name):
                self.refresh_display()
                self.status_var.set(f"🎉 Created new list: {name}")
            else:
                messagebox.showerror("Error", f"List '{name}' already exists!")
    
    def delete_list(self):
        """Delete the current list"""
        current_list_name = self.app.current_list_name
        if not current_list_name:
            messagebox.showwarning("Warning", "No list selected!")
            return
        
        current_list = self.app.get_current_list()
        stats = current_list.get_item_count()
        
        if messagebox.askyesno("Confirm Delete", 
                              f"Delete list '{current_list_name}' with {stats['total']} items?"):
            if self.app.delete_list(current_list_name):
                self.refresh_display()
                self.status_var.set(f"🗑️ Deleted list: {current_list_name}")
            else:
                messagebox.showerror("Error", "Failed to delete list!")
    
    def add_item(self):
        """Add a new item to the current list"""
        title = self.new_item_var.get().strip()
        if not title:
            return
        
        if not self.app.get_current_list():
            messagebox.showwarning("Warning", "No list selected! Create a list first.")
            return
        
        if self.app.add_item(title):
            self.new_item_var.set("")
            self.refresh_items()
            self.refresh_stats()
            self.status_var.set(f"➕ Added task: {title}")
        else:
            messagebox.showerror("Error", "Failed to add item!")
    
    def get_selected_item_index(self):
        """Get the index of the selected item"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an item first!")
            return None
        
        item = self.tree.item(selection[0])
        try:
            # Extract number from text like "#01", "#02", etc.
            text = item['text']
            if text.startswith('#'):
                return int(text[1:])
            else:
                return int(text)
        except (ValueError, KeyError):
            return None
    
    def complete_item(self):
        """Mark the selected item as complete"""
        index = self.get_selected_item_index()
        if index is None:
            return
        
        if self.app.complete_item(index):
            self.refresh_items()
            self.refresh_stats()
            self.status_var.set(f"🎊 Completed task #{index}! Great job!")
        else:
            messagebox.showerror("Error", "Failed to complete item!")
    
    def uncomplete_item(self):
        """Mark the selected item as incomplete"""
        index = self.get_selected_item_index()
        if index is None:
            return
        
        if self.app.uncomplete_item(index):
            self.refresh_items()
            self.refresh_stats()
            self.status_var.set(f"↩️ Marked task #{index} as incomplete")
        else:
            messagebox.showerror("Error", "Failed to mark item as incomplete!")
    
    def remove_item(self):
        """Remove the selected item"""
        index = self.get_selected_item_index()
        if index is None:
            return
        
        current_list = self.app.get_current_list()
        if index <= len(current_list.items):
            item_title = current_list.items[index-1].title
            
            if messagebox.askyesno("Confirm Remove", f"Remove item: {item_title}?"):
                if self.app.remove_item(index):
                    self.refresh_items()
                    self.refresh_stats()
                    self.status_var.set(f"🗑️ Removed task: {item_title}")
                else:
                    messagebox.showerror("Error", "Failed to remove item!")
    
    def save_data(self):
        """Save data manually"""
        if self.app.save_data():
            self.status_var.set("💾 Data saved successfully!")
        else:
            messagebox.showerror("Error", "Failed to save data!")
    
    def on_closing(self):
        """Handle window closing"""
        self.app.save_data()
        self.root.destroy()


def main():
    """Main function to run the GUI"""
    root = tk.Tk()
    app = TodoGUI(root)
    
    # Handle window closing
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    # Start the GUI
    root.mainloop()


if __name__ == "__main__":
    main()