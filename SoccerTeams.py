import random

plList = ["Arsenal", "Bournemouth", "Manchester City", "Manchester United", "Brighton", "Burnley", "Chelsea", "Crystal Palace",
          "Everton", "Huddersfield", "Leicester", "Liverpool", "Newcastle", "Southhampton", "Stoke", "Swansea", "Tottenham", "West Ham",
          "West Brom", "West Ham"]

ligue1 = ["Amiens", "Angers", "Bordeaux", "Caen", "Dijon", "Guingamp", "Lille", "Lyon", "Marseille", "Metz",
          "Monaco", "Montpelier", "Nantes", "Nice", "PSG", "Rennes", "Saint-Etienne", "Strasbourg", "Toulouse", "Troyes"]

serieA = ["Atalanta", "Benevento", "Bologna", "Cagliari", "Chievo", "Crotone", "Fiorentina", "Genoa", "Hellas Verona", "Inter",
          "Juventus", "Lazio", "Milan", "Napoli", "Roma", "Sampdoria", "Sassuolo", "SPAL", "Torino", "Udinese"]

bundes = ["Augsburg", "Hertha BSC", "Werder Bremen", "Borussia", "Eintracht Frankfurt", "Freiburg", "Hamburger SV",
          "Hannover", "Hoffenheim", "Koln", "RB Leipzig", "Leverkusen", "Mainz", "Borussia Monchengladbach", "Bayern",
          "Schalke", "Stuttgart", "Wolfsburg"]

laLiga = ["Alaves", "Bilbao", "Atletico", "Barcelona", "Celta Vigo", "Deportivo", "Eibar", "Espanyol", "Getafe", "Girona",
          "Las Palmas", "Leganes", "Levante", "Malaga", "Real Betis", "Real Madrid", "Real Sociedad", "Sevilla", "Valencia",
          "Villareal"]

print("My Teams:", random.choice(plList), ',', random.choice(ligue1), ',', random.choice(serieA), ',',
       random.choice(bundes), ',', random.choice(laLiga))
