-- --------------
-- StackVsHeap.hs
-- --------------

{-
(>>)     :: IO a   -> IO b        -> IO b  -- 'then' operator
assert   :: Bool   -> a           -> a
catch    :: IO a   -> (e -> IO a) -> IO a
error    :: [Char]                -> a
putStrLn :: String                -> IO ()
return   :: a                     -> IO a
show     :: a                     -> String
-}

import Control.Exception (assert, catch, SomeException)

f :: Int -> Int
f n
    | n == 0     =  0
    | otherwise  =  1 + f (n - 1)

handler1 :: SomeException -> IO ()
handler1 _ = assert False return ()

handler2 :: SomeException -> IO ()
handler2 e = assert ((show e) == "stack overflow") return ()

main :: IO ()
main = do
    putStrLn "StackVsHeap.hs"

    Control.Exception.catch (assert ((f 123456)  == 123456)  return ()) handler1
    Control.Exception.catch (assert ((f 1234567) == 1234567) return ()) handler2

    putStrLn "Done."
