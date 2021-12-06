use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut file = File::open("input.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    let readings: Vec<i64> = contents.split("\n").map(|x| x.parse::<i64>().unwrap()).collect();
    let mut c : i64 = 0;
    let mut prevSum: i64 = readings[0] + readings[1];
    let mut nextSum: i64 = readings[1] + readings[2];
    for i in 0..readings.len()-3 {
        prevSum += readings[i+2];
        nextSum += readings[i+3];
        if nextSum > prevSum {
            c+=1;
        }
        prevSum -= readings[i];
        nextSum -= readings[i+1];
    }
    println!("{:?}", c);
    Ok(())
}