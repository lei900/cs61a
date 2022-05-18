(define (cddr s) 
    (cdr (cdr s)))

(define (cadr s) 
    (car (cdr s)))

(define (caddr s) 
    (cadr (cdr s)))

(define (ascending? lst) 
    (cond
        ((null? lst) false)
        ((null? (cdr lst)) true)
        ((<= (car lst) (cadr lst) ) (ascending? (cdr lst)))
        (else false)
        ))

(define (interleave lst1 lst2) 
    (cond
        ((and (null? lst1)(null? lst2)) nil)
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else list (car lst1) (car lst2) (interleave (cdr lst1) (cdr lst2)))
        )
)

(define (my-filter func lst) 
    (cond
        ((null? lst)
            '())
         ((func (car lst))
        (cons (car lst) (my-filter func (cdr lst))))
        (else 
              (my-filter func(cdr lst)))))

(define (no-repeats lst) 
  (if (null? lst)
      lst
      (cons (car lst)
            (no-repeats
             (my-filter (lambda (x) (not (= (car lst) x)))
                        (cdr lst))))))
