"""
oh no
FANTASY STAR ONLINE
or; how to ruin everyone's fun
by: @lucaspotter
"""

import pandas as pd
import nfl_data_py as nfl

df = "null"


def menu():
	print("Please select an option:")
	print("1. Find play-by-play data for a game")
	print("2. Find the best player/team for a position")
	print("3. Find the best fantasy team")
	print("4. Exit")

	choice = int(input("\nChoice: "))
	if choice == 1:
		print(pbpData())
	elif choice == 2:
		print("Not implemented yet.")
		menu()
	elif choice == 3:
		print("Not implemented yet.")
		menu()
	elif choice == 4:
		exit()
	else:
		print("That's not a valid choice. Try again.")
		menu()
	menu()


def setupDataframe():
	global df
	year = [1999]
	allYears = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
	            2016, 2017, 2018, 2019, 2020]

	choice = input("Would you prefer to use all years of data, or a specific year? (all, specific) ")
	if choice == "all":
		year = allYears
	elif choice == "specific":
		specificYear = int(input("What year would you like to use? use format: '1999' "))
		year[0] = specificYear
	else:
		print("That's not a valid choice. Try again.")
		setupDataframe()

	print("Setting up data...")

	df = nfl.import_pbp_data(year, downcast=False, cache=True)
	df = pd.DataFrame(df, columns=["game_id", "desc"])


def findGameID():
	year = input("What year was the game? ")
	week = input("What week was the game? Add a leading zero if it's a single digit. ")
	awayTeam = input("What team was away? Format: 'ARI, SF' ")
	homeTeam = input("What team was home? Format: 'ARI, SF' ")
	gameID = year + "_" + week + "_" + awayTeam + "_" + homeTeam
	return gameID.upper()


def pbpData():
	gameID = findGameID()
	filtered = df[df["game_id"].str.contains(gameID)]

	if filtered.empty:
		print("That's not a valid game ID. Try again.")
		pbpData()
	else:
		return filtered


if __name__ == "__main__":
	print("Welcome to Fantasy Star Online, the only fantasy tool which has a pun as it's name.")
	setupDataframe()
	menu()
