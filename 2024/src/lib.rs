pub fn read_file(day: usize) -> String {
    let filepath = format!("./inputs/input{:02}.txt", day);
    std::fs::read_to_string(filepath).unwrap()
}
