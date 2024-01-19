-- Quick implementation of Problem 1 through code to test my haskell

sumDiv :: Int -> Int
sumDiv 0 = 0
sumDiv x
   | x == 0 = 0
   | (x `mod` 3) == 0 = x + sumDiv (x - 1)
   | (x `mod` 5) == 0 = x + sumDiv (x - 1)
   | otherwise = sumDiv (x - 1)

main :: IO ()
main = do
    putStrLn "----- Problem 1 -----"
    putStrLn (show (sumDiv 999))

