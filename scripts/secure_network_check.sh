#!/usr/bin/env bash

LOG_FILE="network.log"
DNS="example.com"

log(){
    printf "[$1] $2\n" | tee -a $LOG_FILE
}

if getent hosts $DNS >/dev/null; then
    log OK "DNS Fungerar"
else
    log WARN "DNS Fungerar inte"
fi


