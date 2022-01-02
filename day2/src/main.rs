// source $HOME/.cargo/env

use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut file = File::open("input.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    let readings: Vec<&str> = contents.split("\n").collect();
    let mut h_pos : i64 = 0;
    let mut v_pos : i64 = 0;
    let mut aim : i64 = 0;
    for reading in readings {
        let split: Vec<&str> = reading.split(' ').collect();
        let x = split[1].parse::<i64>().unwrap();
        match split[0] {
            "down" => aim += x,
            "up" => aim -= x,
            "forward" => {
                h_pos += x;
                v_pos += aim * x;
            },
            _ => panic!("something else!"),
        }
    }
    println!("{:?}", v_pos*h_pos);
    Ok(())
}