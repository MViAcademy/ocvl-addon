from logging import getLogger
from bpy.props import BoolProperty, StringProperty

from ...utils import cv_register_class, cv_unregister_class, OCVLPreviewNode, updateNode

logger = getLogger(__name__)


class OCVLSettingsNode(OCVLPreviewNode):
    origin = StringProperty("")
    settings = BoolProperty(default=False)

    def sv_init(self, context):
        self.width = 180
        self.outputs.new("StringsSocket", "settings")

    def wrapped_process(self):
        pass

    def draw_buttons(self, context, layout):
        col = layout.column(align=True)
        col_split = col.split(0.5, align=True)
        col_split.operator('node.change_theme_light', text='Light', icon="OUTLINER_OB_LAMP")
        col_split.operator('node.change_theme_dark', text='Dark', icon="OUTLINER_DATA_LAMP")


def register():
    cv_register_class(OCVLSettingsNode)


def unregister():
    cv_unregister_class(OCVLSettingsNode)