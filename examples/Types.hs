-- --------
-- Types.hs
-- --------

{-
(>>)     :: IO a   -> IO b -> IO b  -- 'then' operator
(==)     :: a      -> a    -> Bool
assert   :: Bool   -> a    -> a
putStrLn :: String         -> IO ()
return   :: a              -> IO a
-}

import Control.Exception (assert)

data A a
    = A Int Double a
    deriving (Eq)

data Color
    = Red
    | Blue
    | Green
    deriving (Eq)

main :: IO ()
main =
    putStrLn "Types.hs" >>

    let bf :: Bool
        bf = False
    in assert (bf == False) return () >>

    let bt :: Bool
        bt = True
    in assert (bt == True) return () >>

    let c :: Char
        c = 'a'
    in assert (c == 'a') return () >>

    let i :: Int                    -- fixed-precision
        i = 2
    in assert (i == 2) return () >>

    let ia :: Integer                -- arbitrary-precision
        ia = 3
    in assert (ia == 3) return () >>

    let f :: Float                    -- single-precision
        f = 4.5
    in assert (f == 4.5) return () >>

    let d :: Double                   -- double-precision
        d = 6.7
    in assert (d == 6.7) return () >>

    let s :: String
        s = "abc"
    in assert (s == "abc") return () >>

    let l :: [Int]                          -- list
        l = [2, 3, 4]
    in assert (l == [2, 3, 4]) return () >>

    let t :: (Char, Double, [Int])                -- tuple
        t = ('a', 2.3, [4])
    in assert (t == ('a', 2.3, [4])) return () >>

    let x :: A Int
        x = A 2 3.45 6
    in assert (x == A 2 3.45 6) return () >>

    let y :: A Double
        y = A 2 3.45 6.78
    in assert (y == A 2 3.45 6.78) return () >>

    let inc :: Int -> Int
        inc n = n + 1
    in assert ((inc 2) == 3) return ()  >>

    let cl :: Color
        cl = Red
    in assert (cl == Red) return () >>

    putStrLn "Done."
