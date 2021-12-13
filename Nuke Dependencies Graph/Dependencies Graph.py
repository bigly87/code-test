
import nuke
import os

'''
    V01
    this function using default bulit in nuke.dependecies() module which 
    in result only returning connected input of selected node and it's mask. 
    It returns Expressioned nodes but not Cloned
'''

def get_dependencies_v01(selected_node):
    dependencies_nodes= selected_node.dependencies()
    return (dependencies_nodes)

result = get_dependencies_v01(nuke.selectedNode())
print(result)



'''
    V02
    is an extended version of v01 which goes up in stream pipe
    and return every node connected in that pipe, untill it
    reaches the first node.
    It returns cloned nodes, expressions
'''

def get_dependencies_v02(node):
    dependencies = []
    nodes_to_process = node.dependencies()
    while nodes_to_process:
        node = nodes_to_process.pop(0)
        if node not in dependencies:
            dependencies.append(node)
            nodes_to_process.extend(node.dependencies())
    return dependencies

all_dependencies = get_dependencies_v02(nuke.selectedNode())
print(all_dependencies)



