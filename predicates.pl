# A predicate in Prolog is like a rule or a statement that describes a relationship or property. It's a way to express some fact or condition about something.

# Predicate to convert Centigrade temperature to Fahrenheit
centigrade_to_fahrenheit(Centigrade, Fahrenheit) :-
    Fahrenheit is (Centigrade * 9 / 5) + 32,
    write('Temperature in Fahrenheit: '), write(Fahrenheit), nl.

# Predicate to check if temperature is below freezing
below_freezing(Temperature) :-
    Temperature < 0,
    write('Temperature is below freezing.').

# Explanation:
# - The predicate `c_to_f/2` takes a temperature in Celsius (`Celsius`) as input and computes the equivalent temperature in Fahrenheit (`Fahrenheit`) using the formula `(Celsius * 9/5) + 32`.
# - The predicate `below_freezing/1` checks if the temperature (`Temperature`) is below freezing (i.e., less than 0 degrees Celsius).

# These predicates utilize Prolog's Horn clause notation, where the left-hand side represents the conclusion, and the right-hand side contains the premises. The `is` operator is used to perform arithmetic computations in Prolog.