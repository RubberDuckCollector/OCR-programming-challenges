fn fact_it(n: u128) -> u128 {
    let mut counter = 1;

    for i in 1..n + 1 {
        counter = counter * i;
    }
    return counter;
}

fn fact_rec(n: u128) -> u128 {
    if n == 1 {
        1
    } else {
        n * fact_rec(n - 1)
    }
}

fn main() {
    println!("{}", fact_it(10));

    println!("{}", fact_rec(10));
}
