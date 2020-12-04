#!/bin/bash

main() {
    year=$1 # YYYY
    day=$((10#$2)) # D
    day0=$(printf "%02d" ${day}) # DD
    cookie=$3 # Session cookie

    # Copy template
    cp -r template ./${year}/${day0}

    # Replace placeholder
    sed -i "s/Day XX/Day ${day}/g" ./${year}/${day0}/README.md
    sed -i "s/TestDayXX/TestDay${day0}/g" ./${year}/${day0}/test.py

    # Fetch input data
    curl --cookie "session=${cookie}" https://adventofcode.com/${year}/day/${day}/input > ./${year}/${day0}/input.txt
}

usage() {
    echo "Usage: get_input.sh YEAR DAY COOKIE"
}

if [ $# == 3 ]; then
    main $1 $2 $3
else
    usage
fi
