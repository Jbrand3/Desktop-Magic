# Desktop-Magic
A lightweight Python GUI utility to dynamically categorize and archive scattered desktop files. 
# Desktop File Sorcery 🚀

A lightweight, local GUI desktop utility built in Python to dynamically isolate, categorize, and archive scattered structural files on native system desktops.

## 🛠️ Core Functionality
- **Dynamic Targeting:** Safely routes loose target extensions (`.py`, `.css`, `.png`, `.java`) via a native Tkinter interface.
- **Automated Directory Provisioning:** Checks for target destination folders and automatically creates them using `pathlib` safely without breaking path bounds.
- **Zero Dependencies:** Runs natively utilizing built-in Python standard libraries (`tkinter`, `shutil`, `os`).

## 💻 Tech Stack
- **Language:** Python 3.x
- **GUI Engine:** Tkinter / TTK
- **File System Architecture:** Pathlib & Shutil (Standard OS manipulation)

## 📈 Next Steps (Data Science Roadmap)
- [ ] **Smart Clustering:** Integrate a lightweight classification system to automatically categorize files based on file content/metadata rather than raw extension entry.
- [ ] **Data Pipeline Logs:** Append metadata logs to a local CSV database to analyze desktop file accumulation frequency and track storage consumption patterns.
