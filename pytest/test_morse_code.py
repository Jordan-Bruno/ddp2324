#If you do not have 

import pytest
import morse_code


def test_morse_translator():
    assert (
        morse_code.morse_translator("HELLO WORLD")
        == ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    )
    assert morse_code.morse_translator("Python") == ".--. -.-- - .... --- -."
    assert (
        morse_code.morse_translator("Morse Code") == "-- --- .-. ... . / -.-. --- -.. ."
    )
