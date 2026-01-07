(define thunk
    (lambda ()
      (map string-split (read-lines))))

(define input
    (with-input-from-file "input/day2.txt" thunk))

(define (apply-move pos move)
  (let ((x   (car pos))
        (z   (cadr pos))
        (cmd (string->symbol (car move)))
        (n   (string->number (cadr move))))
    (case cmd
      ((forward) (list (+ x n) z))
      ((up)      (list x (- z n)))
      ((down)    (list x (+ z n)))
      (else      pos))))

(define final-pos
  (foldl apply-move '(0 0) input))

;;; Part 1
(println (* (car final-pos) (cadr final-pos)))
