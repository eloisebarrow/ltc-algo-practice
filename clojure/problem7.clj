;; Write a function called isPalindrome that, given a string, returns true
;; if the string is a palindrome, and false if not
;;
;; Input: isPalindrome("tacocat")
;; Output: True
;;
;; Input: isPalindrome("nottacocat")
;; Output: False
;; 09/16/20

(defn isPalindrome [s]
  (= s (apply str (reverse s))))

(println (isPalindrome "tacocat"))
(println (isPalindrome "nottacocat"))
