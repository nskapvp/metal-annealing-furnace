def get_recipe_object(select_recipe):
    recipe_info = []
    for recipe in select_recipe:
        recipe_data = {
            "id": recipe.id,
            "name": recipe.name_recipe,
            "stages": []
        }
        stages = [
            recipe.stage_1,
            recipe.stage_2,
            recipe.stage_3,
            recipe.stage_4,
            recipe.stage_5,
        ]
        for i, stage in enumerate(stages, start=1):
            stage_info = {
                "stage": i,
                "time": stage.time_ustavka,
                "temp": stage.temperature_ustavka,
                "gas": stage.gas,
                "pressure": stage.pressure
            }
            recipe_data["stages"].append(stage_info)
        recipe_info.append(recipe_data)
    return recipe_info
