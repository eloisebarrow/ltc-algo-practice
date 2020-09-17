;; Write a function called isPalindrome that, given a string, returns true
;; if the string is a palindrome, and false if not
;;
;; Input: isPalindrome("tacocat")
;; Output: True
;;
;; Input: isPalindrome("nottacocat")
;; Output: False


;; Additional levels of difficulty:
;; Input: isPalindrome("Race car")
;; Output: True

;;Input: isPalindrome("a man, a plan, a canal - panama")
;;Output: True

;;  09/16/20
(require '[clojure.string :as str])

(defn isPalindrome [s]
  (let [s (->> s str/lower-case
                (filter #(<= 97 (int %) 122))
                (vec)
                (apply str))]
    (= s (apply str (reverse s)))))


(println (isPalindrome "tacocat"))
(println (isPalindrome "nottacocat"))
(println (isPalindrome "Race car"))
(println (isPalindrome "a man, a plan, a canal - panama"))
