-- Prime wheels

data Wheel = Wheel Integer [Integer] deriving (Show)
w0 = Wheel 1 [1]

roll (Wheel n rs) = [n*k+r | k <- [0..], r <- rs]
rollTill (Wheel n rs) m = [n*k+r | k <- [0..m], r <- rs]
nextWheelSize (Wheel n rs) p = Wheel (p*n) [r2 | k <- [0..(p-1)], r <- rs, let r2 = n*k+r, r2 `mod` p /= 0]
genWheel ds = foldl nextWheelSize w0 ds


-- Sieve
sieve :: [Integer] -> [Integer]
sieve [] = []
sieve (x:xs)
    | x < 2     = sieve xs
    | otherwise = x : sieve (filter (\n -> n `mod` x /= 0) xs)

main :: IO ()
main = do
    putStrLn "----- Problem 7 -----"
    let wheelPrimes = [2,3,5,7,11]
    let wheel = genWheel wheelPrimes
    putStrLn (show (sieve (wheelPrimes ++ (rollTill wheel 1000000))))
    -- putStrLn (show ((sieve )))

{-
-- This is a very slow implementation
sieve :: [Int] -> [Int]
sieve (p:ps) = p : sieve [x | x <- ps, x `mod` p > 0]

primes :: [Int]
primes = sieve [2..]

main :: IO ()
main = do
    putStrLn "----- Problem 7 -----"
    putStrLn (show (primes !! 10000))
-}

