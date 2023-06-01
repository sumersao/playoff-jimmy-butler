from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from unidecode import unidecode


def scrape_year_seasontype(year, seasontype):
    url = f"https://www.basketball-reference.com/{seasontype}/NBA_{year}_advanced.html"

    # collect HTML data
    html = urlopen(url)

    # create beautiful soup object from HTML
    soup = BeautifulSoup(html, features="lxml")

    # get rows from table
    rows = soup.findAll('tr')[2:]
    rows_data = [[td.getText() for td in rows[i].findAll('td')]
                        for i in range(len(rows))]

    rows_cleaned = []
    for row in rows_data:
        # append a year column to the row
        row.append(year)

        if len(row) != 1:
            row[0] = unidecode(row[0])
            mp = int(row[5])
            if seasontype == "playoffs":
                if mp < 150:
                    continue
                rows_cleaned.append(row)
            else:
                if year == 2012:
                    if mp < 1207:
                        continue
                elif (year >= 2013 and year <= 2019) or year == 2022:
                    if mp < 1500:
                        continue
                elif year == 2020:
                    # conservatively 71 games played
                    if mp*82/71.0 < 1500:
                        continue
                elif year == 2021:
                    # only 72 games played
                    if mp*82/72.0 < 1500:
                        continue
                
                rows_cleaned.append(row)
    return rows_cleaned

def scrape_year(year):
    reg_season = scrape_year_seasontype(year, "leagues")
    playoffs = scrape_year_seasontype(year, "playoffs")

    return reg_season, playoffs

reg_season_total = []
playoffs_total = []

# scrape all years from 2011-2012 to 2021-2022
# for year in range(2012, 2023):
for year in range(2012, 2023):
    print(year)
    reg_season, playoffs = scrape_year(year)
    reg_season_total.extend(reg_season)
    playoffs_total.extend(playoffs)

# read the all star data
all_star = pd.read_csv("all_stars_averages.csv")

all_star_names = set(all_star["PLAYER_NAME"].values)

# drop all players that aren't one of the all stars
reg_season_total = [row for row in reg_season_total if row[0] in all_star_names]
playoffs_total = [row for row in playoffs_total if row[0] in all_star_names]

headers = ["Player", "Pos", "Age", "Tm", "G", "MP", "PER", "TS%", "3PAr", "FTr", "ORB%", 
        "DRB%", "TRB%", "AST%", "STL%", "BLK%", "TOV%", "USG%", "dummy_1", "OWS", "DWS", "WS", "WS/48",
        "dummy_2", "OBPM", "DBPM", "BPM", "VORP", "Year"]

reg_season_df = pd.DataFrame(reg_season_total, columns=headers)
playoffs_df = pd.DataFrame(playoffs_total, columns=headers)

# drop the dummy columns
reg_season_df = reg_season_df.drop(columns=["dummy_1", "dummy_2"])
playoffs_df = playoffs_df.drop(columns=["dummy_1", "dummy_2"])

reg_season_df.to_csv("advanced_stats.csv", index=False)
playoffs_df.to_csv("advanced_stats_playoffs.csv", index=False)