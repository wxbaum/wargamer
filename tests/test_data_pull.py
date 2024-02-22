import pandas as pd
from pathlib import Path
import yaml

# Get config settings from app root folder (the directory above)
config_path = Path(__file__).parents[1]
with open(f'{config_path}/config.yaml') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Get actions data from GitHub
data_target_git_branch = config['DATA-TARGET-BRANCH']
actions_url = f'https://raw.githubusercontent.com/wxbaum/wargamer/{data_target_git_branch}/data/actions'
actions = pd.read_csv(actions_url)
print(actions)
