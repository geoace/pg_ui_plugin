# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PgUserInterface
                                 A QGIS plugin
 This plugin converts QGIS projects to a web application. 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-07-05
        copyright            : (C) 2023 by GEOACE
        email                : aaron@geoace.net
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
    """Load PgUserInterface class from file PgUserInterface.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .pg_ui import PgUserInterface
    return PgUserInterface(iface)