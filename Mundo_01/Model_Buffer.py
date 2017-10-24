# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Model_Buffer.py
# Created on: 2017-09-29 10:26:07.00000
# Usage: Model_Buffer entrada, saida, distancia
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
# We only need to import this module
# The top argument for walk. The
# Python27/Lib/site-packages folder in my case
# The arg argument for walk, and subsequently ext for step
import arcpy
from Tkinter import Tk
from tkFileDialog import askopenfilename, asksaveasfilename

#Shapefile de entrada
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# show an "Open" dialog box and return the path to the selected file
entrada = askopenfilename(defaultextension=".shp", filetypes=(("All Files", "*.*"),("Shape file", "*.shp")))
print(entrada)

#Shapefile resultado
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# show an "Open" dialog box and return the path to the selected file
saida = asksaveasfilename(defaultextension=".shp", filetypes=(("All Files", "*.*"),("Shape file", "*.shp")))
print(saida)

#Campo de distancia do buffer
Distance__value_or_field_ = 0.0025

# Process: Buffer
arcpy.Buffer_analysis(entrada, saida, Distance__value_or_field_, "FULL", "ROUND", "NONE", "")

