#!/bin/bash
set -e


function main() {
    if [ "${1}" = 'test' ]; then
        cd /99bottles && pytest -v ./test_main.py
    else
        cd /99bottles && python ./main.py
    fi

}

main "${@}"
