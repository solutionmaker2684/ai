# What is Prolog:
# 1. Prolog stands for "Programming in Logic."
# 2. It's a declarative programming language, meaning you describe the problem to be solved rather than specifying the steps to solve it.
# 3. Prolog programs consist of facts and rules that define relationships between objects and conditions.

# How to Use Prolog:
# 1. You write Prolog programs using facts and rules to define relationships and logic.
# 2. You can then query the Prolog interpreter to find solutions to logical queries based on the defined facts and rules.

# Advantages of Prolog:
# 1. Declarative Nature: You specify what you want to achieve rather than how to achieve it, which can make programming more intuitive for certain types of problems.
# 2. Built-in Backtracking: Prolog automatically searches for multiple solutions to a problem and backtracks if needed, which can be very useful for tasks like searching and optimization.
# 3. Pattern Matching: Prolog's pattern matching capabilities allow for powerful and concise representations of complex relationships and conditions.

# Disadvantages of Prolog:
# 1. Efficiency: Prolog may not always be the most efficient choice for certain types of problems, especially those that require heavy computation or data manipulation.
# 2. Learning Curve: Its logic-based paradigm can be quite different from traditional imperative or object-oriented programming, requiring a shift in thinking for programmers new to Prolog.
# 3. Limited Use Cases: While Prolog is excellent for certain types of problems, it may not be suitable for all programming tasks, particularly those that involve procedural or object-oriented programming paradigms.

# Facts:
likes(john, pizza).
likes(john, sushi).
likes(mary, sushi).
singer(sonu).
odd_number(5).

# Explanation:
# - `likes(john, pizza)` and `likes(john, sushi)` indicate that John likes pizza and sushi, respectively.
# - `likes(mary, sushi)` states that Mary likes sushi.
# - `singer(sonu)` indicates that Sonu is a singer.
# - `odd_number(5)` signifies that 5 is an odd number.

# Running queries:
# ?- likes(john, pizza).
# Yes.
# ?- likes(john, burger).
# No.
# ?- singer(sonu).
# Yes.
# ?- odd_number(7).
# No.
