(define (domain package-world)
    
    (:requirements :adl
    )
    
    (:predicates
        (on-top ?x ?y)
		(on-floor ?x)
		(clear ?x)
		(in-hands ?x)
    )
    
    (:action grab-from-package
		:parameters (?x ?z)
		:precondition
		(and
		    (not (exists (?y)(in-hands ?y)))
			(clear ?x)
			(on-top ?x ?z)
		)
		:effect
		(and
		    (not (on-top ?x ?z))
		    (in-hands ?x)
			(clear ?z)
		)
	)
	
	(:action grab-from-floor
		:parameters (?x)
		:precondition
		(and
		    (not (exists (?y)(in-hands ?y)))
			(clear ?x)
			(on-floor ?x)
		)
		:effect
		(and
			(in-hands ?x)
			(not (on-floor ?x))
		)
	)
	
	(:action put-on-package
	    :parameters (?z ?x)
	    :precondition
	    (and
	        (clear ?z)
	        (in-hands ?x)
	        (not (on-top ?x ?z))

	    )
	    :effect
	    (and
	        (not (in-hands ?x))
	        (not (clear ?z))
	        (on-top ?x ?z)
	    )
	)
	
	(:action put-on-floor
	    :parameters (?x)
	    :precondition
	    (and
	        (in-hands ?x)
	    )
	    :effect
	    (and
	        (on-floor ?x)
	        (not (in-hands ?x))
	    )
	)
)