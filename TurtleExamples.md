
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

### 216x64 Gradient showing extended color palette shades of green
<center><img src="https://tinkeros.github.io/HolyGFX/extgreen.png"></center>

!hg 216 64

```
/* Use GetColorNum to find the nearest TinkerOS 
 * extended palette color to a given input r,g,b
 *
 * Extended palette has 6 shades of each color */

// Draw the 6 shades of green
U8 g=0;
I64 i;
for (i=0;i<TR_WIDTH;i++)
{
PenSetColor(GetColorNum(0,(i/36)*0x33,0));
TSetPos(i,TR_HEIGHT);
TFd(TR_HEIGHT);
}
```
