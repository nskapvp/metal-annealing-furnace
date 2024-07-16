from opcua import Client, ua


url = "opc.tcp://127.0.0.1:4840" # end point
node_path = "ns=4;s=|var|CODESYS Control Win V3 x64.Application.g2"

client = Client(url)