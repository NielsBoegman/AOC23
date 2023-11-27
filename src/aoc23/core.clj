(ns aoc23.core)

(defn foo
  "I don't do a whole lot."
  [x]
  (println x "Hello, World!")
  (println "Second hello!"))

(defn factorial [n]
  (if (= n 0)
    1
    (* n (factorial (dec n)))))

(defn printfive [_]
  (println "5"))