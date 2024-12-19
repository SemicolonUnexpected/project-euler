{-

(1): O
= 1

(2): OO
     O O
= 2

(3): OOO
     OO O
     O O O
= 3

(4): OOOO
     OOO O
     OO O O
     OO OO
     O O O O
= 5

(5): OOOOO
     OOOO O
     OOO OO
     OOO O O
     OO OO O
     OO O O O
     O O O O O
= 7

(6): OOOOOO
     OOOOO O
     OOOO O O
     OOO OO O
     OOO O O O
     OO OO O O
     OO O O O O
     O O O O O O
     OOOO OO
     OO OO OO
     OOO OOO
 -}

partition :: Integer -> Integer
partition 1 = 1
partition x = 1 + partition (x - 1)

Main :: IO ()
main = do
   putStrLn "----- Problem 78 -----"
