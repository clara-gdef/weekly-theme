import random

from .config import DATA_DIR, THEME_FILE, PASSED_THEMES_FILE


def main():
    _file_checks()
    theme_file_path = DATA_DIR / THEME_FILE
    with open(theme_file_path, "r") as f:
        themes = f.readlines()
    index = random.randint(0, len(themes) - 1)
    selected_theme = themes.pop(index)
    _update_theme_files(selected_theme, themes)
    return selected_theme.strip().lower()


def _update_theme_files(selected_theme, themes):
    # we update the themes file with the updated theme list
    theme_file_path = DATA_DIR / THEME_FILE
    with open(theme_file_path, "w") as f:
        f.writelines(themes)
    passed_themes_file_path = DATA_DIR / PASSED_THEMES_FILE
    with open(passed_themes_file_path, "a") as f:
        f.write(selected_theme)


def _file_checks():
    if not DATA_DIR.exists():
        DATA_DIR.mkdir()
    if not (DATA_DIR / THEME_FILE).exists():
        raise FileNotFoundError(
            f"File {THEME_FILE} not found in {DATA_DIR}, please add it under the correct path.")

    # Initialize the passed and left themes files if they don't exist
    if not (DATA_DIR / PASSED_THEMES_FILE).exists():
        print(f"File {PASSED_THEMES_FILE} not found in {DATA_DIR}, creating it.")
        with open(DATA_DIR / PASSED_THEMES_FILE, "w") as f:
            f.write("")


if __name__ == "__main__":
    main()
