---
title: Creating heatmaps with matplotlib in python
categories:
 - notes
tags: python, visualization
author: tenpages
---

Creating (categorical) heatmaps with `matplotlib` consists of 3 steps: painting cells with colors, annotating, and adding the sidebar.

# Packages
The package in need is mainly `matplotlib`.
```python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
```
Using `numpy` or `pandas` would also make things easier. 

# Painting cells
Assuming we already have an numpy array named `fusMat` (i.e. a fusion matrix). The name of columns (as well as rows) in a list is `classes`. To paint the cells, do this
```python
fig, ax = plt.subplots()
im = ax.imshow(fusMat)
```
and we will get something like:


# Annotating
