
## HolyGFXBot Turtle API Examples

### Drawing (Simplified Turtle API)
  - See [available Turtle API drawing functions](https://tinkeros.github.io/HolyGFX/turtle.html)

## Examples:

### 240x240 Blue square with yellow border
<center><img src="https://tinkeros.github.io/HolyGFX/ybsq.png"></center>
!hg 240 240

```
PenSetWidth(4);
TSetPos(TR_WIDTH/4, 3*TR_HEIGHT/4);
TFd(TR_WIDTH/2);
TRt(90);
TFd(TR_WIDTH/2);
TRt(90);
TFd(TR_WIDTH/2);
TRt(90);
TFd(TR_WIDTH/2);
TRt(90);

// Center Turtle inside square to fill it.
THome;
TSetFillColor(BLUE);
TFill;
```
