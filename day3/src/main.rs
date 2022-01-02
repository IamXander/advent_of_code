// source $HOME/.cargo/env

use std::fs::File;
use std::io::prelude::*;

fn ms(readings: &mut Vec<&str>, first: usize, last: usize, depth: usize) -> usize{
    if first >= last {
        return last;
    }
    match readings[first].chars().nth(depth).unwrap() {
        '1' => {
            match readings[first].chars().nth(depth).unwrap() {
                '1' => return ms(readings, first, last - 1, depth),
                '0' => {
                    readings.swap(first, last);
                    return ms(readings, first - 1, last - 1, depth);
                },
                _ => panic!("something else!"),
            }
        },
        '0' => return ms(readings, first + 1, last, depth),
        _ => panic!("something else!"),
    }
}

fn main() -> std::io::Result<()> {
    let mut file = File::open("input.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    let readings: Vec<&str> = contents.split("\n").collect();
    let mut vals: Vec<i64> = vec![0; readings[0].len()];
    for reading in readings {
        for i in 0..reading.len() {
            match reading.chars().nth(i).unwrap() {
                '1' => vals[i] += 1,
                '0' => vals[i] -= 1,
                _ => panic!("something else!"),
            }
        }
    }
    let mut epsilon: i64 = 0;
    let mut gamma: i64 = 0;
    for v in vals {
        if v > 0 { // There were more 1s
            epsilon = epsilon << 1;
            gamma = (gamma << 1) + 1;
        } else {
            epsilon = (epsilon << 1) + 1;
            gamma = (gamma << 1);
        }
    }
    println!("{:?}", epsilon*gamma);
    Ok(())
}