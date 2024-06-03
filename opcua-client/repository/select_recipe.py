from controller.db_driver import session
from models.recipe_model import Recipe, Stage

def select_recipe(recipe_id):
    return session.query(Recipe).filter(Recipe.id == recipe_id).all()