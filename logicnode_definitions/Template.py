import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

# class <NodeName>(Node, ArmLogicTreeNode):
#    '''<Short Desciption (optional)>'''
#    bl_idname = 'LN<NodeName>'
#    bl_label = '<Name of the Node inside Blender>'
#    bl_icon = 'QUESTION'

#    def init(self, context):
#        self.inputs.new('<SocketType>', '<SocketName>')
#        self.outputs.new('<SocketType>', '<SocketName>')

# add_node(<NodeName>, category='<Category of the node>')
