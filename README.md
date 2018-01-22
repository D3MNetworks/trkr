# trkr

`trkr` is a command-line tool to help track what our team is working on and
how long they work on it. With Trello and Google Sheets integration, it allows
you to search and select a related Trello card, and writes directly to a Worksheet.

## Requirements

Python 2.6+ or 3+

## Installation

```python
pip install trkr
```

## Usage

Using trkr is as simple as running `trkr run`. A list of valid command is available
by running `trkr --help`.

### Description

Provide a description of the work accomplished. If none is provided, the commit
message of the last commit at HEAD will be used.

### Minutes Worked

Time worked in minutes (must be a valid integer).

### Trello Card

You have the choice to (i)nput a card's URL, fuzzy (s)earch for a card, (p)ick from
a list of your assigned cards, or choose to (n)ot include a card.

### Date

Enter a timestamp in the `MM/DD/YYYY` format. This can be skipped, and will instead
use the current date.

## Setup

To start the setup script, run `trkr setup`. It will ask for an email, Trello
API keys, and the worksheet URL. All settings are saved at `~/.trkr/config.json`,
and can be modified at a later time.

### Trello Authentication

#### Finding Client ID and Board ID

On Trello, navigate to a board and append `.json` to the URL. It should look
something like `https://trello.com/c/<url>.json`. When the JSON data has loaded,
hthe first `id` will be the *Board ID*; copy and save it somewhere.

Search next for your name or username, find the `id` associated with it, and
save it somewhere; this is your *Client ID*.

#### API Keys and Token

Trello API keys can be found at [trello.com/app-key](https://trello.com/app-key).
The hash found under `Key` is your *API Key*, and the one under `Secret` is your
*API Secret*. A Token can be generated by clicking `Token` on the same page; this
is your *Token*.

### Google Sheets Authentication

Once you've created a new Google Sheet, it's URL is the *Document URL*, and the
name of the sheet at the bottom is the *Worksheet Name*.

In order to authorize `trkr` to read/write from a worksheet, follow the steps
layed out in [Authorizing pygsheets](https://pygsheets.readthedocs.io/en/latest/authorizing.html).
With the JSON file in hand, move it to `~/.trkr/keyfile.json`. Lastly, share
the worksheet with the email found in `keyfile.json`. `trkr` should now be setup
and ready to use!

## Acknowledgement

`trkr` relies on the great work done by the [pygsheets](https://github.com/nithinmurali/pygsheets/)
and [py-trello](https://github.com/sarumont/py-trello) teams.

