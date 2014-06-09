(ns clojure-euler.core
  (:gen-class))

(defn doit [sum, value]
  (if (or
        (= (mod value 3) 0)
        (= (mod value 5) 0))
    (+ sum value)
    sum))

;; Find the sum of all the multiples of 3 or 5 below 1000
(defn p1 []
  (reduce doit (range 1000)))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  ;; work around dangerous default behaviour in Clojure
  (alter-var-root #'*read-eval* (constantly false))
  (p1))

