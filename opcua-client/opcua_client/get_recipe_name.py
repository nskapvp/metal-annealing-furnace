def get_recipe_name(client, node_path):
    # Получаем объект "g2"
    g2_obj = client.get_node(node_path)

    # Получаем список всех дочерних элементов объекта "g2"
    children = g2_obj.get_children()

    # Проходимся по всем дочерним элементам объекта "g2" и ищем "recipe"
    for child in children:
        child_name = child.get_browse_name().Name
        if child_name == "recipe":
            return child.get_value()