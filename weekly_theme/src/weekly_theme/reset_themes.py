from config import DATA_DIR, THEME_FILE, PASSED_THEMES_FILE

def reset_themes():
    with open(DATA_DIR / THEME_FILE, "r") as f:
        remaining_themes = f.readlines()
    with open(DATA_DIR / PASSED_THEMES_FILE, "r") as f:
        passed_themes = f.readlines()

    remaining_themes.extend(passed_themes)

    with open(DATA_DIR / THEME_FILE, "w") as f:
        f.writelines(remaining_themes)
    with open(DATA_DIR / PASSED_THEMES_FILE, "w") as f:
        f.write("")


if __name__ == "__main__":
    reset_themes()
