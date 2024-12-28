import argparse
import urllib

from openai import OpenAI

from .config import DATA_DIR, IMAGE_DIR


def main(theme: str) -> str:
    response = _open_ai_request(theme)
    print("Image received from OpenAI API!")
    img_url = response.data[0].url
    tgt_path = DATA_DIR / IMAGE_DIR / f"{theme}_moodboard.jpg"
    urllib.request.urlretrieve(img_url, tgt_path)
    return tgt_path


def _generate_prompt(theme: str) -> str:
    return f"A mood-board of diverse images for the theme: '{theme}'. Please include abstract images as well as figurative ones, including a variety of colors, textures ans subjects, from people to landscapes and architecture."


def _open_ai_request(theme):
    client = OpenAI()
    print("Making request to OpenAI API...")
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
    main(args.theme)
