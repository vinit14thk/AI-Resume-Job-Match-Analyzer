import re

SKILL_SYNONYMS = {
    "python": ["python"],
    "sql": ["sql", "structured query language"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "scikit-learn": ["scikit-learn", "sklearn"],
    "machine learning": ["machine learning"],
    "data analysis": [
        "data analysis",
        "analyzing data",
        "analysing data"
    ],
    "statistics": ["statistics", "statistical analysis"],
    "data visualization": [
        "data visualization",
        "data visualisation",
        "data visualization tools",
        "data visualisation tools"
    ],
    "communication": ["communication", "communicating"],
    "problem-solving": ["problem-solving", "problem solving"],
    "analytical thinking": ["analytical thinking", "analytical skills"],
    "git": ["git"],
    "github": ["github"],
    "business analytics": ["business analytics"]
}


def skill_is_present(skill, text):
    variants = SKILL_SYNONYMS.get(
        skill.lower(), [skill.lower()]
    )

    for variant in variants:
        pattern = r"(?<!\w)" + re.escape(variant) + r"(?!\w)"

        if re.search(pattern, text.lower()):
            return True

    return False
