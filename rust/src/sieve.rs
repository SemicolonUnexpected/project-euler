fn sieve(i32 n) -> Vec<i32> {
    let half: i32 = (n / 2.0).floor();
    let mut nums: Vec<bool> = vec![true; half];
    for i in 
