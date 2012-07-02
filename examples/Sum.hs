-- ------
-- Sum.hs
-- ------

{-
(+)      :: a             -> a        -> a
assert   :: Bool          -> a        -> a
foldl    :: (a -> b -> a) -> a -> [b] -> a
putStrLn :: String                    -> IO ()
return   :: a                         -> IO a
sum      :: [a]                       -> a
-}

import Control.Exception (assert)

sum_1 :: Num a => [a] -> a
sum_1 []       = 0
sum_1 (x : xs) = x + sum_1 xs

sum_2 :: Num a => [a] -> a
sum_2 a = foldl (+) 0 a

main :: IO ()
main = do
    putStrLn "Sum.hs"

    let a :: [Int]
        a = [2,  3,  4]
    assert ((sum_1 a) == 9) return ()
    assert ((sum_2 a) == 9) return ()
    assert ((sum   a) == 9) return ()

    putStrLn "Done."
