import Control.Exception (assert)

main :: IO ()
main = do
    putStrLn "Operators.hs"

    (
    let i, j :: Int
        i = 2
        j = -i                 -- negation
    assert (j == -2) return ()
    )

    (
    let i, j, k :: Int
        i = 2
        j = 3
        k = i + j             -- addition: (+) i j
    assert (k == 5) return ()
    )

    putStrLn "Done."
