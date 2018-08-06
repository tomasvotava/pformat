# PFormat
Python TTY color formatter.

## Screenshot

![alt text](https://raw.githubusercontent.com/tomasvotava/pformat/master/screenshot.png "Screenshot")

## Installation
```bash
$ git clone https://github.com/tomasvotava/pformat.git
$ cd pformat
$ ./setup.py install
```

## Usage
```python
from pformat import pprint

pprint(":red:This is a red text:-: This is default text. :blue:This is blue text.")
pprint("Every pprint command ends with default reset, so this a default text.")
```

## Available codes
| Code    | Meaning                                                  |
|---------|----------------------------------------------------------|
| -       | reset everything                                         |
| bold    | **bold text**                                            |
| dim     | <span style="color: gray;">dimmed text</span>            |
| normal  | normal text                                              |
| black   | <span style="color: black;">black text</span>            |
| red     | <span style="color: red;">red text</span>                |
| green   | <span style="color: green;">green text</span>            |
| yellow  | <span style="color: yellow;">yellow text</span>          |
| blue    | <span style="color: blue;">blue text</span>              |
| magenta | <span style="color: magenta;">magenta text</span>        |
| cyan    | <span style="color: cyan;">cyan text</span>              |
| white   | <span style="color: white;">white text</span>            |
| bblack  | <span style="background: black;">black background</span> |
| bred    | <span style="background: red;">red background</span>     |
| bgreen  | <span style="background: green;">green background</span> |
| bwhite  | <span style="background: white;">white background</span> |
