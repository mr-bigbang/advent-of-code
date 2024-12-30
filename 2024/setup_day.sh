#!/bin/bash
# Most of this is stolen from https://github.com/kageru/advent-of-code/blob/master/2024/setup_day.sh

function copy_template() {
    year=$1 # YYYY
    day=$2 # DD

    mkdir -p src/bin
    echo '#![feature(test)]
extern crate test;

use advent_of_code::read_file;

const DAY: usize = '${day}';
type T = usize;
type Parsed = Vec<T>;

fn parse_input(raw: &str) -> Parsed {
    todo!();
}

fn part1(parsed: &Parsed) -> usize {
    todo!();
}

fn part2(parsed: &Parsed) -> usize {
    todo!();
}

fn main() {
    let raw_input = read_file(DAY);
    let input = parse_input(&raw_input);
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = "";

    #[test]
    fn test_part1() {
        let input = parse_input(TEST_INPUT);
        assert_eq!(part1(&input), 0);
    }

    #[test]
    fn test_part2() {
        let input = parse_input(TEST_INPUT);
        assert_eq!(part2(&input), 0);
    }

    #[bench]
    fn bench_parse(b: &mut test::Bencher) {
        let raw = &read_file(DAY);
        b.iter(|| parse_input(test::black_box(&raw)));
    }

    #[bench]
    fn bench_part1(b: &mut test::Bencher) {
        let raw = &read_file(DAY);
        let input = parse_input(&raw);
        b.iter(|| part1(test::black_box(&input)));
    }

    #[bench]
    fn bench_part2(b: &mut test::Bencher) {
        let raw = &read_file(DAY);
        let input = parse_input(&raw);
        b.iter(|| part2(test::black_box(&input)));
    }
}' > src/bin/day${day}.rs
}

function get_input() {
    year=$1 # YYYY
    day=$2 # DD
    cookie=$3

    mkdir inputs
    curl --cookie "session=${cookie}" https://adventofcode.com/${year}/day/$((10#${day}))/input > ./inputs/input${day}.txt
}

function main() {
    year=$1 # YYYY
    day=$2 # DD
    cookie=$3
    if [[ ${day} != 0* ]]; then
    	day="0${day}"
    fi

    echo "Setting up day ${day}"
    copy_template ${year} ${day}
    get_input ${year} ${day} ${cookie}
}

usage() {
    echo "Usage: setup_day.sh YEAR DAY COOKIE"
}

if [[ $# == 3 ]]; then
    main $1 $2 $3
else
    usage
fi

