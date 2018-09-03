import bpy
from . step5_ui import \
    VIEW3D_PT_jet_step5, \
    VIEW3D_OT_jet_apply_modifiers, \
    VIEW3D_OT_jet_remove_parent, \
    VIEW3D_OT_jet_assign_decimate, \
    VIEW3D_OT_jet_apply_decimate, \
    VIEW3D_OT_jet_append_opt_high, \
    VIEW3D_OT_jet_assign_subsurf, \
    VIEW3D_OT_jet_apply_transf_constraints

def register():
    #bpy.utils.register_class(VIEW3D_OT_jet_add_sufix)
    bpy.utils.register_class(VIEW3D_OT_jet_apply_transf_constraints)
    bpy.utils.register_class(VIEW3D_OT_jet_assign_subsurf)
    bpy.utils.register_class(VIEW3D_OT_jet_append_opt_high)
    bpy.utils.register_class(VIEW3D_OT_jet_assign_decimate)
    bpy.utils.register_class(VIEW3D_OT_jet_apply_decimate)
    bpy.utils.register_class(VIEW3D_OT_jet_apply_modifiers)
    bpy.utils.register_class(VIEW3D_OT_jet_remove_parent)
    bpy.utils.register_class(VIEW3D_PT_jet_step5)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_jet_step5)
    #bpy.utils.unregister_class(VIEW3D_OT_jet_add_sufix)
    bpy.utils.unregister_class(VIEW3D_OT_jet_apply_modifiers)
    bpy.utils.unregister_class(VIEW3D_OT_jet_remove_parent)
    bpy.utils.unregister_class(VIEW3D_OT_jet_assign_decimate)
    bpy.utils.unregister_class(VIEW3D_OT_jet_apply_decimate)
    bpy.utils.unregister_class(VIEW3D_OT_jet_append_opt_high)
    bpy.utils.unregister_class(VIEW3D_OT_jet_assign_subsurf)
    bpy.utils.unregister_class(VIEW3D_OT_jet_apply_transf_constraints)



