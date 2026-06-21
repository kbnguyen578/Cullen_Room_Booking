# SASE Cullen College Room Booking Automation 

Automates filling out the UH Cullen College of Engineering room reservation form using data that officers provided from the SASE Room Booking Google Sheet. 

## Requirements 
- Python 
- Safari or Chrome 

## Setup 
1. Clone this repo 

    (in terminal)
    git clone https://github.com/kbnguyen578/Cullen_Room_Booking
    cd Cullen_Room_Booking 

2. Create and activate virtual environment 

    (in terminal)
    # Mac
    python3 -m venv venv 
    source venv/bin/activate 
    # Windows 
    python -m venv venv 
    venv\Scripts\activate

3. Install dependencies 

    (in terminal)
    pip install -r depedencies.txt 

4. Add your (Event Coordinator) credentials 
    - get the "service_acount.json" file from the current event coordinator 
    - place it into project folder 
    - copy and fill out the config.template.json file and rename it to config.json 

## Usage 
- "main.py"                 -- entry point, terminal menu 
- "sheets.py"               -- reads from Google Sheets 
- "autofill.py"             -- fills the UH form using Selnium 
- "config.json"             -- Event Coordinator's info 
- "service_account.json"    -- Google Sheets Credentials (never release this anywhere)
