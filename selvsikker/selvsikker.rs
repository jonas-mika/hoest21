use std::io::{self, BufRead};

fn main () {
    let mut input = String::new();
    io::stdin().lock().read_line(&mut input).unwrap();

    let str_arr: Vec<&str> = input.split(' ').collect();
    println!("size: {}", str_arr.len());
}
