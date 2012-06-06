cpms :: Double       -- clocks per millisecond
cpms = 10 ^ (9::Int)

sqre_diff :: Double -> Double -> Double
sqre_diff x y = (x - y) ^ (2::Int)

main :: IO ()
main =
    putStrLn "Test.hs" >>
    putStrLn "Done."
