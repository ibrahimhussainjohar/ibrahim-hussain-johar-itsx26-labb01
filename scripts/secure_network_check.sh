#!/usr/bin/env bash

readonly LOG_FILE="network.log"
readonly DNS="example.com"
readonly DATE=$(date -Is)

log(){
    printf "$DATE [$1] $2\n" | tee -a $LOG_FILE
}

check_dep(){
	if [[ -z $(command -v ss) ]]; then
		log WARN "ss är inte installerad"
		exit 1
	fi
}



# Kollar om DNS fungerar
check_dns(){
	if getent hosts $DNS >/dev/null; then
		log OK "DNS Fungerar"
	else
		log FAIL "DNS Fungerar inte"
	fi
}


check_port(){
# Kollar om localport är öppet
port=$(ss -tuln | grep 8080 | awk '{print $5}')

# Kollar om server svarar.
    if [[ -n $port ]] && curl -Is $port >/dev/null; then
        log OK "Localhost 8080 lyssnar"
    else
        log FAIL "Localhost 8080 lyssnar inte"
    fi
}


tot_list_port(){
    local listall=$(ss -tuln | wc -l)
    local tot=$((listall-1))
    
    local tcp=$(ss -tuln | grep tcp | wc -l)
    local udp=$(ss -tuln | grep udp | wc -l)

    log "tcp: $tcp/$tot udp: $udp/$tot"
}


main(){
log INFO "Början"
check_dep
check_dns
check_port
tot_list_port 
echo "Log file: $PWD/$LOG_FILE"
log INFO "Slutet"
}
main


