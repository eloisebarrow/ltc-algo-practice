;; Write a function called stringCompress that, given a string, returns a
;; string that represents a numerically compressed format of the string.
;;
;; Input: stringCompress("abbcccdddde")
;; Output: "a2b3c4de"
;;
;; Input: stringCompress("abcd")
;; Output: "abcd"

(defn stringCompress [x]
  (let [p (partition-by identity x)
        m (map #(str (count %) (first %)) p)
        s (apply str m)
        f (clojure.string/replace s "1" "")]
    f))
(println (stringCompress "abbcccdddde"))
(println (stringCompress "abcde"))
