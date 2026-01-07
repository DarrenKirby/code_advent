;; AoC 2021 day 3

(define thunk
    (lambda ()
        (read-lines)))

(define input
    (with-input-from-file "input/day3.txt" thunk))

(define c_input (apply zip (map string->list input)))

(define (find p l)
    (if (p (count #\1 l) (count #\0 l)) "1" "0"))

(define gamma
    (apply string-append
        (map (lambda (l) (find > l)) c_input)))

(define epsilon
    (apply string-append
        (map (lambda (l) (find < l)) c_input)))

;;; Part 1
(println (* (string->number gamma 2)
            (string->number epsilon 2)))
