# Workflow Manager CLI Documentation

This document provides a comprehensive guide to the **Workflow Manager CLI** tool, including installation, commands, and functionality. This tool is designed to help users manage projects, workstreams, phases, and meetings through an interactive command-line interface.

---

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Commands](#commands)
4. [Functions](#functions)
5. [Example Usage](#example-usage)

---

## Installation

1. Clone the repository.
2. Install required libraries using:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the tool by executing the main Python file:
    ```bash
    python workflow_manager.py
    ```

---

## Usage

The Workflow Manager CLI uses a command-line interface to manage project workflows, including projects, workstreams, phases, and meetings. The tool supports various commands, which can be used to create, view, and export project structures.

To start the CLI, enter:
```bash
python workflow_manager.py
```

---

## Commands

### General Commands
- `help`: Display a help table listing all available commands.
- `show-info`: Display information about a specific project, including workstreams, phases, and meetings.
- `show-structure`: Display the hierarchical structure of a project.

### Project Management Commands
- `new-project`: Create a new project with a specified name.
- `new-workstream`: Add a workstream to an existing project.
- `new-phase`: Add a phase within a specified workstream of a project.
- `new-meeting`: Schedule a meeting within a specified phase of a workstream.

### Import and Export Commands
- `import`: Import a project structure from a CSV file.
- `export`: Export project details to a CSV file for documentation and sharing.

---

## Functions

Below is a detailed breakdown of each function within the Workflow Manager CLI.

### 1. **`check_directory_exists(directory_name: str) -> bool`**
   - Checks if the specified directory exists.
   - **Parameters**: `directory_name` (str): Name of the directory.
   - **Returns**: `True` if directory exists, `False` otherwise.

### 2. **`print_error(message: str) -> None`**
   - Prints an error message in bold red format.
   - **Parameters**: `message` (str): Error message to display.

### 3. **`print_dir_error() -> None`**
   - Prints a default error message if a directory is not found.

### 4. **`inputGetter()`**
   - Captures user input, splits it into command and arguments, and calls the corresponding function.
   - Available commands include `help`, `new-project`, `new-workstream`, `new-phase`, `new-meeting`, `show-info`, `export`, `import`, `show-structure`.

### 5. **`display_help() -> None`**
   - Displays the help table with all available commands and their descriptions.

### 6. **`createProject(project_name: str) -> None`**
   - Creates a directory with the specified project name.

### 7. **`createWorkstream(workstream_name: str, project_name: str) -> None`**
   - Creates a workstream folder inside the specified project directory.
   - **Parameters**:
     - `workstream_name` (str): Name of the workstream.
     - `project_name` (str): Name of the project.

### 8. **`createPhase(phase_name: str, workstream_name: str, project_name: str) -> None`**
   - Creates a phase folder within a specified workstream directory.
   - **Parameters**:
     - `phase_name` (str): Name of the phase.
     - `workstream_name` (str): Name of the workstream.
     - `project_name` (str): Name of the project.

### 9. **`createMeeting(meeting_date: str, attendees: list[str], phase_name: str, workstream_name: str, project_name: str) -> None`**
   - Creates a meeting file within a specified phase and workstream, including attendees' names and a section for notes.
   - **Parameters**:
     - `meeting_date` (str): Date of the meeting.
     - `attendees` (list): List of attendee names.
     - `phase_name`, `workstream_name`, `project_name`: Hierarchical names.

### 10. **`showInfo(project_name: str) -> dict`**
   - Displays and returns a summary table with details on meetings, phases, workstreams, and attendees within the project.
   - **Returns**: A dictionary of meetings and their associated details.

### 11. **`display_tree_structure(directory: str, tree: Optional[Tree] = None) -> Tree`**
   - Recursively traverses project folders, creating a visual tree structure of the project.
   - **Parameters**:
     - `directory` (str): The root directory to display.
     - `tree` (Tree): The tree object for displaying hierarchy.

### 12. **`createCSV(payload: dict, project_name: str) -> None`**
   - Exports the project details to a CSV file.
   - **Parameters**:
     - `payload` (dict): Dictionary containing project data.
     - `project_name` (str): Name of the project for naming the file.

### 13. **`importCSV(file: str) -> None`**
   - Imports project structure and details from a CSV file, creating directories and files as needed.
   - **Parameters**:
     - `file` (str): Name of the CSV file.

### 14. **`main()`**
   - Initializes the Workflow Manager CLI, clears the console, and displays the welcome screen.

---

## Example Usage

1. **Starting the CLI**:
   ```bash
   python workflow_manager.py
   ```

2. **Creating a New Project**:
   - Command: `new-project`
   - Follow prompts to enter the project name.

3. **Adding Workstreams, Phases, and Meetings**:
   - Command: `new-workstream`, `new-phase`, `new-meeting`
   - Follow prompts to specify names and dates.

4. **Viewing Project Information**:
   - Command: `show-info`
   - Displays detailed tables with all meetings, attendees, phases, and workstreams.

5. **Exporting Project to CSV**:
   - Command: `export`
   - Choose the project name, and a CSV file will be generated with all details.

6. **Importing Project from CSV**:
   - Command: `import`
   - Specify the CSV file name, and the project structure will be recreated.

---
- Auto Generated by Copilot

