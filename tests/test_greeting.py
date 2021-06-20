import pytest
from lib.greeting import greeting

class Test_Greeting:
    
    def test_greet(self):
        greet = greeting('Manoj')
        assert greet == 'Hello manoj'