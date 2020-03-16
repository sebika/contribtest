### Marinescu Sebastian-Ioan, interview pull request

## Info
Generate site from static pages, loosely inspired by Jekyll
## Installation

You should have `python3` and `pip3` installed.
After that, install all requirements for the project:

    pip3 install -r requirements.txt

If that doesn't work try with the command below, or check the `requirements.txt` file and install them manually:

    pip3 install -r requirements.txt --user

## Runnnig
From the root directory (`contribtest`), run the main module like this:

    ./generate.py test/source output

The generated `output` should be the same as `test/expected_output`

## Testing

If you installed `requirements.txt` correctly you can simply run:

    pytest
