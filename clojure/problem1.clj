;; Given a two-digit integer, return the sum of its digits.
;; 09/08
(defn add_digits [x]
  (let [left (quot x 10)
        right (mod x 10)]
    (+ left right)))

(println (add_digits 29))
(println (add_digits 30))
