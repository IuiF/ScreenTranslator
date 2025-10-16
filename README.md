# Advanced Screen Translator

Forked from [OneMoreGres/ScreenTranslator](https://github.com/OneMoreGres/ScreenTranslator) with focus on improving OCR text detection accuracy.

## Introduction

This software allows you to translate any text on screen.
Basically it is a combination of screen capture, OCR and translation tools.
Translation is currently done via online services.

## Enhancements in this Fork

### OCR Detection Improvements
- **Deskewing**: Automatic text rotation correction for better accuracy (±2 degrees)
- **Adaptive Binarization**: Sauvola algorithm with Otsu fallback for various lighting conditions
- **Noise Reduction**: Gaussian-like filtering to reduce image noise
- **Border Optimization**: 10px white border addition for improved edge detection
- **Resolution Optimization**: Adjusted to Tesseract-recommended 300 DPI

### Planned Improvements
- Dynamic PSM (Page Segmentation Mode) selection
- OCR confidence-based retry mechanism
- Configurable OEM (OCR Engine Mode) settings

## Installation

Build from source (see below). Pre-built binaries are not yet available for this fork.

For the original ScreenTranslator binaries, see [OneMoreGres/ScreenTranslator releases](https://github.com/OneMoreGres/ScreenTranslator/releases).

## Setup

The app doesn't have a main window.
After start it shows only the tray icon.

If the app detects invalid settings, it will show the error message via system tray.
It will also highlight the section name in red on the left panel of the settings window.
Clicking on that section name will show a more detailed error message in the right panel (also in red).

The packages downloaded from this site do not include resources, such as recognition language packs or scripts to interact with online translation services.

To download them, open the settings window and go to the `Update` section.
In the right panel, expand the `recognizers` and `translators` sections.
Select preferred items, then right click and choose `Install/Update`.
After the progress bar reaches `100%`, the resource's state will change to `Up to Date`.

You must download at least one `recognizers` resource and one `translators` resource.

After finishing downloads, go to the `Recognition` section and update the default recognition language setting (the source to be translated).
Then go to the `Translation` section, update the default translation language setting (the language to be translated into) and enable some or all translation sevices (you may also change their order by dragging).

After that all sections in the left panel should be black.
Then click `Ok` to close settings.

### Third party enhancements

**Not tested or reviewed by me**

* to translate with online AI services use scripts from [here](https://github.com/Suki8898/Translator)

* to install Hebrew translation of the app itself (thanks to [Y-PLONI](https://github.com/Y-PLONI)),
download [this](https://github.com/OneMoreGres/ScreenTranslator/releases/download/3.3.0/screentranslator_he.qm)
file and place it into the `translations` folder next to `screen-translator.exe`.

## Usage

1. Run program (note that it doesn't have main window).
2. Press capture hotkey.
3. Select region on screen. Customize it if needed.
4. Get translation of recognized text.
5. Check for updates if something is not working.

## FAQ

By default resources are downloaded to the one of the user's folders.
If `Portable` setting in `General` section is checked, then resources will be downloaded to the app's folder.

Set `QTWEBENGINE_DISABLE_SANDBOX=1` environment variable when fail to start due to crash.

Answers to some frequently asked questions can be found in issues or
[wiki](https://github.com/OneMoreGres/ScreenTranslator/wiki/FAQ)

## Limitations

* Can not capture some dynamic web-pages/full screen applications

## Dependencies

* see [Qt 5](https://qt-project.org/)
* see [Tesseract](https://github.com/tesseract-ocr/tesseract/)
* see [Leptonica](https://leptonica.com/)
* several online translation services

## Build from source

Look at the scripts (python3) in the `share/ci` folder.
Normally, you should only edit the `config.py` file.

Build dependencies at first, then build the app.

## Attributions

* icons made by
[Smashicons](https://www.flaticon.com/authors/smashicons),
[Freepik](https://www.flaticon.com/authors/freepik),
from [Flaticon](https://www.flaticon.com/)

## Alternative solutions

* [Translumo](https://github.com/ramjke/Translumo) - Advanced real-time screen translator for games, hardcoded subtitles in videos, static text and etc.
