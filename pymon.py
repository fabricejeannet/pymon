
def start():
    sequence.clear()
    append_new_entry_to_sequence()

def append_new_entry_to_sequence():
    sequence.append(0)    

def is_correct(index, value):
    print (sequence)
    return sequence[index] == value

sequence = []
RED = 0
GREEN = 1
BLUE = 2
YELLOW = 3
#-------------------------------------------------------------

def test_first_sequence_contains_one_element():
    start()
    assert len(sequence) == 1
    
def test_sequence_grows_one_by_one():
    start()
    append_new_entry_to_sequence();
    assert len(sequence) == 2

def test_returns_true_when_value_matches_list_value_for_the_given_index():
    start()
    sequence = [RED, GREEN, BLUE, YELLOW]
    assert is_correct(1, GREEN) == True
    


