#!/usr/bin/env bash

failed_login = 0

with open("/data/auth.log", encoding="utf-8") as log_file:
    for line in log_file:
        if "Failed login" in log_file:
            print(line.strip())
