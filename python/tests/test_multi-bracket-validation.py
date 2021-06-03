from code_challenges.multi_bracket_validation.multi_bracket_validation import (multi_bracket_validation)

def test_one():
   string = "{}{Code}[Fellows](())"
   actual = multi_bracket_validation(string)
   expected = True
   assert actual == expected

def test_two():
   string = "{{}}}}"
   actual = multi_bracket_validation(string)
   expected = False
   assert actual == expected

def test_three():
   string = "(){}[]"
   actual = multi_bracket_validation(string)
   expected = True
   assert actual == expected

def test_four():
   string = "{"
   actual = multi_bracket_validation(string)
   expected = False
   assert actual == expected
