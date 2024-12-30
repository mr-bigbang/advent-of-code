#![feature(test)]
extern crate test;

use advent_of_code::read_file;

const DAY: usize = 02;
type T = usize;
type Parsed = Vec<Vec<T>>;

fn split_nums(line: &str) -> Vec<usize> {
    line.split(" ")
        .map(|x| x.parse::<usize>().unwrap())
        .collect()
}

fn parse_input(raw: &str) -> Parsed {
    raw.lines().map(split_nums).collect()
}

fn correct_spacing(row: &Vec<usize>) -> bool {
    for i in 0..row.len() -1 {
        if !(1..=3).contains(&row[i].abs_diff(row[i+1])) {
            return false
        }
    }
    true

    /*for i in 0..row.len() -1 {
        let diff = row[i].abs_diff(row[i + 1]);
        if diff >= 1 && diff <= 3 {
            continue
        } else {
            return false
        }
    }
    true*/
}

fn is_safe(row: &Vec<usize>) -> bool {
    if !correct_spacing(row) {
        return false;
    }
    if row.is_sorted() {
        return true;
    }
    if row.iter().rev().is_sorted() {
        return true;
    }
    false
}

fn is_safe_with_dampener(row: &Vec<usize>) -> bool {
    todo!()
}

fn part1(parsed: &Parsed) -> usize {
    parsed.iter().filter(|&x| is_safe(x)).count()
}

fn part2(parsed: &Parsed) -> usize {
    parsed.iter().filter(|&x| is_safe_with_dampener(x)).count()
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

    const TEST_INPUT: &str = "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9";

    #[test]
    fn test_part1() {
        let input = parse_input(TEST_INPUT);
        assert_eq!(part1(&input), 2);
    }

    #[test]
    fn test_part2() {
        let input = parse_input(TEST_INPUT);
        assert_eq!(part2(&input), 4);
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

    #[test]
    fn test_correct_spacing() {
        assert!(correct_spacing(&vec![1, 3, 6, 7, 9]));
        assert!(!correct_spacing(&vec![1, 2, 7, 8, 9]));
        assert!(!correct_spacing(&vec![9, 7, 6, 2, 1]));
    }
}
