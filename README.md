# Web_Tools

A small personal toolbox for opening browser tabs and scraping web data. It holds one Python
script that opens a preset group of websites (or closes browser windows) based on a command
argument, and three R scripts that pull tables off web pages or the OMDb API and write the
results to CSV. The scripts are standalone; there is no package, no shared library, and no
build step.

## Tools

### `browse_bot.py`

Opens a fixed set of URLs in the default browser, grouped by activity. Each group is a
hardcoded dictionary of name to URL inside the script, so changing which sites open means
editing the file.

Run it with one command argument:

```bash
python browse_bot.py <command>
```

Commands:

- `startwork` opens Outlook calendar and mail, Trello, Google Calendar, Gmail, and Slack.
- `jobhunt` opens AWS, a Google Drive resume link, LinkedIn Jobs, saved Indeed jobs, a Trello
  job-search board, and a Podio workspace.
- `realestate` opens Podio, AirDNA, BiggerPockets, PropStream, and Zillow.
- `mymoney` opens Mint, Bank of America, Chase, Amex, and Fidelity.
- `endwork` closes three browser windows by moving the mouse and clicking with `pyautogui`.
- `workkpis` is accepted by the argument parser but has no branch in `main()`, so it does
  nothing. The `work_kpis()` function exists in the file but is never called.

`endwork` relies on hardcoded screen coordinates for a specific three-monitor layout. On any
other display setup those clicks will land somewhere else.

Several of the URLs point at Amazon-internal hosts (`ballard.amazon.com`, `quip-amazon.com`,
`accolades.corp.amazon.com`) and personal Podio and Salesforce workspaces, which will not
resolve or authenticate for anyone else.

### `6. Web Tools/Scaper-BOM-Actors.R`

Scrapes the Box Office Mojo actor listing across pages 1 to 3, takes the third HTML table on
each page, renames the columns to actor name, total gross, movie count, average per movie,
number one movie, and its gross, strips `$`, `%`, `,`, and `^` characters, converts the
numeric columns, then writes `Scraper-BOM-Actors.csv`.

Run it from R:

```r
source("6. Web Tools/Scaper-BOM-Actors.R")
```

The script calls `setwd("~/Documents/my-toolbox/5. Web Tools")` before writing, so the output
path only works on the original machine. It also references `df$Studio`, a column the scraper
never creates. The Box Office Mojo URL format it targets is old and the site has since been
restructured, so this will likely need rewriting to run today.

A sample output is committed as `6. Web Tools/Scraper-BOM-Actors.csv`.

### `6. Web Tools/Scaper-Montessori Schools.R`

Starts by reading the tables from `http://www.montessoricensus.org/school-maps/public/CA` into
a variable, then continues with an unchanged copy of the Box Office Mojo scraper above. The
Montessori table is fetched but never used, so despite the filename the script produces the
same actor CSV. Treat it as an unfinished draft.

### `6. Web Tools/Scraping-IMBD.R`

Reads `titlekey.csv` from `~/Desktop`, keeps the rows with a non-empty `imdbid`, and calls
`omdbapi::find_by_id()` on each ID. The results are flattened into a data frame with columns
for title, year, rating, release, runtime, genre, director, writer, actors, plot, language,
country, awards, poster, metascore, IMDb rating, IMDb votes, IMDb ID, and type, then written
to `IMBD Rating - OMBD API.csv`.

Run it from R:

```r
source("6. Web Tools/Scraping-IMBD.R")
```

The `omdbapi` package needs an OMDb API key. Set it before running:

```r
Sys.setenv(OMDB_API_KEY = "your_key")
```

The script hardcodes `setwd("~/Desktop")`, so `titlekey.csv` has to sit there. A copy of that
input file is committed at `6. Web Tools/titlekey.csv` with columns `imdbid`, `movielabs`,
`deluxe`, `bomid`, `bomtitle`, `wwrelease`, and `inreg`.

## Requirements

There is no requirements file or DESCRIPTION in the repo. Based on the imports:

Python 3:

- `pyautogui`
- standard library `webbrowser`, `time`, `argparse`

R:

- `XML` for the two scrapers
- `dplyr`, `pbapply`, and `omdbapi` for the IMDb script (only `omdbapi` is actually used)

## Installation

Clone the repo and install the dependencies you need.

```bash
git clone https://github.com/espin086/Web_Tools.git
cd Web_Tools
pip install pyautogui
```

For the R scripts:

```r
install.packages(c("XML", "dplyr", "pbapply"))
# omdbapi is on GitHub, not CRAN
remotes::install_github("hrbrmstr/omdbapi")
```

## License

No LICENSE file in this repo.
