main :: IO ()
main = do
    putStrLn "Test.hs"

    (
    let s :: String
        s = "abc"
    putStrLn s
    )

    (
    let s :: String
        s = "def"
    putStrLn s
    )

    putStrLn "Done."
