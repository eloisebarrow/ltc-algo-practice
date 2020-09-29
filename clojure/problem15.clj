
;;Write a function called greatestCommomFactor that, given two distinct positive
;;integers, returns the greatest common factorof those two values
;;
;;Input: greatestCommonFactor(9,12)
;;Output: 3
;;
;;Input: greatestCommonFactor(6,18)
;;Output: 6
;;
;;Input: greatestCommonFactor(7,11)
;;Output: 1

(require '[clojure.set :as s])

(defn greatestCommonFactor [x y]
 (let [xfactor (filter #(zero? (mod x %)) (range 1 (inc x)))
       yfactor (filter #(zero? (mod y %)) (range 1 (inc y)))]
  ;(max (clojure.set/intersection (set xfactor) (set yfactor)))))
  (apply max (s/intersection (set xfactor) (set yfactor)))))

(println (greatestCommonFactor 9 12))
(println (greatestCommonFactor 6 18))
(println (greatestCommonFactor 7 11))
