import pytest
from L4_string_utils import StringUtils

def test_capitilize():
    string_util = StringUtils()
    assert string_util.capitilize("automation") == "Automation"
    
def test_capitilize_empty_string():
    string_util = StringUtils()
    assert string_util.capitilize("") == ""
    
def test_trim():
    string_util = StringUtils()
    assert string_util.trim("   automation") == "automation"
    assert string_util.trim("") == ""
    
def test_trim_no_whitespace():
    string_util = StringUtils()
    assert string_util.trim("automation") == "automation"

def test_to_list():
    string_util = StringUtils()
    assert string_util.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_util.to_list("1:2:3", ":") == ["1", "2", "3"]

def test_contains():
    string_util = StringUtils()
    assert string_util.contains("automation", "a") == True
    assert string_util.contains("automation", "D") == False
    
def test_contains_symbol_not_present():
    string_util = StringUtils()
    assert string_util.contains("automation", "x") == False

def test_delete_symbol():
    string_util = StringUtils()
    assert string_util.delete_symbol("automation", "t") == "auomaion"
    assert string_util.delete_symbol("automation", "mation") == "auto"
    
def test_delete_symbol_symbol_not_present():
    string_util = StringUtils()
    assert string_util.delete_symbol("automation", "x") == "automation"

def test_starts_with():
    string_util = StringUtils()
    assert string_util.starts_with("automation", "a") == True
    assert string_util.starts_with("automation", "m") == False
    
def test_starts_with_symbol_not_present():
    string_util = StringUtils()
    assert string_util.starts_with("automation", "x") == False

def test_end_with():
    string_util = StringUtils()
    assert string_util.end_with("automation", "n") == True
    assert string_util.end_with("automation", "o") == False
    
def test_end_with_symbol_not_present():
    string_util = StringUtils()
    assert string_util.end_with("automation", "x") == False

def test_is_empty():
    string_util = StringUtils()
    assert string_util.is_empty("") == True
    assert string_util.is_empty(" ") == True
    assert string_util.is_empty("SkyPro") == False
    

@pytest.mark.parametrize ('list, result', [ ([1, 2, 3, 4], "1, 2, 3, 4"), (["Sky", "Pro"], "Sky, Pro"), ([], "" )])   
def test_list_to_string(list, result):
    string_util = StringUtils()
    assert string_util.list_to_string(list) == result
    assert string_util.list_to_string(lst=["Sky", "Pro"], joiner="-") == "Sky-Pro"






