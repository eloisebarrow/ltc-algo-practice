;;Given an array of strings, return another array containing all of its longest strings.
;;
;;Input: ["aba", "aa", "ad", "vcd", "aba"]
;;Output: ["aba", "vcd", "aba"]
;;
;; 09/11/20

(defn getLongestStrings [strlist]
  (let [maxlen (reduce max (map count strlist))]
    (vec (filter #(= maxlen (count %)) strlist))))

(println (getLongestStrings ["aba", "aa", "ad", "vcd", "aba"]))
