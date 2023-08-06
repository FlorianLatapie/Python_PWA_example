
# Python server for PWA (Progressive Web App) example

This is a simple example of a Python server for a PWA (Progressive Web App).

App icon from [Flaticon](https://www.flaticon.com/fr/icones-gratuites/application) by [Freepik](https://www.flaticon.com/fr/auteurs/freepik).

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python server.py
```

Then go to [http://localhost:5000](http://localhost:5000).

## Known issues

- It does not work on iOS (Safari and Chrome, I tried), it may be caused by the lack of support for the [Web Share API](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/share) and the [Web App Manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest).

## See also

This repository is inspired from [zdimension's volumegui.py gist](https://gist.github.com/zdimension/2b193e5d1ba403aa1ad1f570becd5399), feel free to take a look at it.
