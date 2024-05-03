# Phi Kappa Chi GroupMe Statistics

Analyzes data from the GroupMe API for main chat statistics.

## Keepers of the Code:

### Current Keeper
Oliver Liu, Gamma Delta, 2024 - present

### Former Keepers
| Name | Class | Time |
| --- | --- | --- |
| Luke Boydstun | Beta Psi | 2022 - 2023 |

## Installation

Use pip to install dependencies after cloning the project:

```
git clone git@github.com:oliverliu1/groupme-stats.git
pip install -r requirements.txt
```

## Usage
1. Go to https://dev.groupme.com/ and get an access token
2. Run `archive_chat.py --token [access token] --group-chat-id 30827774` on the command line
3. Run `analysis.py`
    - You will need to update the file paths in analysis.py to match the folder created by archive_chat.py:
        - Set `message_path` to `[chat name]/messages.json`
        - Set `people_path` to `[chat name]/people.json`
4. Run `category_leaders.py`













