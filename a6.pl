%rules
parent(lokesh,manish).
parent(lokesh,sam).
male(lokesh).
female(sam).

%facts
father(X,Y):-parent(X,Y),male(X).
sibling(X,Y):-parent(Z,X),parent(Z,Y),X\=Y.
