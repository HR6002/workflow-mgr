import os
import csv
import art
import time
from rich.console import Console
from rich.table import Table
from rich.box import ROUNDED
from rich.tree import Tree
from rich import print
console = Console()
#Imports the necessary lib

#checks if a directory exists
def check_directory_exists(directory_name:str)->bool:
    return os.path.isdir(directory_name)

#prints given error msg in good format 
def print_error(message:str)->None:
    console.print(f"[bold red]Error:[/bold red] {message}")

#prints common error msg of directory not existig
#TODO include this in the check_directory_exist func makes it more efficient
def print_dir_error():
    console.print(f"[bold red]Error:[/bold red] Direcotry Does not exist")

#Gets the input and validates teh input and calls the necessary functions
def inputGetter():
    usr_input = console.input(prompt='[bold blue]WorkFlow-Mgr >[/] ')
    user_input_args = usr_input.rsplit(' ')
    user_command = user_input_args[0] #splits the user input for easier handling
    if user_command == 'help':
        display_help() 

    elif user_command == 'new-project':
        project_name = console.input(prompt='   [purple]Project Name: [/] ')
        createProject(project_name)

    elif user_command == 'new-workstream':
        project_name = console.input(prompt='   [purple]Project Name: [/] ')
        if check_directory_exists(project_name):
            console.print("Enter Workstream Name, enter 'finish' to finish ")
            while True:
                workstream_name = console.input(prompt=f'[bold blue]WorkFlow-Mgr/{project_name} >[/]   [purple]Workstream Name: [/] ')
                if workstream_name =='finish':
                    break
                else:
                    createWorkstream(workstream_name, project_name)
        else:
            print_dir_error()

    elif user_command == 'new-phase':
        project_name = console.input(prompt='   [purple]Project Name: [/] ')
        if check_directory_exists(project_name):
            workstream_name = console.input(prompt='   [purple]Workstream Name: [/] ')
            if check_directory_exists(f'{project_name}/{workstream_name}'):
                console.print("Enter Phase Name, enter 'finish' to finish ")
                while True:
                    phase_name = console.input(prompt=f'[bold blue]WorkFlow-Mgr/{project_name}/{workstream_name} >[/]   [purple]Phase Name: [/] ')
                    if phase_name == 'finish':
                        break
                    else:
                        createPhase(phase_name, workstream_name, project_name)
            else:
                print_dir_error()
        else:
            print_dir_error()

    elif user_command == 'new-meeting':
        atendees = []
        add_new_meeting='y'
        project_name = console.input(prompt='   [purple]Project Name: [/] ')
        if check_directory_exists(project_name):
            workstream_name = console.input(prompt='   [purple]Workstream Name: [/] ')
            if check_directory_exists(f'{project_name}/{workstream_name}'):
                phase_name = console.input(prompt='   [purple]Phase Name: [/] ')
                if check_directory_exists(f'{project_name}/{workstream_name}/{phase_name}'):
                    console.print("Enter new Meeting Date")
                    while True:
                        meeting_date_year = console.input(prompt=f'[bold blue]WorkFlow-Mgr/{project_name}/{workstream_name}/{phase_name} >[/]       [purple]Meeting Date Year(DD): [/] ')
                        meeting_date_month = console.input(prompt=f'[bold blue]WorkFlow-Mgr/{project_name}/{workstream_name}/{phase_name} >[/]       [purple]Meeting Date Month(MM): [/] ')
                        meeting_date_day = console.input(prompt=f'[bold blue]WorkFlow-Mgr/{project_name}/{workstream_name}/{phase_name} >[/]       [purple]Meeting Date Day(YYYY): [/] ')
                        if meeting_date_day.isdigit() and meeting_date_month.isdigit() and meeting_date_year.isdigit():
                            console.print("Enter Atendees Name, enter 'finish' to finish ")
                            while True:
                                atendees_name = console.input(prompt=f'[bold blue]WorkFlow-Mgr/{project_name}/{workstream_name}/{phase_name}/{meeting_date_day}-{meeting_date_month}-{meeting_date_year} >[/]       [purple]Atendees Name: [/] ')
                                atendees.append(atendees_name)
                                if atendees_name == 'finish': break
                            createMeeting(f'{meeting_date_day}-{meeting_date_month}-{meeting_date_year}', atendees,  phase_name, workstream_name, project_name)
                        else:
                            print_error('Date is not in the correct format')
                        add_new_meeting=console.input('Add More meeting y/N ?')
                        if add_new_meeting.lower() == 'n': break
                else:
                    print_dir_error()
            else:
                print_dir_error()
        else:
            print_dir_error()

    elif user_command == 'show-info':
        project_name = console.input(prompt='   [purple]Project Name: [/] ')
        if check_directory_exists(project_name):
            showInfo(project_name)
        else:
            print_dir_error()
    elif user_command == 'export':
        project_name = console.input(prompt='   [purple]Project Name: [/] ')
        if check_directory_exists(project_name):
            createCSV(showInfo(project_name), project_name)
        else:
            print_dir_error()
    elif user_command == 'import':
        error = False
        file_name = console.input(prompt='   [purple]CSV File Name: [/] ')
        try:
            importCSV(file_name)
        except:
            print_dir_error()
            error = True
        if not error:
            art.tprint('WorkFlow Manager', font='big')
            print('''
    ==========================================
            Welcome to Workflow Manager CLI
    ==========================================

    Enjoy your stay! Use `help` to view a list of available commands.

    IMPORTANT NOTICE:
    Workflow Manager is proprietary software. 
    Unauthorized distribution or modifications are strictly prohibited.
    All rights reserved.

    (Note: This project is part of a QMUL assignment.)
    ''')
            tasks = ['Importing Tasks', 'Creating WorkStreams', 'Creating Phases', 'Creating Meetings']
            with console.status("[bold green]Working on tasks...") as status:
                while tasks:
                    task = tasks.pop(0)
                    time.sleep(2)
                    console.log(f"{task} - [bold green]Complete[/]")

    elif user_command=='show-structure':
        project_name = console.input(prompt='   [purple]Project Name: [/] ')
        if check_directory_exists(project_name):
            print(display_tree_structure(project_name))
        else:
            print_dir_error()
    else:
        print_error('Command Not Found')



