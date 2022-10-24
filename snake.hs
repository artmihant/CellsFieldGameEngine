module Coins where

import Data.List

-- -- Функция принимает список номиналов монет, денежную сумму и количество. Возвращает список пар (номинал, количество)
-- splitCoins :: [Int] -> Int -> Int -> [[(Int, Int)]]

-- -- Сперва сортируем монетки в обратном порядке
-- splitCoins cs p n = splitSortCoins (reverse sort cs) p n
--     where
splitSortCoins :: [Int] -> Int -> Int -> [[(Int, Int)]]
splitSortCoins [] _ _ = []

-- в случае одного типа монет всё понятно
splitSortCoins [c] p n = if n*c == p then [[(c, n)]] else []
splitSortCoins (c:cx) p n
    | p <= 0 = []
    | n <= 0 = []
    | True = let
            -- узнаем возможный максимум наибольших по номиналу монет
            maxBigestCoin = min (div p c) n

            -- функция возвращает раскладки в том случае, если фиксировано число наибольших монет
            splitCoinsFixBigest :: Int -> [[(Int, Int)]]
            splitCoinsFixBigest i = xsumm (c,i) $ splitSortCoins cx (p-c*i) (n-i)

            xsumm ::  a -> [[a]] -> [[a]]
            xsumm  _ [] = []
            xsumm a (c:cs) = (a:c):(xsumm a cs)

        in  foldr (++) [] $ map splitCoinsFixBigest [0..maxBigestCoin]


