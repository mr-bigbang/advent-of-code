#![feature(test)]
extern crate test;

use advent_of_code::read_file;

const DAY: usize = 01;
type T = usize;
type Parsed = (Vec<T>, Vec<T>);

fn parse_input(raw: &str) -> Parsed {
    let (mut v1, mut v2): Parsed = raw
        .lines() // split at EOL
        .filter_map(|l| l.split_once("   ")) // shorthand for filter().map()
        .map(|(a, b)| (a.parse::<usize>().unwrap(), b.parse::<usize>().unwrap())) // parse into numbers
        .unzip(); // opposite of zip()

    // sort_unstable() seems to be faster than sort()
    v1.sort_unstable();
    v2.sort_unstable();

    (v1, v2)
}

fn part1((l, r): &Parsed) -> usize {
    l.iter() // turn left Vec<> into an iterator
        .zip(r) // zip with right Vec
        .map(|(&a, &b)| a.abs_diff(b)) // get the diff for each pair, ignoring sign
        .sum() // sum it all up
}

fn part2((l, r): &Parsed) -> usize {
    l.iter()
        .map(|i| i * r.iter().filter(|&x| x == i).count())
        .sum()
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

    const TEST_INPUT: &str = "3   4
4   3
2   5
1   3
3   9
3   3";

    #[test]
    fn test_part1() {
        let input = parse_input(TEST_INPUT);
        assert_eq!(part1(&input), 11);
    }

    #[test]
    fn test_part2() {
        let input = parse_input(TEST_INPUT);
        assert_eq!(part2(&input), 31);
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
}