# Displays the help page detailing the available commands available
def display_help():
    table = Table(title="Workflow Manager CLI Help", box=ROUNDED, show_header=True, header_style="bold magenta")
    
    table.add_column("Command", style="bold cyan", width=20)
    table.add_column("Description", style="dim", width=65)
    
    table.add_row("help", "Displays this help page with available commands.")
    table.add_row("show-info", "Displays information about a certain project")
    table.add_row("show-structure", "Displays the Project structure")
    table.add_row("new-project", "Creates a new project with the specified name.")
    table.add_row("new-workstream", "Creates a new workstream with the specified name.")
    table.add_row("new-phase", "Creates a new phase with the specified name.")
    table.add_row("new-meeting", "Creates a new phase with the specified name.")
    table.add_row("import-project", "Create a project from a CSV file")
    table.add_row("export-project", "Create a csv file")

    
    console.print(table)

#Creates a directory with the given name of project name
def createProject(projectName:str)->None:
    os.mkdir(projectName)

#Creates another folder inside projectname with name workstreamname
def createWorkstream(WorkstreamName:str, projectName:str)->None:
    try:
        os.mkdir(f'{projectName}/{WorkstreamName}')
    except Exception as e:
        print_error(f'Exception Error: {e}')

#Creates another folder inside projectname which is inside project name with a given name of Phase Name 
def createPhase(PhaseName:str, WorkstreamName:str, projectName:str):
    try:
        os.mkdir(f'{projectName}/{WorkstreamName}/{PhaseName}')
    except Exception as e:
        print_error(f'Exception Error: {e}')

#Creates a meeting txt file  with the date as its name and then a place with NOTES 
def createMeeting(MeetingDate, Atendees, PhaseName, WorkstreamName, projectName):
    try:
        with open(f'{projectName}/{WorkstreamName}/{PhaseName}/{MeetingDate}.txt', 'w') as file:
            for i in Atendees:
                file.write(f'{i}\n')
            file.write('NOTES: (Notes go below this)\n')
    except Exception as e:
        print_error(f'Exception Error: {e}')

