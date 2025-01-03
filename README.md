# Weekly Themes

Welcome to this simple package that will draw a random theme for your upcoming week.
This theme is meant to be a source of inspiration for your week, and can be used in any way you see fit.
I personally use it to drive my outfits, makeup, and even as an extra nudge when I need to make decisions and I feel a bit lost.

I hope you like it!

## Getting Started

### Requirements
See the `pyproject.toml` file for the required packages.

### Download
You can download this package by cloning this repository:

```bash
git clone https://github.com/clara-gdef/weekly-theme.git
```

### Installation
You can install this package using `poetry`:

```bash
poetry install [--with dev]
```

### Usage

You can use this package by running the following command:

```bash
 poetry run python weekly_theme/src/weekly_theme/theme_moodboard.py
```

## TODO
- [ ] Add a connection to Google Keep to sync your weekly themes with a note you can modify from your phone
- [ ] Automate the draw so that it happens every Sunday at 12:00.
- [ ] Add a connection to Google Calendar to add your weekly theme as an event
- [ ] Add a connection to Spotify to create a playlist based on your weekly theme (?)
- [x] Add a connection to Dall-E or any other (free!) AI image generator to create a moodboard based on your weekly theme
- [ ] Add a nicer User Interface
- [x] Fix the command line for running the script, it should be  poetry run python weekly_theme but somehow it's not working
- [ ] Add type hinting
- [ ] Add tests
- [ ] Add a logging system rather than just print statements