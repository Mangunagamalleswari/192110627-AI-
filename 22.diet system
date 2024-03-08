has_disease(john, diabetes).
has_disease(susan, hypertension).
has_disease(mary, obesity).

suggest_diet(Person, Diet) :-
    has_disease(Person, diabetes), Diet = 'Low-carb diet'.
suggest_diet(Person, Diet) :-
    has_disease(Person, hypertension), Diet = 'Low-sodium diet'.
suggest_diet(Person, Diet) :-
    has_disease(Person, obesity), Diet = 'Balanced diet with portion control'.
