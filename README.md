# Discord Username Checker

This is a Python script that checks the availability of Discord usernames using the Discord API.

## Prerequisites

Before running the script, make sure you have the following prerequisites:

- Python 3.x
- `requests` library (you can install it using `pip install requests`)
- `dotenv` library (you can install it using `pip install python-dotenv`)

## Setup

1. Clone the repository:

```bash
git clone https://github.com/verifizieren/discord-user-checker
```
2. Install the required dependencies:
```bash
pip install requests python-dotenv
```
3. Create a `.env` file in the root directory of the project and add your Discord API token:
```makefile
TOKEN=YOUR_DISCORD_API_TOKEN
```
## Usage

1. Open a terminal and navigate to the project directory.
2. Run the script:
```bash
python discord-user.py
```
3. Enter the desired username length and delay (in milliseconds) when prompted.
4. The script will generate random usernames, check their availability, and display the results.
