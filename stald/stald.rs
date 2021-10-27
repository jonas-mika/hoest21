use std::io::{self, Read};

fn main() -> io::Result<()> {
    let mut buffer = String::new();
    let mut stdin = io::stdin(); // We get `Stdin` here.
    stdin.read_to_string(&mut buffer)?;
    let lines = buffer.lines();

    let mut c = 0;
    let mut counts = vec![0];
    for line in lines {
        if line == "Får ind" {
            c += 1;
        } else {
            c -= 1;
        }
        counts.push(c);
    }
    println!("{}", counts.iter().max().unwrap() - counts.iter().min().unwrap());

    Ok(())
}
