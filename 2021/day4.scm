;;; AoC 2021 day 4

(define thunk
  (lambda ()
    (read-lines)))

(define input
  (with-input-from-file "input/day4.txt" thunk))

(define draws (map string->number (string-split (car input) ",")))

(set! input (filter (lambda (s) (not (string=? s ""))) (cdr input)))

(define (take lis k)
  (let recur ((lis lis) (k k))
    (if (zero? k) '()
                  (cons (car lis)
                    (recur (cdr lis) (- k 1))))))

(define (drop lis k)
  (let iter ((lis lis) (k k))
    (if (zero? k) lis (iter (cdr lis) (- k 1)))))

(define (transpose matrix)
  (if (null? matrix)
      '()
      (apply map list matrix)))

(define (any pred lst)
  (if (null? lst)
      #f
      (if (pred (car lst))
          #t
          (any pred (cdr lst)))))

(define (every pred lst)
  (if (null? lst)
      #t
      (if (pred (car lst))
          (every pred (cdr lst))
          #f)))

(define (chunks-of-5 lst)
  (if (null? lst)
      '()
      (cons (take lst 5)
            (chunks-of-5 (drop lst 5)))))

(define (parse-card lines)
  (map
    (lambda (line)
      (map string->number
           (string-split line)))
    lines))

(define cards (map parse-card (chunks-of-5 input)))

(define (mark-card n card)
  (map (lambda (row)
         (map (lambda (x)
                (if (equal? x n) #f x))
              row))
       card))

(define (mark-all-cards n cards)
  (map (lambda (card)
         (mark-card n card))
       cards))

(define (winning-row? row)
  (every false? row))

(define (winning-card? card)
  (if (any winning-row? card)
      #t
      (any winning-row? (transpose card))))

(define (play-until-win draws cards)
  (if (null? draws)
      (raise "no winning card")
      (let* ((n (car draws))
             (new-cards (mark-all-cards n cards)))
        (let ((winners (filter winning-card? new-cards)))
          (if (null? winners)
              (play-until-win (cdr draws) new-cards)
              (cons n winners))))))

(define winner (play-until-win draws cards))

;;; Part 1 lol
(println
  (* (apply +
       (map (lambda (l)
              (foldl (lambda (acc v)
                       (+ (if (boolean? v) 0 v) acc)) 0 l))
         (cadr winner))) (car winner)))
