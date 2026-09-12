## Benjamin Naderi

Co-founder of **GeoBirds**. Entrepreneurship and hardware development, with a
background in manufacturing where I have worked on systems at both small and
large scale.

On the organising committee of
[PyData Amsterdam](https://amsterdam.pydata.org/).

Father of two.

### polars-crs

[**polars-crs**](https://github.com/benjamin-naderi-gh/polars-crs) detects which
coordinate reference system a column of unlabelled x/y numbers is in, by looking
at the values.

You get a CSV with two numeric columns and no metadata. Nobody records the
projection, and every existing tool makes you already know it. Guess wrong and
nothing warns you: assume lat/lon for Dutch RD New coordinates and Amsterdam to
Rotterdam comes out as 6,612 km instead of 57.7 km.

```python
import polars as pl
import polars_crs as plc

df.select(plc.detect("x", "y"))   # 'EPSG:28992'
```

A Polars expression plugin written in Rust. Bounds derived from PROJ areas of
use and validated against pyproj ground truth. Runs on 10 million rows in
0.020s.

```
pip install polars-crs
```

### Elsewhere

Homelabs and home automation, less actively than I used to be. Reading about
history and space exploration.
