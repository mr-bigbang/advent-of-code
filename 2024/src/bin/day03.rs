#![feature(test)]
extern crate test;

use advent_of_code::read_file;
use regex::Regex;
use std::sync::LazyLock;

const DAY: usize = 03;
type T = usize;
type Parsed = Vec<(T, T)>;

fn parse_input(raw: &str) -> Parsed {
    const REGEX: &str = r"mul\((\d+),(\d+)\)";
    // Avoid re-compiling regex for part2()
    //let re: Regex = Regex::new(REGEX).unwrap();
    static RE: LazyLock<Regex> = LazyLock::new(|| Regex::new(REGEX).unwrap());

    let ret: Parsed = RE
        .captures_iter(raw)
        .map(|caps| {
            let (_, [a, b]) = caps.extract();
            (a.parse().unwrap(), b.parse().unwrap())
        })
        .collect();
    ret
}

fn parse_input2(raw: &str) -> Parsed {
    // Flag s is required because raw contains line breaks
    const REGEX: &str = r"(?s)do\(\)(.*?)don't\(\)";
    let re: Regex = Regex::new(REGEX).unwrap();
    // prepend `do()` to enable at start
    let inp = format!("{}{}{}", "do()", raw, "don't()");
    let ret = re
        .captures_iter(&inp)
        .map(|caps| parse_input(caps.get(1).unwrap().as_str()))
        .flatten()
        .collect();
    ret
}

fn part1(parsed: &Parsed) -> usize {
    parsed.iter().map(|x| x.0 * x.1).sum()
}

fn part2(parsed: &Parsed) -> usize {
    parsed.iter().map(|x| x.0 * x.1).sum()
}

fn main() {
    let raw_input = read_file(DAY);
    let input = parse_input(&raw_input);
    println!("Part 1: {}", part1(&input));
    let input2 = parse_input2(&raw_input);
    println!("Part 2: {}", part2(&input2));
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str =
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
    const TEST_INPUT2: &str =
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";

    #[test]
    fn test_part1() {
        let input = parse_input(TEST_INPUT);
        assert_eq!(part1(&input), 161);
    }

    #[test]
    fn test_part1_own_input() {
        let input = parse_input(&read_file(DAY));
        // This is the correct answer
        assert_eq!(part1(&input), 175615763);
    }

    #[test]
    fn test_part2() {
        let input = parse_input2(TEST_INPUT2);
        assert_eq!(part2(&input), 48);
    }

    #[test]
    fn test_part2_own_input() {
        let input = parse_input2(&read_file(DAY));
        // These are all the wrong answers I've tried
        assert_ne!(part2(&input), 48450967);
        assert_ne!(part2(&input), 40153637);
        // This is the correct answer
        assert_eq!(part2(&input), 74361272);
    }

    #[bench]
    fn bench_parse(b: &mut test::Bencher) {
        let raw = &read_file(DAY);
        b.iter(|| parse_input(test::black_box(&raw)));
    }

    #[bench]
    fn bench_parse2(b: &mut test::Bencher) {
        let raw = &read_file(DAY);
        b.iter(|| parse_input2(test::black_box(&raw)));
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
        let input = parse_input2(&raw);
        b.iter(|| part2(test::black_box(&input)));
    }
}
