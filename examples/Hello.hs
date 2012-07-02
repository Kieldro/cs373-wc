-- --------
-- Hello.hs
-- --------

{-
% ghc -Wall Hello.hs -o Hello.hs.app
% Hello.hs.app
-}

{-
putStrLn :: String -> IO ()
-}

main :: IO ()
main = putStrLn "Nothing to be done."

{-
% ghci
GHCi, version 7.4.1: http://www.haskell.org/ghc/  :? for help
Loading package ghc-prim ... linking ... done.
Loading package integer-gmp ... linking ... done.
Loading package base ... linking ... done.
Prelude> :load Hello
[1 of 1] Compiling Main             ( Hello.hs, interpreted )
Ok, modules loaded: Main.
*Main> :t main
main :: IO ()
*Main> :t putStrLn
putStrLn :: String -> IO ()
*Main> main
Nothing to be done.
*Main> :quit
Leaving GHCi.
-}
