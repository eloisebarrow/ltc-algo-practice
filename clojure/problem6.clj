;; Write a function called printArr that will print the items of an array.
;;
;; Input: ['sally','monique','caleb']
;; Output:
;;
;; sally
;; monique
;; caleb

(defn printArr [input]
  (doseq [item input]
    (println item)))

(printArr ["sally", "monique", "caleb"])

