(define (vir-fib n)
    (cond
        ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (vir-fib (- n 2)) (vir-fib (- n 1)))
        )
    )
)

(expect (vir-fib 10) 55)
(expect (vir-fib 1) 1)


(define with-cons
    (cons
        (cons 'a (cons 'b nil))
        (cons 'c (cons 'd (cons (cons 'e nil) nil)))
    )
)
(draw with-list)

(define with-quote
    '(
        (a b)
        c d (e)
    )
)

(define with-list
    (list
        (list 'a 'b)
        'c 'd (list 'e)
    )
)

(define (list-concat a b)
    (if (null? a)
        b
        (cons (car a) (list-concat (cdr a) b))
))

(expect (list-concat '(1 2 3) '(2 3 4)) (1 2 3 2 3 4))
(expect (list-concat '(3) '(2 1 0)) (3 2 1 0))



(define (map-fn fn lst)
    (if (null? lst)
        nil
        (cons (fn (car lst)) (map-fn fn (cdr lst)))
))

(map-fn (lambda (x) (* x x)) '(1 2 3))
; expect (1 4 9)


(define (remove item lst)
  (cond
        ((null? lst) '())
        ((equal? item (car lst)) (remove item (cdr lst)))
        (else (cons (car lst) (remove item (cdr lst))))
  )
)

' or (filter (lambda (x) (not (= x item))) lst))

(expect (remove 3 nil) ())
(expect (remove 2 '(1 3 2)) (1 3))
(expect (remove 1 '(1 3 2)) (3 2))
(expect (remove 42 '(1 3 2)) (1 3 2))
(expect (remove 3 '(1 3 3 7)) (1 7))