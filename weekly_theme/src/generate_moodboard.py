import argparse
import urllib

from openai import OpenAI
import ipdb

from weekly_theme.src.config import DATA_DIR, IMAGE_DIR


def generate_moodboard(theme: str) -> str:
    response = _open_ai_request(theme)
    img_url = response.data[0].url
    tgt_path = DATA_DIR / IMAGE_DIR / f"{theme}_moodboard.jpg"
    urllib.request.urlretrieve(img_url, tgt_path)
    return tgt_path

def _generate_prompt(theme: str) -> str:
    return f"A mood-board of diverse images for the theme of {theme}."

def _open_ai_request(theme):
    client = OpenAI()

    return client.images.generate(
        model="dall-e-3",
        prompt=_generate_prompt(theme),
        size="1024x1024",
        quality="standard",
        n=1,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a moodboard for a given theme.")
    parser.add_argument("--theme", type=str,
                        help="The theme for which to generate a moodboard.",
                        default="glitter")
    args = parser.parse_args()
    theme = args.theme
    with ipdb.launch_ipdb_on_exception():
        generate_moodboard(args.theme)
