-- --------
-- Lists.hs
-- --------

{-
(>>)     :: IO a   -> IO b -> IO b  -- 'then' operator
(==)     :: a      -> a    -> Bool
(!!)     :: [a]    -> Int  -> a
(:)      :: a      -> [a]  -> [a]
(++)     :: [a]    -> [a]  -> [a]
assert   :: Bool   -> a    -> a
drop     :: Int    -> [a]  -> [a]
elem     :: a      -> [a]  -> Bool
head     :: [a]            -> a
init     :: [a]            -> [a]
last     :: [a]            -> a
length   :: [a]            -> Int
null     :: [a]            -> Bool
putStrLn :: String         -> IO ()
return   :: a              -> IO a
reverse  :: [a]            -> [a]
tail     :: [a]            -> [a]
take     :: Int    -> [a]  -> [a]
-}

import Control.Exception (assert)

a :: [Int]
a = []

b :: [Int]
b = [2, 3, 4]

main :: IO ()
main =
    putStrLn "Lists.hs" >>

    assert (a == [])        return () >>
    assert (b == [2, 3, 4]) return () >>

    assert ((null a) == True)  return () >>
    assert ((null b) == False) return () >>

    assert ((length a) == 0) return () >>
    assert ((length b) == 3) return () >>

--  assert ((head a) == 0) return () >> -- Prelude.head: empty list
    assert ((head b) == 2) return () >>

--  assert ((last a) == 0) return () >> -- Prelude.head: empty list
    assert ((last b) == 4) return () >>

--  assert ((init a) == [])     return () >> -- Prelude.head: empty list
    assert ((init b) == [2, 3]) return () >>

--  assert ((tail a) == [])     return () >> -- Prelude.head: empty list
    assert ((tail b) == [3, 4]) return () >>

    assert ((take 0 a) == [])     return () >>
--  assert ((take 1 a) == [])     return () >> -- Prelude.head: empty list
    assert ((take 2 b) == [2, 3]) return () >>

    assert ((drop 0 a) == [])     return () >>
--  assert ((drop 1 a) == [])     return () >> -- Prelude.head: empty list
    assert ((drop 1 b) == [3, 4]) return () >>

--  assert ((a !! 0) == 0) return () >> -- Prelude.(!!): index too large
    assert ((b !! 0) == 2) return () >>
--  assert ((b !! 3) == 5) return () >> -- Prelude.(!!): index too large

    assert ((elem 3 b) == True)  return () >>
    assert ((elem 5 b) == False) return () >>

    assert ((1 : a) == [1])          return () >>
    assert ((1 : b) == [1, 2, 3, 4]) return () >>

    assert (([1] ++ a) == [1])          return () >>
    assert (([1] ++ b) == [1, 2, 3, 4]) return () >>

    assert ((reverse a) == [])        return () >>
    assert ((reverse b) == [4, 3, 2]) return () >>

    assert ([x * 2 | x <- a] == [])        return () >>
    assert ([x * 2 | x <- b] == [4, 6, 8]) return () >>

    assert ([x * 2 | x <- a, even x] == [])     return () >>
    assert ([x * 2 | x <- b, even x] == [4, 8]) return () >>

    putStrLn "Done."
