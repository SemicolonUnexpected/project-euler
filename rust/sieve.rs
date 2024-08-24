fn main() {
    sieve(100);
}

fn sieve(n: u32) {
    let half: usize = n >> 1;
    let mut nums = [true; half];
    for i in 0..half {
        println!("{0}", i);
    }
}
