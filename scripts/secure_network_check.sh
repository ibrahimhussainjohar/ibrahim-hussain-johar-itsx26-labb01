#!/usr/bin/env bash

readonly LOG_FILE="network.log"
readonly DNS="example.com"
readonly DATE=$(date -Is)

log(){
    printf "$DATE [$1] $2\n" | tee -a $LOG_FILE
}


# Kollar om DNS fungerar
if getent hosts $DNS >/dev/null; then
    log OK "DNS Fungerar"
else
    log FAIL "DNS Fungerar inte"
fi


# Kollar om localport är öppet
port=$(ss -tuln | grep 8080 | awk '{print $5}')

# Kollar om server svarar.
    if [[ -n $port ]] && curl -Is $port >/dev/null; then
        log OK "Localhost fungerar"
    else
        log FAIL "Localhost fungerar inte"
    fi


tot_list_port(){
    local listall=$(ss -tuln | wc -l)
    local tot=$((listall-1))
    
    local tcp=$(ss -tuln | grep tcp | wc -l)
    local udp=$(ss -tuln | grep udp | wc -l)

    log "tcp: $tcp/$tot udp: $udp/$tot"
}

echo "Log file: $PWD/$LOG_FILE"
tot_list_port 

