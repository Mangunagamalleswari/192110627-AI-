planet(mercury, 57.91, no).
planet(venus, 108.2, no).
planet(earth, 149.6, yes).
planet(mars, 227.9, yes).
planet(jupiter, 778.3, yes).
planet(saturn, 1427, yes).
planet(uranus, 2871, yes).
planet(neptune, 4497, yes).

has_moons(Planet) :- planet(Planet, _, yes).
within_distance(Planet, Distance) :- planet(Planet, D, _), D =< Distance.
