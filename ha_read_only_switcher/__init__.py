# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HAReadOnlySwitcher
                                 A QGIS plugin
 This Plugin is for swicthing read only status by one click for multiple layers
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-04-12
        copyright            : (C) 2024 by Lei Ding
        email                : lei.ding@headlandarchaeology.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load HAReadOnlySwitcher class from file HAReadOnlySwitcher.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ha_read_only_switcher import HAReadOnlySwitcher
    return HAReadOnlySwitcher(iface)