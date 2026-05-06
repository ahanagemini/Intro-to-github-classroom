from definitions import get_definition_category

def test_categories():
    assert get_definition_category("Turing Test") == "Act Humanly"
    assert get_definition_category("Laws of Thought") == "Think Rationally"
    assert get_definition_category("Cognitive Modeling") == "Think Humanly"
    assert get_definition_category("Rational Agent") == "Act Rationally"
    print("✅ Chapter 1 definitions correctly mapped!")

if __name__ == "__main__":
    test_categories()
