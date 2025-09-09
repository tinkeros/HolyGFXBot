
## HolyGFXBot

### Valid commands are:
 - `!hg` - creates single frame static image
 - `!hgds` creates animated "ditherspark" GIF (draws the same frame 4 times with different dithering and loops)

### Optional space delimited image dimension parameters (each should be a multiple of 8):
- `width` - image width (default 240, up to 1920)
- `height` - image height (default 240, up to 1080)

### Required code parameter only 1 of the following:
- Code block of text
- Attached .HC or .TXT file with code to execute

### Drawing:
  - The standard TempleOS graphics API can be used to draw to `dc`
  - Color pixel at x,y with color c manually by: `dc->body[y*dc->width+x]=c;`

### Default Color Map:
[Temple/TinkerOS default color maps](https://tinkeros.github.io/palette.html)

## Examples:
