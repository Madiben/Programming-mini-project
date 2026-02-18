"""
Task Manager - A command-line application for managing homework/study tasks
University of Mohamed Kheider - Biskra
Course: Programming (Mahdi Bentaleb - Lahcene Mamen)
Academic Year: 2025/2026
"""

import json
import os
from datetime import datetime


TASKS_FILE = "tasks.json"


def load_tasks():
    """
    Load tasks from JSON file.
    Returns empty list if file doesn't exist or is invalid.
    """
    if not os.path.exists(TASKS_FILE):
        print(f"Info: {TASKS_FILE} not found. Starting with empty task list.")
        return []

    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as file:
            tasks = json.load(file)
            if not isinstance(tasks, list):
                print("Error: Invalid tasks file format. Starting fresh.")
                return []
            return tasks
    except json.JSONDecodeError:
        print(f"Error: {TASKS_FILE} contains invalid JSON. Starting fresh.")
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []


def save_tasks(tasks):
    """
    Save tasks to JSON file.
    Returns True if successful, False otherwise.
    """
    try:
        with open(TASKS_FILE, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False


def add_task(tasks):
    """
    Add a new task to the task list.
    """
    print("\n--- Add New Task ---")
    title = input("Enter task title: ").strip()

    if not title:
        print("Error: Task title cannot be empty.")
        return

    description = input("Enter task description (optional): ").strip()

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(task)

    if save_tasks(tasks):
        print(f"✓ Task added successfully! (ID: {task['id']})")
    else:
        print("✗ Failed to save task.")


def list_tasks(tasks):
    """
    Display all tasks in a formatted list.
    """
    if not tasks:
        print("\nNo tasks found. Add your first task!")
        return

    print("\n" + "=" * 70)
    print("YOUR TASKS")
    print("=" * 70)

    for task in tasks:
        status = "✓" if task.get("done", False) else "○"
        task_id = task.get("id", "?")
        title = task.get("title", "Untitled")
        description = task.get("description", "")
        created = task.get("created_at", "Unknown")

        print(f"\n[{status}] Task #{task_id}: {title}")
        if description:
            print(f"    Description: {description}")
        print(f"    Created: {created}")

    print("\n" + "=" * 70)


def mark_done(tasks):
    """
    Mark a task as done.
    """
    if not tasks:
        print("\nNo tasks available to mark as done.")
        return

    print("\n--- Mark Task as Done ---")
    try:
        task_id = int(input("Enter task ID to mark as done: "))
    except ValueError:
        print("Error: Invalid task number. Please enter a number.")
        return

    # Find task by ID
    task_found = False
    for task in tasks:
        if task.get("id") == task_id:
            task_found = True
            if task.get("done", False):
                print(f"Task #{task_id} is already marked as done.")
            else:
                task["done"] = True
                task["completed_at"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                if save_tasks(tasks):
                    print(f"✓ Task #{task_id} marked as done!")
                else:
                    print("✗ Failed to save changes.")
            break

    if not task_found:
        print(f"Error: Task #{task_id} not found.")


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 70)
    print("TASK MANAGER - University of Mohamed Kheider, Biskra")
    print("=" * 70)
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Mark task as done")
    print("4. Exit")
    print("=" * 70)


def main():
    """Main function to run the task manager application."""
    print("\nWelcome to Task Manager!")
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            print("\nThank you for using Task Manager. Goodbye!")
            break
        else:
            msg = "Invalid choice. Please enter a number between 1-4."
            print(f"\nError: {msg}")


if __name__ == "__main__":
    main()
