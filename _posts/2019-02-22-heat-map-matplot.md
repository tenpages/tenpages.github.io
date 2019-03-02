---
title: Creating heatmaps with matplotlib in python
categories:
 - notes
tags: python, visualization
author: tenpages
---

Creating (categorical) heatmaps with `matplotlib` consists of 2 steps: painting cells with colors and annotating it.

<!-- more -->
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
![](/assets/images/20190222/Figure_1.png)
To change the coloring scheme, use parameter `cmap` in `.imshow()` method:
```python
im = ax.imshow(fusMat, cmap=plt.cm.Reds)
```

# Annotating
Clearly the axises in the figure above is not what we want. So we need to change these "tick labels":
```python
ax.set_xticks(np.arange(len(classes)))
ax.set_yticks(np.arange(len(classes)))
ax.set_xticklabels(classes)
ax.set_yticklabels(classes)
```
We would also like to specify what x- and y-axis stands for:
```python
ax.set_xlabel("pred")
ax.set_ylabel("gold")
```
A color bar would be nice:
```python
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel(ylabel="# of pred", rotation=-90, va="bottom")
```
We want the numbers of each cell be displayed, in white on dark cells, and black on light cells:
```python
for i in range(0,len(classes)):
    for j in range(0,len(classes)):
        if fusMat[j][i] > (fusMat.max()+fusMat.min())/2:
            text = ax.text(i,j, fusMat[j][i],
                           ha="center", va="center", color="w")
        else:
            text = ax.text(i,j, fusMat[j][i],
                           ha="center", va="center", color="k")
```
To add title, use
```python
ax.set_title("Fusion matrix")
```
Finally, we get somthing like this:
![](/assets/images/20190222/Figure_2.png)

# Saving to file
To save the fig to a file:
```python
fig.tight_layout()
plt.savefig(filename)
```

# References
- [Creating annotated heatmaps](https://matplotlib.org/gallery/images_contours_and_fields/image_annotated_heatmap.html)
- [Matplotlib coloring scheme](https://matplotlib.org/examples/color/colormaps_reference.html)