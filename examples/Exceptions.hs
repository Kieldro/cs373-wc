-- -------------
-- Exceptions.hs
-- -------------

{-
assert   :: Bool   -> a           -> a
catch    :: IO a   -> (e -> IO a) -> IO a
error    :: [Char]                -> a
putStrLn :: String                -> IO ()
return   :: a                     -> IO a
show     :: a                     -> String
-}

import Control.Exception (assert, catch, SomeException)

f :: Bool -> Int
f False = 0
f True  = error "abc"

handler1 :: SomeException -> IO ()
handler1 _ = assert False return ()

handler2 :: SomeException -> IO ()
handler2 e = assert ((show e) == "abc") return ()

main :: IO ()
main = do
    putStrLn "Exceptions.hs"

    Control.Exception.catch (assert ((f False) == 0) return ()) handler1
    Control.Exception.catch (assert ((f True)  == 1) return ()) handler2

    putStrLn "Done."
