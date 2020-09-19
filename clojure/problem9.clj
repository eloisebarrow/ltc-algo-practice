;;Create a function called findMissingNums that takes in two arrays. Iterate over
;;the first array and the number you are iteratring over is NOT present in the
;;second array, push the number into it. Once the loop is complete return the
;;second array.
;;
;;Input: [0,1,2,3,4,5,6,7,8,9], [2,3,7,9]
;;Output: [ 2, 3, 7, 9, 0, 1, 4, 5, 6, 8 ]

;;09/18/20

(defn findMissingNums [a b]
  (let [a (filter #(not (contains? (set b)  %)) a)]
    (vec (concat b a))))

(println (findMissingNums [0 1 2 3 4 5 6 7 8 9] [2 3 7 9]))
