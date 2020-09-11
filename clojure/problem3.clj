;; Anagram
;; isAnagram("cinema", "iceman") == True
;; isAnagram("randum" "werdz") == False
;; 09/10/20

(defn isAnagram [s1, s2]
  (let [sorted1 (sort s1)
        sorted2 (sort s2)]
    (= sorted1 sorted2)))

(println (isAnagram "cinema" "iceman"))
(println (isAnagram "randum" "werdz"))
