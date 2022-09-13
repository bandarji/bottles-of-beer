#!/bin/bash
set -e


function main() {
    if [ "${1}" = 'test' ]; then
        cd /99bottles/beer && cargo test
    else
        cd /99bottles/beer && cargo run
    fi
}

main "${@}"
