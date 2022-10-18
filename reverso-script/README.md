# Reverso translator script
This script allows some translations from a given word to any reverso supported language.

I made this script in order to extend my vocabulary and learn new english words.

There's also a way to store the translations in an online Google Sheet with the following format:
| Source Language word | Destination language word |
|----------------------|---------------------------|
| ....                 | ...                       |
| ...                  | ...                       |

## Usage
Install the requirements
```pip install -r requirements.txt```

Args:
- `--source`: Source language (default: en)
- `--dest`: Destination language (default: it)
- `--word`: Word to translate (required)
- `--depth`: Numbers of desired different translations (default=5)
- `--write`: Write the translations to a Google Sheet (default=False) 
- `--file_id`: Google Sheet file id (required if write=y)

Example:

```python3 reverso.py --source=en --destination=it --word=Unabashed --depth=6 --write=y --file_id=1X2Y3Z```
## Libraries
- [reverso_context_api](https://github.com/flagist0/reverso_context_api)
- [gspread](https://github.com/burnash/gspread)