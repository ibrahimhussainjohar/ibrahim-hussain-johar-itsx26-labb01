#!/usr/bin/env python3

failed_login = 0

auth_file = "../data/auth.log"

# Testar om filen existerar eller inte
try:
  with open(auth_file, "r", encoding="utf-8") as log_file:
      for line in log_file:
          if "Failed login" in line:
              failed_login += 1
              print(line.strip())
  print(f"Failed logins: {failed_login}")
# Om filen inte finns, skriv ut att det inte finns
except FileNotFoundError:
    print(auth_file + " does not exist")

