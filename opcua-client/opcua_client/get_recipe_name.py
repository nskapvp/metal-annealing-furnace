def get_recipe_name(client, node_path):
    g2_obj = client.get_node(node_path)

    children = g2_obj.get_children()

    for child in children:
        child_name = child.get_browse_name().Name
        if child_name == "recipe":
            return child.get_value()