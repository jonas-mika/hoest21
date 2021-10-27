use std::io::{self, Read};

fn main() -> io::Result<()> {
    let mut buffer = String::new();
    let stdin  = io::stdin(); // We get `Stdin` here.
    stdin.read_line(&mut buffer)?;

    println!("{}", )
    
    let n = buffer.parse::<i32>().unwrap(); 
    println!("{}", n);

    Ok(())
}
