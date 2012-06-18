-- ------------
-- Selection.hs
-- ------------

{-
(>>)     :: IO a   -> IO b -> IO b -- 'then' operator
assert   :: Bool   -> a    -> a
putStrLn :: String         -> IO ()
return   :: a              -> IO a
-}

import Control.Exception (assert)

f :: Int -> Int
f n =
    if n < 0 then
        -1
    else if n > 0 then
        1
    else
        0

g :: Int -> Int
g n
    | n < 0     = -1
    | n > 0     =  1
    | otherwise =  0

h :: Int -> Int
h (-2) = -1
h   3  =  1
h   _  =  0

x :: Int -> Int
x n =
    case n of
        -2 -> -1
        3  ->  1
        _  ->  0

main :: IO ()
main =
    putStrLn "Selection.hs" >>

    assert ((f (-2)) == -1) return () >>
    assert ((f   0 ) ==  0) return () >>
    assert ((f   3 ) ==  1) return () >>

    assert ((g (-2)) == -1) return () >>
    assert ((g   0 ) ==  0) return () >>
    assert ((g   3 ) ==  1) return () >>

    assert ((h (-2)) == -1) return () >>
    assert ((h   0 ) ==  0) return () >>
    assert ((h   3 ) ==  1) return () >>

    assert ((x (-2)) == -1) return () >>
    assert ((x   0 ) ==  0) return () >>
    assert ((x   3 ) ==  1) return () >>

    putStrLn "Done."
