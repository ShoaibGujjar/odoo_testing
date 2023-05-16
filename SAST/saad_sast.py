import bandit
from bandit.core import manager

def run_bandit_sast():
    bandit_config = {
        'targets': ['path/to/odoo/addons/project_manager'],
        'recursive': True,
        'format': 'txt',
        'output_file': 'bandit_report.txt'
    }
    manager.BanditManager(bandit_config).run()
    print("Bandit SAST analysis completed.")

if __name__ == "__main__":
    print("Running SAST for Project Manager module in Odoo...")
    
    run_bandit_sast()

    print("SAST analysis completed.")
