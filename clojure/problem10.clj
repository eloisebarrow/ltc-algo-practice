;; Write a function called phoneBook that given two parameters, the first being an
;; array of hashes containing n number of names and phone numbers and the second
;; being an array of friends names will then will assemble a phone book that maps
;; the 'friends' array of names to their respective phone numbers if they are
;; found in the first array. Each found entry will print the associated entry from
;; your phone book on a new line in the form name=phoneNumber; if an entry is not
;; found, print Not found instead.
;;
;; Input 1: [{sam:99912222},{tom:11122222},{harry:12299933}]
;; Input 2: ['sam','ed','harry']
;;
;; Output:
;; sam=99912222
;; NOT FOUND
;; harry:12299933

;; 09/21/2020

(defn phoneBook [entries names]
  (let [phonebook (apply merge entries)]
    (doseq [n names]
      (if (contains? phonebook (keyword n))
        (println (str n "=" (get phonebook (keyword n))))
        (println "NOT FOUND")))))

(phoneBook [{:sam 99912222} {:tom 11122222} {:harry 12299933}]
           ["sam", "ed", "harry"])
