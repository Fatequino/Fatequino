
add_library(Qt5::QWebGLIntegrationPlugin MODULE IMPORTED)

_populate_Gui_plugin_properties(QWebGLIntegrationPlugin RELEASE "platforms/qwebgl.dll")

list(APPEND Qt5Gui_PLUGINS Qt5::QWebGLIntegrationPlugin)
