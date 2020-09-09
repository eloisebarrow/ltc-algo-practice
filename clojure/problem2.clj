;; Write a function called oddsEvens that given a string, prints its
;; even-indexed and odd-indexed characters as space-separated strings on a
;; single line.

;; Input: Hacker Output: Hce akr
;; 09/09
(require '[clojure.string :as str])

(defn oddEvens [s]
  (let [indexedStr (map-indexed vector s)
        evenChars (filter (fn [x] (odd? (get x 0))) indexedStr)
        oddChars (filter (fn [x] (even? (get x 0))) indexedStr)
        evenStr (str/join (map #(get % 1) evenChars))
        oddStr (str/join (map #(get % 1) oddChars))]
    (print oddStr " " evenStr)))

(oddEvens "Hacker")