#Creates a pretty table to show the current meetings for a project with the attendees that are assigned to it and then the phase and workstream they are part of 
def showInfo(project:str)->dict:
    workStreams = [i for i in os.listdir(project)]
    phases = {}
    meetings = []
    for i in workStreams:
        phases_found = []
        for j in os.listdir(f'{project}/{i}'):
            phases_found.append(j)
        phases[i] = phases_found

    for i in phases:
        for j in phases[i]:
            for o in os.listdir(f'{project}/{i}/{j}'):
                with open(f'{project}/{i}/{j}/{o}', 'r') as file:
                    lines = []
                    for line in file:
                        if 'NOTES' in line:
                            break
                        lines.append(line.rstrip())
                meetings.append({
                    'meeting':o,
                    'phase':j,
                    'workstream':i,
                    'attendees':lines
                })

    table = Table(title=f"Workflow Manager CLI Summaty for {project}", box=ROUNDED, show_header=True, header_style="bold magenta")
    table.add_column("Meeting", style="bold cyan", width=20)
    table.add_column("Attendes", style="white", width=65)
    table.add_column("Phase", style="red", width=35)
    table.add_column("Workstream", style="blue", width=35)
    for i in meetings:
        meeting_date = i['meeting']
        atendees_name =i['attendees']
        phase_name = i['phase']
        workstream_name=i['workstream']

        table.add_row(meeting_date, ', '.join(atendees_name), phase_name, workstream_name)
    print(table)
    return meetings

#Recursively goes through every folder in the given directory to build a tree to show the structure of the folder
def display_tree_structure(directory:str, tree=None)->Tree:
    if tree is None:
        tree = Tree(f"📁 [bold yellow]{directory}[/bold yellow]", guide_style="bold bright_blue")
    try:
        entries = sorted(os.listdir(directory))
    except PermissionError:
        tree.add("[red]Permission Denied[/red]")
        return tree
    for entry in entries:
        entry_path = os.path.join(directory, entry)
        if os.path.isdir(entry_path):
            sub_tree = tree.add(f"📁 [bold yellow]{entry}[/bold yellow]")
            display_tree_structure(entry_path, sub_tree)
        else:
            tree.add(f"📄 {entry}", style="dim")
    return tree

#Creates a CSV File with a fomat similar to the format of show-table
def createCSV(payload:str, projectName:str)->None:
    with open(f'output-{projectName}.csv', mode = 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Meeting Date', 'Attendees', 'Phase', 'Workstream'])
        for i in payload:
            meeting_date = i['meeting']
            atendees_name =i['attendees']
            phase_name = i['phase']
            workstream_name=i['workstream']
            writer.writerow([meeting_date, '; '.join(atendees_name), phase_name, workstream_name])

#Creates and builds a project structure based on the payload available in the csv file
def importCSV(file:str)->None:
    project_name = console.input(prompt='   [purple]Project Name: [/] ')
    with open(file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                createProject(project_name)
            except:
                pass
            try:
                createWorkstream(row[3], project_name)
            except:
                pass
            try:
                createPhase(row[2], row[3], project_name)
            except:
                pass
            try:
                createMeeting(row[0], [item.strip() for item in row[1].split(';')], row[2], row[3], project_name)
            except:
                pass
    os.system('clear')
    os.system('clear')

#Prints the welcome page very pretty
def main():
    os.system('clear')
    os.system('clear')
    art.tprint('WorkFlow Manager', font='big')
    print('''
==========================================
        Welcome to Workflow Manager CLI
==========================================

Enjoy your stay! Use `help` to view a list of available commands.

IMPORTANT NOTICE:
Workflow Manager is proprietary software. 
Unauthorized distribution or modifications are strictly prohibited.
All rights reserved.

(Note: This project is part of a QMUL assignment.)
''')
    while True:
        inputGetter()

if __name__ == "__main__":
    main()
