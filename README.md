# sketch_measure
Sketch measure parser

This library is built to parse the exported index.html file, generated by [Sketch Measure](https://github.com/utom/sketch-measure) plugin. It helps the programmer to quickly get the information from its embedded json data. So, the automation from the index.html file is made possible with this library for further processing.

# Usage
```
from sketch_measure import SketchMeasure

sm = SketchMeasure.load("index.html")
# then all elements are available as python object

for layer in sm.artboards[0].layers:
    layer.pretty_print()
```

# License
Apache 2.0 license
