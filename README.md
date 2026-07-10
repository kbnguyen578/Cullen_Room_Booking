# SASE Cullen College Room Booking Automation 

Automates filling out the UH Cullen College of Engineering room reservation form using data that officers provided from the SASE Room Booking Google Sheet. 

⚠️ WARNING - SAFARI IS NOT READY YET, BRAVE IN TESTING ⚠️

## Requirements 
- Python 
- Safari or Chrome 

## Setup 
1. Clone this repo 

    (in terminal)
    ```
    git clone https://github.com/kbnguyen578/Cullen_Room_Booking
    cd Cullen_Room_Booking 
    ```
2. Delete the files that are NOT your browser file 
    
    You should only have these files: 
        - Browser_Name/ 
            - autofill.py 
            - main.py 
            - template.config.json 
            - sheets.py 
            - dependencies.txt 

3. Create and activate virtual environment 

    (in terminal)

    //  Mac
    ```
    python3 -m venv venv 
    source venv/bin/activate 
    ```

    // Windows 
    ```
    python -m venv venv 
    venv\Scripts\activate
    ```

4. Install dependencies 

    (in terminal)
    ```
    pip install -r depedencies.txt 
    ```

5. Add your (Event Coordinator) credentials 
    - get the "service_acount.json" file from the current event coordinator 
    - place it into project folder 
    - copy and fill out the config.template.json file and rename it to config.json 

    Brave users need to add the browser path in config.json: 
    ```
        Windows:
        "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    ```
    ```
        Mac: 
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
    ```
    ```
        Linux: 
        "/usr/bin/brave-browser"
    ```

## Usage 
- "main.py"                 -- entry point, terminal menu 
- "sheets.py"               -- reads from Google Sheets 
- "autofill.py"             -- fills the UH form using Selnium 
- "config.json"             -- Event Coordinator's info 
- "service_account.json"    -- Google Sheets Credentials (never release this anywhere)
- venv/                     -- emulate every dependencies Event Coordinator needs to use program 
- "dependencies.txt"        -- all the dependencies program uses & what venv needs to set up for Event Coordinator 
