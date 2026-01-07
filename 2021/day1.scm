;;; Solution written in Cozenage Scheme
;;; https://github.com/DarrenKirby/cozenage

; For cdddr
(import (base cxr))

(define (identity x) x)

(define (count-increases lst)
    (length (filter identity
        (map < lst (cdr lst)))))

(define thunk
    (lambda ()
        (map string->number (read-lines))))

(define input
    (with-input-from-file "input/day1.txt" thunk))

;;; Part 1
(println (count-increases input))

;;; Part 2
(println (length
    (filter identity
        (map < input (cdddr input)))))
