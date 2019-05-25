woj = { "podkarpackie": "PK",
		"malopolskie": "MP",
		"mazowieckie": "MZ",
		"slaskie": "SL"
		}
miasta = {
		"MP": "Krakow",
		"PK": "Rzeszow",
		"MZ": "Warszawa",
		"SL": "Katowice"
		}

for w, abbr in woj.items():
	print(f"Woj: {w} ({abbr}), city: {miasta[abbr]}")
