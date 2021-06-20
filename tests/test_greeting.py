import pytest
from lib.greeting import Greeting

class Test_Greeting:
    
    def test_greet(self):
        greet = Greeting()
        full_greet=greet.greeting('Manoj')
        assert full_greet == 'Hello Manoj'
    
    def test_invalid_string_for_name_in_greet_(self):
        with pytest.raises(ValueError) as exp:
            greet=Greeting()
            greet.greeting(2)
        assert str(exp.value)== 'Invalid name'