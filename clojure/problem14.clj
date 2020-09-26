;; Write a function called uniqueVals that will return an array of unique values,
;; no duplicates allowed. It will accept 2 arguments, the first will be the
;; desired length of the returned array and the second will the be the max value
;; in the random set.
;;
;; Input: uniqueVals(5,10)
;; Possible Output: [1,7,3,9,2]

;; 09/25/2020

(defn uniqueVals [lenght max-val]
  (take lenght (shuffle (range 1 max-val))))

(println (uniqueVals 5 10))
