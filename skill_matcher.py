import re

SKILL_SYNONYMS = {
    "python": [
        "python",
        "python programming",
        "python scripting"
    ],
    "sql": [
        "sql",
        "structured query language",
        "sql queries"
    ],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "scikit-learn": [
        "scikit-learn",
        "scikit learn",
        "sklearn"
    ],
    "machine learning": [
        "machine learning",
        "ml algorithms"
    ],
    "data analysis": [
        "data analysis",
        "analyzing data",
        "analysing data"
    ],
    "statistics": [
        "statistics",
        "statistical analysis"
    ],
    "data visualization": [
        "data visualization",
        "data visualisation",
        "data visualization tools",
        "data visualisation tools"
    ],
    "communication": [
        "communication",
        "communicating",
        "communication skills"
    ],
    "problem-solving": [
        "problem-solving",
        "problem solving",
        "problem-solving skills"
    ],
    "analytical thinking": [
        "analytical thinking",
        "analytical skills"
    ],
    "git": ["git", "git version control"],
    "github": [
        "github",
        "github repository",
        "github repositories"
    ],
    "business analytics": ["business analytics"]
}


def skill_is_present(skill, text):
    normalized_skill = skill.casefold().strip()
    normalized_text = text.casefold()

    variants = SKILL_SYNONYMS.get(
        normalized_skill,
        [normalized_skill]
    )

    for variant in variants:
        pattern = r"(?<!\w)" + re.escape(variant) + r"(?!\w)"

        if re.search(pattern, normalized_text):
            return True

    return False

def find_skill_match(skill, text):
    normalized_skill = skill.casefold().strip()
    normalized_text = text.casefold()

    variants = sorted(
    SKILL_SYNONYMS.get(
        normalized_skill,
        [normalized_skill]
    ),
    key=len,
    reverse=True
)

    for variant in variants:
        pattern = r"(?<!\w)" + re.escape(variant) + r"(?!\w)"

        if re.search(pattern, normalized_text):
            return variant

    return None