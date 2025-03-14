# Implementation Details:

1. Clone the Repository:
    - `git clone https://github.com/mallow-self/timesheet.git`

2. Change directory into timesheet:
    - `cd timesheet`

3. Set up a conda virtual environment:
    - Current directory:
        - ~/timesheet/
    1. Create a virtual conda environment:
        - `conda create -n timesheet-env python=3.12`
        - Note: You need to have conda installed globally - [Refer](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html)
    2. Activate the environment:
        - `conda activate timesheet-env`

4. Set up poetry:
    - Current directory:
        - ~/timesheet/
    1. Add packages using poetry:
        - `poetry install`
        - Note: You need to have poetry installed globally - [Refer](https://python-poetry.org/docs/basic-usage/)

5. Change Directory:
    - Current directory:
        - ~/timesheet/
    1. Change into timesheetMod directory from timesheet directory:
        - `cd timesheetMod`

6. Make migrations:
    - Current directory:
        - ~/timesheet/timesheetMod
    
    - Run this command to make migrations:
        - ubuntu/linux: `python3 manage.py makemigrations`
        - windows: `python manage.py makemigrations`

7. Migrate:
    - Current directory:
        - ~/timesheet/timesheetMod
    
    - Run this command to migrate:
        - ubuntu/linux: `python3 manage.py migrate`
        - windows: `python manage.py migrate`

8. Run app/server:
    - Current directory:
        - ~/timesheet/timesheetMod
    
    - Run this command to run the server:
        - ubuntu/linux: `python3 manage.py runserver`
        - windows: `python manage.py runserver`