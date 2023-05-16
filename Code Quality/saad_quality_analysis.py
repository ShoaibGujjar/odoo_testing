import pylint.lint
import flake8.main.cli
import bandit.core.cli

# Pylint
def run_pylint():
    pylint_opts = [
        "--load-plugins=pylint_odoo",
        "--disable=all",
        "--enable=odoo-addons",
        "--reports=no",
        "--output-format=text",
    ]
    pylint_run = pylint.lint.Run(pylint_opts + ["C:\odoo\addons\project_manager"])
    pylint_results = pylint_run.linter.stats["global_note"]
    return pylint_results

# Flake8
def run_flake8():
    flake8_opts = ["--max-line-length=120", "C:\odoo\addons\0project_manager"]
    flake8_main = flake8.main.cli.main(flake8_opts)
    flake8_results = flake8_main.exit_code
    return flake8_results

# Bandit
def run_bandit():
    bandit_opts = ["-r", "C:\odoo\addons\0project_manager"]
    bandit_main = bandit.core.cli.main(bandit_opts)
    bandit_results = bandit_main.exit_code
    return bandit_results

if __name__ == "__main__":
    print("Running code quality analysis for Project Manager module in Odoo...")
    
    print("Running Pylint...")
    pylint_results = run_pylint()
    print("Pylint Results:", pylint_results)

    print("Running Flake8...")
    flake8_results = run_flake8()
    print("Flake8 Results:", flake8_results)

    print("Running Bandit...")
    bandit_results = run_bandit()
    print("Bandit Results:", bandit_results)

    print("Code quality analysis completed.")
