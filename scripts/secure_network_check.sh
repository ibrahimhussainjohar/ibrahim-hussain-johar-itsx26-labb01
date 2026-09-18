#!/usr/bin/env bash

#
# Detta script kollar om DNS fungerar och om lokalhost 8080 är öppet.
#

readonly LOG_FILE="network.log"
readonly DNS="example.com"
succes_count=2
kill_server=""

if [[ $1 == "-s" ]]; then
    python3 -m http.server --bind 127.0.0.1 8080 >/dev/null 2>&1 &
    server_ps=$!
    kill_server="yes"
    sleep 1
fi

log(){
    printf '%s [%s] %s\n' "$(date -Is)" "$1" "$2" | tee -a "$LOG_FILE"
}

# Miljö översikt
env_status(){
    device_interface=$(ip route | awk 'NR==1{print $5}')
    ip_address=$(ip -br a | grep "$device_interface" |awk '{print $3}')
    log INFO "Device Interface: $device_interface"
    log INFO "IP-adress: $ip_address"
}

check_dep(){
    if [[ -z $(command -v ss) ]]; then
        log WARN "ss är inte installerad"
        exit 1
    fi
}

# Kollar om DNS fungerar
check_dns(){
    if getent hosts "$DNS" >/dev/null; then
        log OK "DNS Fungerar"
    else
        log FAIL "DNS Fungerar inte"
        succes_count=$((succes_count-1))
    fi
}

check_port(){
    # Kollar om localport är öppet
    port=$(ss -tuln | grep 8080 | awk '{print $5}')

    # Kollar om server svarar.
    if [[ -n $port ]] && curl -Is "$port" >/dev/null; then
        log OK "Localhost 8080 lyssnar"
    else
        log FAIL "Localhost 8080 lyssnar inte"
        succes_count=$((succes_count-1))
    fi
}

tot_list_port(){
    local listall=$(ss -tuln | wc -l)
    local tot=$((listall-1))

    local tcp=$(ss -tuln | grep tcp | wc -l)
    local udp=$(ss -tuln | grep udp | wc -l)

    log INFO "tcp: $tcp/$tot udp: $udp/$tot"
}

cleanup(){
    if [[ $kill_server == "yes" ]]; then
        kill "$server_ps"
    fi
}
trap cleanup EXIT

main(){
    check_dep
    log INFO "Början"
    env_status
    check_dns
    check_port
    tot_list_port
    log INFO "Succes $succes_count/2"
    log INFO "Log file: $PWD/$LOG_FILE"
    log INFO "Slutet"
}
main
