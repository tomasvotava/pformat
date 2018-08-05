# PFormat
Python TTY color formatter.

## Usage
```python
from pformat import pprint

pprint(":red:This is a red text:-: This is default text. :blue:This is blue text.")
pprint("Every pprint command ends with default reset, so this a default text.")
```

## Available codes
| Code    | Meaning          |
|---------|------------------|
| -       | reset everything |
| bold    | *bold text*      |
| dim     | dimmed text      |
| normal  | normal text      |
| black   | black text       |
| red     | red text         |
| green   | green text       |
| yellow  | yellow text      |
| blue    | blue text        |
| magenta | magenta text     |
| cyan    | cyan text        |
| white   | white text       |
| bblack  | black background |
| bred    | red background   |
| bgreen  | green background |
| bwhite  | white background |
