from draw_theme import draw_theme
from generate_moodboard import generate_moodboard


def main():
    theme = draw_theme()
    path_to_image = generate_moodboard(theme)
    print(
        f"Generated moodboard for weekly theme: {theme}. Image saved at: {path_to_image}. Enjoy!")


if __name__ == "__main__":
    main()
