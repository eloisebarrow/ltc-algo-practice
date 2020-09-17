;; Write a function called likes which takes in an array, containing the names of people who like an item. It must return the display text as shown in the examples and is dependent on the number of elements in the array.
;;
;; Input: likes([])
;; Output: "no one likes this"
;;
;; Input: likes(["Peter"])
;; Output: "Peter likes this"
;;
;; Input: likes(["Jacob", "Alex"])
;; Output: "Jacob and Alex like this"
;;
;; Input: likes(["Max", "John", "Mark"])
;; Output: "Max, John and Mark like this"
;;
;; Input: likes(["Alex", "Jacob", "Mark", "Max"])
;; Output: "Alex, Jacob and 2 others like this"

;; 09/17/20

(defn likes [x]
  (let [len (count x)
        names (cond
                (= len 0) "no one likes"
                (= len 1) (str (first x) " likes")
                (= len 2) (str (nth x 0) " and " (nth x 1) " like")
                (= len 3) (str (nth x 0) ", " (nth x 1) " and " (nth x 2) " like")
                :else (str (nth x 0) ", " (nth x 1) " and " (- len 2) " others like"))]
    (str names " this")))

(println (likes []))
(println (likes ["Peter"]))
(println (likes ["Jacob" "Alex"]))
(println (likes ["Max" "John" "Mark"]))
(println (likes ["Alex" "Jacob" "Mark" "Max"]))
