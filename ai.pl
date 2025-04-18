likes(aman, X) :- drink(X).

drink(water).
drink(juice).
drink(X) :- drinks(Y, X), \+ dead(Y).

drinks(lokesh, tea).
drinks(manish, coffee).

dead(manish).
