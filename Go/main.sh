#!/bin/bash
set -e


function main() {
    if [ "${1}" = 'test' ]; then
        cd /99bottles && go test -v
    else
        cd /99bottles && go run main.go
    fi

}

main "${@}"
