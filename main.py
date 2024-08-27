"""
Kochbuch
"""

import json

recipe = {
    "title": "Spaghetti Bolognese",
    "ingredients": {
        "Spaghetti": 400,
        "Tomato Sauce": 300,
        "Minced Meat": 500
    },
    "servings": 4
}

servings = 2


def adjust_recipe(recipes, serving):
    # Berechne den Anpassungsfaktor
    factor = serving / recipes["servings"]

    # Passe die Zutatenmengen an
    adjusted_ingredients = {ingredient: amount * factor for ingredient, amount in recipes["ingredients"].items()}

    # Erstelle das angepasste Rezept
    adjusted_recipe = {
        "title": recipes["title"],
        "ingredients": adjusted_ingredients,
        "servings": serving
    }

    return adjusted_recipe


def load_recipe(json_recipe):
    return json.loads(json_recipe)


if __name__ == "__main__":
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')
    # Dein Code kommt hier hin
    adjust_recipe(recipe_json, servings)
    load_recipe(recipe_json)
