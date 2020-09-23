;; Write a function called twoSum that given an array of integers and a target
;; number, returns two array integers that add up to the target.
;;
;; Input: [3, 2, 5, 7, 11, 15], 9
;; Output: Return [2, 7]
;; 09/22/2020

(defn twoSum
  [nums target]
  (vec (filter #(.contains nums (- target %)) nums)))

(println (twoSum [3 2 5 7 11 15] 9))
