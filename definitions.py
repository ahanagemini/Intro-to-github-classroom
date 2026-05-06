def get_definition_category(approach_name):
    """
    Match the approach to its category based on Figure 1.1 in Chapter 1.
    Categories: "Think Humanly", "Think Rationally", "Act Humanly", "Act Rationally"
    """
    # Example: "The Turing Test" -> "Act Humanly"
    
    mapping = {
        "Turing Test": "",
        "Laws of Thought": "",
        "Cognitive Modeling": "",
        "Rational Agent": ""
    }
    
    return mapping.get(approach_name, "Unknown")
