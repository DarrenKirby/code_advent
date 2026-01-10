;; AoC 2021 day 3

(define thunk
    (lambda ()
        (read-lines)))

(define input
    (with-input-from-file "input/day3.txt" thunk))

(define c_input (apply zip (map string->list input)))

(define (find p l)
    (if (p (count-equal #\1 l) (count-equal #\0 l)) "1" "0"))

(define gamma
    (apply string-append
        (map (lambda (l) (find > l)) c_input)))

(define epsilon
    (apply string-append
        (map (lambda (l) (find < l)) c_input)))

;;; Part 1
(println (* (string->number gamma 2)
            (string->number epsilon 2)))


(define (count-bits idx lst)
  (foldl
    (lambda (acc str)
      (if (char=? (string-ref str idx) #\1)
          (cons (+ 1 (car acc)) (cdr acc)) ; (ones . zeros)
          (cons (car acc) (+ 1 (cdr acc)))))
    (cons 0 0)
    lst))

(define (o2-bit idx lst)
  (let* ((counts (count-bits idx lst))
         (ones (car counts))
         (zeros (cdr counts)))
    (if (>= ones zeros) #\1 #\0)))

(define (co2-bit idx lst)
  (let* ((counts (count-bits idx lst))
         (ones (car counts))
         (zeros (cdr counts)))
    (if (<= zeros ones) #\0 #\1)))

(define (get-rating bit-position lst elem)
  (let* ((this-bit (elem bit-position lst))
         (filtered-list
           (filter (lambda (str)
                     (char=? (string-ref str bit-position) this-bit))
                   lst)))
    (if (= (length filtered-list) 1)
        (string->number (car filtered-list) 2)
        (get-rating (+ bit-position 1) filtered-list elem))))

(define o2 (get-rating 0 input o2-bit))
(define co2 (get-rating 0 input co2-bit))

;;; Part 2
(println (* o2 co2))
