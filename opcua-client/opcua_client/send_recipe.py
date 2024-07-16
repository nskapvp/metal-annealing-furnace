from opcua_client.opcua_client_driver import client, node_path, ua

def send_recipe(recipe_info):
    for i in range(1,6):
        node_ustavka_time = client.get_node(node_path + f".ustavka{i}_time")
        node_ustavka_temperature = client.get_node(node_path + f".ustavka{i}_temperature")
        node_ustavka_gas = client.get_node(node_path + f".ustavka{i}_gas")
        node_ustavka_pressure = client.get_node(node_path + f".ustavka{i}_pressure")     
        
        stage_time = recipe_info[0]["stages"][i - 1]["time"]
        variant_time = ua.Variant(stage_time, ua.VariantType.Float)
        node_ustavka_time.set_value(variant_time)

        stage_temperature = recipe_info[0]["stages"][i - 1]["temp"]
        variant_temperature = ua.Variant(stage_temperature, ua.VariantType.Float)
        node_ustavka_temperature.set_value(variant_temperature)

        stage_gas = recipe_info[0]["stages"][i - 1]["gas"]
        variant_gas = ua.Variant(stage_gas, ua.VariantType.Float)
        node_ustavka_gas.set_value(variant_gas)

        stage_pressure = recipe_info[0]["stages"][i - 1]["pressure"]
        variant_pressure = ua.Variant(stage_pressure, ua.VariantType.Float)
        node_ustavka_pressure.set_value(variant_pressure)