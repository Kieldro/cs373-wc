-- -------------
-- Assertions.hs
-- -------------

{-
Turn OFF assertions at compile time with -fignore-asserts or -O
% ghc -fignore-asserts -Wall Assertions.hs -o Assertions.hs.app
% ghc -O               -Wall Assertions.hs -o Assertions.hs.app
% Assertions.hs.app
-}

{-
(>>)     :: IO a   -> IO b -> IO b  -- 'then' operator
assert   :: Bool   -> a    -> a
putStrLn :: String         -> IO ()
return   :: a              -> IO a
-}

import Control.Exception (assert)

cycle_length :: Int -> Int
cycle_length n
    | n         == 1  =  0
    | (mod n 2) == 0  =  1 + cycle_length (div n 2)
    | otherwise       =  1 + cycle_length ((3 * n) + 1)

main1 :: IO ()
main1 =
    putStrLn "Assertions.hs" >>

    assert ((cycle_length 1) == 1) return () >>
    assert ((cycle_length 5) == 6) return () >>

    putStrLn "Done."

main2 :: IO ()
main2 = do
    putStrLn "Assertions.hs"

    assert ((cycle_length 1) == 1) return ()
    assert ((cycle_length 5) == 6) return ()

    putStrLn "Done."

main :: IO ()
main = main1

{-
Assertions.hs
Assertions.hs.app: Assertions.hs:31:5-10: Assertion failed
-}

{-
Assertions.hs
Assertions.hs.app: Assertions.hs:40:5-10: Assertion failed
-}
