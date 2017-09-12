import pytest
from phonebook import Phonebook

def test_and_add_lookup_entry():
    phonebook = Phonebook()
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob")

def test_phonebook_gives_access_to_names_and_numbers():
    phonebook = Phonebook()
    phonebook.add("Alice", "12345")
    assert "Alice" in phonebook.names()
    assert "12345" in phonebook.numbers()

def test_missing_entry_raises_KeyError():
    phonebook = Phonebook()
    with pytest.raises(KeyError):
        phonebook.lookup("missing")
