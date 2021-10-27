use std::io::{self, Read};

//read lines from stdin and return a vector
fn readlines() -> Vec<String> {
    use std::io::prelude::*;
    let stdin = std::io::stdin();
    let v = stdin.lock().lines().map(|x| x.unwrap()).collect();
    v
}

fn main() {
    let mut values = readlines();
    println!("{}", values.len())

    // let values = input.split_whitespace().map(|x| x.parse::<i32>()).collect::<Result<Vec<i32>, _>>().unwrap();

    assert!(values.len() == 2);
    let b : i32 = values[0];
    let a : i32 = values[1];

    let mut with_clock =  360 - b;
    let mut against_clock = b;

    if a > b {
        with_clock -= 360 - a;
        against_clock += 360 - a;
    } else if b > a {
        with_clock += a;
        against_clock -= a;
    } else {
        println!("{}", 180);
    }

    // println!("with={}, against={}", with_clock, against_clock);

    if with_clock < against_clock {
        println!("{}", with_clock)
    } else {
        println!("{}", - against_clock)
    }
}
