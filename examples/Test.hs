main :: IO ()
main = do
    putStrLn "Test.hs"

    (let s = "abc" in
        putStrLn s)

    (let s = "def" in
        putStrLn s)

    putStrLn "Done."
