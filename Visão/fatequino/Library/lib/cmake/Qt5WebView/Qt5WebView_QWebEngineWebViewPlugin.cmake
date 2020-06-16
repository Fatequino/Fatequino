
add_library(Qt5::QWebEngineWebViewPlugin MODULE IMPORTED)

_populate_WebView_plugin_properties(QWebEngineWebViewPlugin RELEASE "webview/qtwebview_webengine.dll")

list(APPEND Qt5WebView_PLUGINS Qt5::QWebEngineWebViewPlugin)
