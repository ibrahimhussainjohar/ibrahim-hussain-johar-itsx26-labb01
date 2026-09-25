#!/usr/bin/env python3

skipped = 0

auth_file = "../data/auth.log"


try:
  with open(auth_file, "r", encoding="utf-8") as log_file:
    for line in log_file:
        # En linje tas och delas up och sätts in i ett array
        fields = line.split()
        source_fields = [f for f in fields if f.startswith("src=")]

        if not source_fields:
            skipped += 1
            continue
        
        # Välj första element av array. Dela elementen till två delar och '=' är markör var det ska delas.
        p_address = source_fields[0].split("=", 1)[1]

        print(f"IP address: {p_address}")
except FileNotFoundError:
    print(auth_file + " does not exist")
