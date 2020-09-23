;; Write a function called hasVowels that takes in an array of words and
;; returns a new array of only those words that contain one or more vowels.
;;
;; Input: hasVowels(['jon', 'ada', 'ppzpp', 'brgggg', 'eric'])
;; Output: ['jon', 'ada', 'eric']

;; 09/23/2020

(defn hasVowels
  [words]
  (vec (filter #(some (set "aeiou") %) words)))

(println (hasVowels ["jon" "ada" "ppzpp" "brgggg" "eric"]))
