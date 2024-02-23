import pandas as pd
from pathlib import Path
import yaml


class DataRequest:
    def __init__(self) -> None:
        self.config = self._load_config()

    def _load_config(self):
        # Get config settings from app root folder (the directory above)
        config_path = Path(__file__).parents[1]
        with open(f'{config_path}/config.yaml') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def get_actions_data(self):
        # Get actions data from GitHub
        data_target_git_branch = self.config['DATA-TARGET-BRANCH']
        actions_url = f'https://raw.githubusercontent.com/wxbaum/wargamer/{data_target_git_branch}/data/actions'
        actions = pd.read_csv(actions_url)
        actions.columns = [col.replace(' ', '_').lower() for col in actions.columns]
        return actions
