from opcua_client.opcua_client_driver import client, node_path
from opcua_client.get_recipe_name import get_recipe_name
from opcua_client.send_recipe import send_recipe
from time import sleep
from repository.get_recipe_object import get_recipe_object
from repository.select_recipe import select_recipe

if __name__ == "__main__":
    while True:
        try:
            client.connect()
            recipe_name = get_recipe_name(client, node_path)
            if recipe_name != 0 and recipe_name!= None:
                recipe = select_recipe(recipe_name)           
                obj = get_recipe_object(recipe)
                send_recipe(obj)
        finally:
            client.disconnect()
        sleep(1)