;;Write a function called isPrime, that takes in a positive integer and returns
;;True if number is Prime, otherwise false
;;
;;Input: isPrime(10)
;;Output: False
;;
;;Input: isPrime(13)
;;Output: True

(defn isPrime [x]
  (let [divisors (filter #(zero? (mod x %)) (range 1 x))]
   (= 1 (count divisors))))

(println (isPrime 1))
(println (isPrime 2))
(println (isPrime 10))
(println (isPrime 13))
