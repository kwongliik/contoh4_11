from contoh4_11 import *
from tud_test_base import *
import pytest

@pytest.mark.parametrize("a", [(4), (5), (6)])
def test_bilangan_batu(a):
    x = bilangan_batu(a)
    assert 0 <= x <= a 

def test_main():
    set_keyboard_input(['T'])
    main()
    output = get_display_output()
    
    assert output != None