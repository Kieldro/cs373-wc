-- ------------
-- Operators.hs
-- ------------

{-
(>>)     :: IO a   -> IO b -> IO b  -- 'then' operator
assert   :: Bool   -> a    -> a
putStrLn :: String         -> IO ()
return   :: a              -> IO a
-}

import Control.Exception (assert)
import Data.Bits         ((.&.), (.|.), complement, shift, xor)

main :: IO ()
main =
    putStrLn "Operators.hs" >>

    (
    let i, j :: Int
        i = 2
        j = -i                    -- negation
    in assert (j == -2) return ()
    ) >>

    (
    let i, j, k :: Int
        i = 2
        j = 3
        k = i + j                -- addition: (+) i j
    in assert (k == 5) return ()
    ) >>

    (
    let i, j, k :: Int
        i = 12
        j = 10
        k = div i j              -- integer division: k = i `div` j
    in assert (k == 1) return ()
    ) >>

    (
    let f, g, h :: Float
        f = 12
        g = 10
        h = f / g                  -- float division
    in assert (h == 1.2) return ()
    ) >>

    (
    let i, j, k :: Int
        i = 12
        j = 10
        k = mod i j              -- integer mod
    in assert (k == 2) return ()
    ) >>

    (
    let i, j, k :: Int
        i = 2
        j = 3
        k = i ^ j                -- integer, integer power
    in assert (k == 8) return ()
    ) >>

    (
    let f, h :: Float
        j    :: Int
        f = 2
        j = 3
        h = f ^^ j               -- integer, float power
    in assert (h == 8) return ()
    ) >>

    (
    let f, g, h :: Float
        f = 2
        g = 3
        h = f ** g               -- float, float power
    in assert (h == 8) return ()
    ) >>

    (
    let i, j, k :: Int
        i = 2
        j = 3
        k = shift i j            -- bit shift left
    in assert (k == 16) return ()
    ) >>

    (
    let i, j, k :: Int
        i = 16
        j = -3
        k = shift i j            -- bit shift right
    in assert (k == 2) return ()
    ) >>

    (
    let i, j, k :: Int
        i = 10
        j = complement i              -- bit complement
        k = j + 1
    in assert (j == -11) return () >>
       assert (k == -10) return ()
    ) >>

    (
    let i, j, k :: Int
        i = 10                   -- 1010
        j = 12                   -- 1100
        k = i .&. j              -- 1000: bit and
    in assert (k == 8) return ()
    ) >>

    (
    let i, j, k :: Int
        i = 10                    -- 1010
        j = 12                    -- 1100
        k = i .|. j               -- 1110: bit or
    in assert (k == 14) return ()
    ) >>

    (
    let i, j, k :: Int
        i = 10                   -- 1010
        j = 12                   -- 1100
        k = xor i j              -- 0110: bit exclusive or
    in assert (k == 6) return ()
    ) >>

    (
    let a, b, c :: Bool
        a = True
        b = True
        c = False
    in assert (a && b)                                 return () >>
       assert (not (a && c))                           return () >>
       assert (a || b)                                 return () >>
       assert (a || c)                                 return () >>
       assert ((a && b) == (not ((not a) || (not b)))) return () >>
       assert ((a && c) == (not ((not a) || (not c)))) return ()
    ) >>

    (
    let s, t, u :: String
        s = "a"
        t = "bc"
        u = s ++ t                   -- string concatenation
    in assert (u == "abc") return ()
    ) >>

    (
    let x, y :: [Int]
        i    :: Int
        i = 2
        x = [3, 4]
        y = i : x                        -- list constructor
    in assert (y == [2, 3, 4]) return ()
    ) >>

    (
    let x :: [Int]
        x =  [2..5]                         -- list constructor
    in assert (x == [2, 3, 4, 5]) return ()
    ) >>

    (
    let x, y, z :: [Int]
        x = [2]
        y = [3, 4]
        z = x ++ y                       -- list concatenation
    in assert (z == [2, 3, 4]) return ()
    ) >>

    (
    let x :: [Int]
        i :: Int
        x =  [2, 3, 4]
        i =  x !! 1              -- list index
    in assert (i == 3) return ()
    ) >>

    putStrLn "Done."
