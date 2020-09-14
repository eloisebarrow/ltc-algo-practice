;; Write a function called largestNumber that will return the largest value from an array.

;; Input: [1,2,5,10]
;; Output: 10

;; 09/14/2020

(defn largestNum [x]
  (reduce max x))

(println (largestNum [1, 2, 5, 10]))
