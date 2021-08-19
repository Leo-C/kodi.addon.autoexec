import xbmc
import xbmcaddon


startup_addon = xbmcaddon.Addon().getSetting("startup_addon").strip()
if startup_addon != "":
    xbmc.log("[service.autoexec.addon] starting Addon:" + startup_addon, xbmc.LOGINFO)
    xbmc.executebuiltin('RunAddon(%s)' % startup_addon)
