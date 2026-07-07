import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

def run_cleanup():
    ext_input = entry_ext.get().strip().lower()
    folder_input = entry_folder.get().strip()
    
    if not ext_input or not folder_input:
        messagebox.showerror("Error", "Please fill out both fields!")
        return
        
    # Format extension properly (e.g., 'py' becomes '.py')
    ext = f".{ext_input.replace('.', '')}"
    
    # Target User's Desktop
    desktop_path = Path.home() / "Desktop"
    target_dir = desktop_path / folder_input
    
    try:
        target_dir.mkdir(exist_ok=True)
        moved_count = 0
        
        # Scan and move matching loose files
        for item in desktop_path.iterdir():
            if item.is_file() and item.suffix.lower() == ext:
                shutil.move(str(item), str(target_dir / item.name))
                moved_count += 1
                
        messagebox.showinfo("Success", f"Cleaned up {moved_count} loose '{ext}' files!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {str(e)}")

# UI Setup
root = tk.Tk()
root.title("Desktop File Sorcery")
root.geometry("320x220")
root.resizable(False, False)

frame = ttk.Frame(root, padding="20")
frame.pack(fill="both", expand=True)

# Extension Input
ttk.Label(frame, text="File Extension to grab (e.g., py, png, css):").pack(anchor="w", pady=(0,2))
entry_ext = ttk.Entry(frame, width=30)
entry_ext.pack(fill="x", pady=(0,15))

# Target Folder Input
ttk.Label(frame, text="Name of New Destination Folder:").pack(anchor="w", pady=(0,2))
entry_folder = ttk.Entry(frame, width=30)
entry_folder.pack(fill="x", pady=(0,20))

# Execute Button
btn_run = ttk.Button(frame, text="🚀 Organize Desktop", command=run_cleanup)
btn_run.pack(fill="x")

root.mainloop()
