#![feature(test)]
extern crate test;

use advent_of_code::read_file;

const DAY: usize = 04;
type T = u8;
type Parsed = Vec<Vec<T>>;

fn parse_input(raw: &str) -> Parsed {
    raw.lines().map(|x| x.bytes().collect()).collect()
}

fn part1(parsed: &Parsed) -> usize {
    for row in parsed {
        for &column in row {
            if column == b'X' {
                continue;
            }
        }
    }
    todo!()
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

    const TEST_INPUT: &str = "MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX";

    #[test]
    fn test_part1() {
        let input = parse_input(TEST_INPUT);
        assert_eq!(part1(&input), 18);
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
}
