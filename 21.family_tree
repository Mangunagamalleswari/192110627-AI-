parent(john, jim).
parent(john, ann).
parent(ann, peter).
male(jim).
female(ann).
male(john).
male(peter).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
