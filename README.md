# Task Manager - Command-Line Application

A simple command-line task manager for PhD students to manage homework and study tasks.

**University of Mohamed Kheider – Biskra**  
**Course:** Programming  
**Student:** PhD students: Mahdi Bentaleb - Lahcene Mamen 
**Academic Year:** 2025/2026

## Features

- ✅ Add new tasks with title and description
- ✅ View all tasks with status indicators
- ✅ Mark tasks as done
- ✅ Persistent storage using JSON file
- ✅ Error handling for invalid inputs
- ✅ Clean, readable code following PEP 8 standards

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Madiben/Programming-mini-project.git
cd Programming-mini-project
```

2. Ensure Python 3 is installed:
```bash
python --version
```

## Usage

### Running the Application

```bash
python tasks.py
```

### Menu Options

When you run the application, you'll see a menu with the following options:

1. **Add new task** - Create a new task with a title and optional description
2. **View all tasks** - Display all tasks with their status (done/pending)
3. **Mark task as done** - Mark a specific task as completed by entering its ID
4. **Exit** - Close the application

### Example Workflow

```
Welcome to Task Manager!
Info: tasks.json not found. Starting with empty task list.

======================================================================
TASK MANAGER - University of Mohamed Kheider, Biskra
======================================================================
1. Add new task
2. View all tasks
3. Mark task as done
4. Exit
======================================================================

Enter your choice (1-4): 1

--- Add New Task ---
Enter task title: Complete Python assignment
Enter task description (optional): Finish the task manager project
✓ Task added successfully! (ID: 1)
```

## File Structure

```
.
├── tasks.py          # Main application file
├── tasks.json        # JSON file for storing tasks (auto-created)
└── README.md         # This file
```

## JSON File Format

Tasks are stored in `tasks.json` with the following structure:

```json
[
  {
    "id": 1,
    "title": "Complete Python assignment",
    "description": "Finish the task manager project",
    "done": false,
    "created_at": "2026-02-18 10:30:00"
  }
]
```

## Error Handling

The application handles the following errors:

- Missing or corrupted `tasks.json` file
- Invalid JSON format
- Empty task titles
- Invalid task ID numbers
- Non-numeric input for task IDs

## Code Quality

This project follows Python best practices:

- ✅ PEP 8 compliant (verified with Flake8)
- ✅ Proper function documentation
- ✅ Error handling for edge cases
- ✅ Clean, readable code structure

## Testing with Flake8

To verify code quality:

```bash
pip install flake8
flake8 tasks.py
```

## Author

PhD Student Mahdi Bentaleb - University of Mohamed Kheider, Biskra
PhD Student Lahcene Mamen - University of Mohamed Kheider, Biskra

## License

This project is created for educational purposes as part of the Programming course.

