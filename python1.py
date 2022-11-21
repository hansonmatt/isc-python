import csv

#teams = {
#    "ISC Gunners 04G GA" : { "coach" : "Giovanni Monroe", "program" : ""}
#}
teams = dict()
teams["ISC Gunners 04G GA"]={ "coach" : "Giovanni Monroe", "program" : "Premier"}
teams["ISC Gunners 08B EA"]={ "coach" : "Michael Conchie", "program" : "Premier"}
teams["ISC Gunners 06B EA"]={ "coach" : "Michael Conchie", "program" : "Premier"}
teams["ISC Gunners 07B EA"]={ "coach" : "Eddie Henderson", "program" : "Premier"}
teams["ISC Gunners Select B12 Blue"]={ "coach" : "Brandon Hubbardn", "program" : "Select"}

dates=dict()
with open('/Users/matthewhanson/Development/isc/ISC-Gunners-schedule.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['Match #'], row['Date'], row['Time'], row['Home Team'], row['Away Team'], row['Location'], row['Division'])
        if row['Home Team'] in teams:
            team=teams[row['Home Team']]
            if team is not None:
                program=team['program']
                game = {
                    "program" : program,
                    "match" : row['Match #'],
                    "coach" : team['coach'],
                    "home_team" : row['Home Team'],
                    "away_team" : row['Away Team'],
                    "date" : row['Date'],
                    "time" : row['Time']
                }
                #print("Found game = " + str(game))

                #tmp = dates.get(game["date"])
                if dates.get(game["date"]) is None:
                    dates[game["date"]] = dict()
                
                if dates[game["date"]].get(program) is None:
                    dates[game["date"]][program] = dict()

                if dates[game["date"]][program].get(game['coach']) is None:
                    dates[game["date"]][program][game['coach']] = list()

                dates[game["date"]][program][game['coach']].append(game)

print(dates)
for date in dates:
    print("Date = " + date)
    for program in dates[date]:
        print("Program = " + program)
        #coaches = dates[date][program]
        for coach in dates[date][program]:
            print("Coach = " + coach)
            for game in dates[date][program][coach]:
                print("Game = " + str(game))
        #for coach in dates[date][program]:
        #    print("Coach = " + coach)
        
