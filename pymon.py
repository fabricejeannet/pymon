import random

def start_sequence():
    sequence = []
    for value in range(4):
        sequence.append(random.randint(0,3))
    return sequence

def is_correct(sequence, index, input):
    return sequence[index] == input

RED = 0
GREEN = 1
BLUE = 2
YELLOW = 3
#-------------------------------------------------------------

def test_a_sequence_sarts_with_four_elements():
    sequence = start_sequence()
    assert len(sequence) == 4

def test_testing_a_good_input_returns_true():
    sequence = [RED,GREEN, BLUE]
    assert is_correct(sequence, 1, GREEN) == True

def test_testing_a_wrong_input_returns_false():
    sequence = [RED,GREEN, BLUE]
    assert is_correct(sequence, 1, BLUE) == False

    


