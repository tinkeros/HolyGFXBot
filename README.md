
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

### Optional defines and variable (hgds only)
- Define up to 100 frames to be drawn with `#define NUM_FRAMES 100`
- Use frame count variable `frame_num` in your code to change what you draw (goes from 0 to NUM_FRAMES - 1).
- Each frame is drawn for 1/10th of a second.
- The dc/image width is `TR_WIDTH` and height is `TR_HEIGHT` (set by width/height parameters following hg or hgds)

### Drawing:
  - The standard TempleOS graphics API can be used to draw to `dc`
  - Color pixel at x,y with color c manually by: `dc->body[y*dc->width+x]=c;`

### Default Color Map:
[Temple/TinkerOS default color maps](https://tinkeros.github.io/palette.html)

### You can change colors 0-254 to be whatever RGB888 value you want with:
 - `GrSetRGB(I64 color_number, U8 red, U8 green, U8 blue);`

## Examples (cool things you can draw with <= 2000 discord characters):

### 42x42 Chad
<center><img src="https://tinkeros.github.io/HolyGFX/Chad.png"></center>
!hg 42 42

```
U8*p="NAMAKBJBHAEEFAHAGAHEGAHBJALAMBNCODNBOFODMAJAHBEEHAGAHHIALAMAOINALAOEOFJAHAEAFADAEBHJLAOKNAJAIAODOGHAEBFAECGAHBGBHAIAJALAOCNAOAMANAOENALAJAODOGKAFAECFAEAHAGBHCJALAOCNDOEMBIAHANAOCOHFBEEHDJALAOCNALCNBODNALAJAHAMAOCOHHAFAECFAEBHBJAOENCOGNCHAJAOCOHKAFAEFIANAOENCOHNAMANAJBOCOHLAEEHALAOGNBOHMALBNAJALAOCOHNAFAECJAMAOHNAOJLAHALBMAOCOIFAEBJAOANBMANAOENAOINALAHALBNAOCOIGAEAFAMCLAMBOENAOJLAIALANALAOCOIHAEAHANAKBLANCODNAOEMDLAHADAFANCOBOIJAEAIALBJALBMAOENAODMALAIAJALBHADAFAOALAMAOBOILAFAHALAJBIALANAMAODNAOCNALEJACAEAOBLBOBOJFAHAKAJAIAJALAMANAODLAOCLCIAHAFAHACAJBLBJAOBOJEAHALAIALBMBLAODLAOCNAJAEAIAJBNALAIAEALBFAOBOJEBLAIALAJALCNAOBNALAOCNALAIAKALBNBJBLANADAMAOAOJFAEALBKAJALBMBOBLAIAOCNBMANAOAMANAOAIALAJANADAHAOAOINAHBIALBJBKANAMBOAJAGAOKHAJALAOAFAAAOAOHNAHAEAHBMALAJALDMAOALAHAJAOCNCOANALAJBLAJANAEA@AOAOHJAHBEBNAKAJANAJAIAJAIALAKAHAJBOBNALBHALAMAJAHALAFAJAFACAOAOHJCGAFALCJAHDJALAIAJALBOBNALAEAFAHAEAHALAEAHBDAOAOHNAKADACAFAJAMALAJAHDGAHAJAKALAKAMANAOAMAIBHAGAHAJAHALAJAIAOAOGLAOAMAHAEBJAMAKAGAHCGAHCJALBMANCHAFAEAHBIANBHAOBOGKAJALAMAHBLAMAJAHEEAHAGAIAKALANCLAJAFAEAHAIAKAOALCOAOHGAHBEBKAIAHAFBGAFAEAHBIBKANBOBNAJBEAJBLAOCNALAOHKAHBCAEALAIAGAECHAGBJBKAMBOEIAFAHAGAOCNAFAIAOHNAFAEBHALBGAECHCIAKALANBOEJAFAIAEAOCNALAMAOHNAJAGALBMANAJAECHCLAMBLANAOELAHAJAHAMAOCLANAOINBMANBMAIAECGBHAIAJANAOGNBMAJALANALAJAMAOAOKNAMANAMALAECHCJAIAJALAKANBOEMBHAJAEADAOBOKNAMANAMALAHAEBGBHAIALCNBODNAMALAKAJCHADBOBOMMAKAMALAHAFAEAGAHBIALAMBOCMANBJAGAIAJAFAEAGAOBOINAOCMALDHAFAEBHAGBJALAMANALDJAHAJBEBHAOBOJNBOAMALDJBHAFAHCOCKBLBJCHAFADAKAOBOINAOANAMAOAMCLAJBIAHAEAHCJALGJBHAFACAOCOLNAMCNBIAJAHCGAHAGAJBLFJAHBEAIAOCOKNAMALAMANAMBLAIAHAGAHDIAJCLDHBFBODOMNAOCMBJAGAHBEAHAIBJBLDJAHBFALAODOKNBMBNDLAJAHAGBJBIAJALAIALDJAHAJAOEOKNAKANAOCLAMALCJAIAJBKALAMAOANAOANAOBNAOFOONEKALCNBOOOAONNBOANAMBNALANAMAOOOCOOOANBMANALBMANBOANAOOOOOCNBLANAMANBOOBBOOODNCMAOOODOOOOOL",x,n;
U64 i=0;while(*p){x=*p++-'@';n=*p++-'@';while(n--)dc->body[dc->width*(41-i/42)+i++%42]=15-x;}GrPaletteSet(gr_palette_gray);
```

### 240x240 TempleOS dithersparkle sword
<center><img src="https://tinkeros.github.io/HolyGFX/SwordDS.gif"></center>
!hgds

```
U8 *sw="Mesh{FALSE,(0,-293,0),(15,-263,0),(-18,-263,0),(15,176,0),    //3
(-18,176,0),(0,-263,2),(0,176,2),(0,-263,-4),    //7
(0,176,-4),(-52,176,-11),(50,176,-11),(50,196,-11),    //11
(-52,196,-11),(-52,176,9),(50,176,9),(50,196,9),    //15
(-52,196,9),(-35,176,-11),(-52,159,-11),(-52,176,-11),    //19
(-35,176,9),(-52,159,9),(-52,176,9),(50,176,-11),    //23
(50,159,-11),(32,176,-11),(50,176,9),(50,159,9),    //27
(32,176,9),(-15,196,-11),(13,196,-11),(9,295,-11),    //31
(-11,295,-11),(-15,196,9),(13,196,9),(9,295,9),    //35
(-11,295,9):(TWO|HALF|15,3,6,5),(TWO|HALF|15,5,1,3),
(TWO|HALF|15,6,4,2),(TWO|HALF|15,2,5,6),(TWO|HALF|15,0,1,5),
(TWO|HALF|15,5,2,0),(TWO|HALF|15,0,2,7),(TWO|HALF|15,7,1,0),
(TWO|HALF|15,7,8,3),(TWO|HALF|15,3,1,7),(TWO|HALF|15,7,2,4),
(TWO|HALF|15,4,8,7),(TWO|HALF|14,9,10,14),(TWO|HALF|14,14,13,9),
(TWO|HALF|14,10,11,15),(TWO|HALF|14,15,14,10),(TWO|HALF|14,11,12,16),
(TWO|HALF|14,16,15,11),(TWO|HALF|14,12,9,13),(TWO|HALF|14,13,16,12),
(TWO|HALF|14,9,10,12),(TWO|HALF|14,10,11,12),(TWO|HALF|14,14,13,16),
(TWO|HALF|14,15,14,16),(TWO|HALF|14,17,18,21),(TWO|HALF|14,21,20,17),
(TWO|HALF|14,18,19,22),(TWO|HALF|14,22,21,18),(TWO|HALF|14,19,17,20),
(TWO|HALF|14,20,22,19),(TWO|HALF|14,17,18,19),(TWO|HALF|14,21,20,22),
(TWO|HALF|14,23,24,27),(TWO|HALF|14,27,26,23),(TWO|HALF|14,24,25,28),
(TWO|HALF|14,28,27,24),(TWO|HALF|14,25,23,26),(TWO|HALF|14,26,28,25),
(TWO|HALF|14,23,24,25),(TWO|HALF|14,27,26,28),(TWO|HALF|15,29,30,34),
(TWO|HALF|15,34,33,29),(TWO|HALF|15,30,31,35),(TWO|HALF|15,35,34,30),
(TWO|HALF|15,31,32,36),(TWO|HALF|15,36,35,31),(TWO|HALF|15,32,29,33),
(TWO|HALF|15,33,36,32),(TWO|HALF|15,29,30,32),(TWO|HALF|15,30,31,32),
(TWO|HALF|15,34,33,36),(TWO|HALF|15,35,34,36)};
";
CDoc *d=DocNew;
Mat4x4Scale(dc->r,0.4);
Mat4x4RotZ(dc->r,0.5);
DocPrint(d,"%s",sw);
Sprite3B(dc,120,120,0,Code2Sprite(d));
```

### 120x32 Blink Test
<center><img src="https://tinkeros.github.io/HolyGFX/blink.gif"></center>
!hgds 120 32

```
#define NUM_FRAMES 100
if ((frame_num/2)%2) {
  DCFill(dc,BLACK);
  dc->color=WHITE;
}
else {
  DCFill(dc,WHITE);
  dc->color=BLACK;
}
U8 *str="Blink Test!";
I64 x=TR_WIDTH/2 - 8*StrLen(str)/2;
GrPrint3(dc,x,TR_HEIGHT/2-4,0,str);
```


### 160x160 Hexagonal Prism
<center><img src="https://tinkeros.github.io/HolyGFX/hexp.gif"></center>
!hgds 160 160

```
#define PI 3.14159
#define NUM_SIDES 6
#define NUM_FRAMES 100
static CD3I32 top_poly[NUM_SIDES];
static CD3I32 bottom_poly[NUM_SIDES];
static CD3I32 side_face[NUM_SIDES][4];
Mat4x4RotX(dc->r,ToF64(frame_num)*PI/4.0);
Mat4x4RotZ(dc->r,ToF64(2.0*frame_num)*PI/ToI64(NUM_FRAMES));
dc->flags|=DCF_TRANSFORMATION;
dc->x=TR_WIDTH/2;
dc->y=TR_HEIGHT/2;
dc->thick=1;
dc->dither_probability_u16=1<<15;

F64 angle, angle_step, height, radius, x_off, y_off, z_off;

I64 i, next;
angle_step = 2.0 * PI / NUM_SIDES;
radius = 50.0;
height = 75.0;

for (i=0; i<NUM_SIDES; i++) {
    angle = angle_step * i;
    x_off = radius * Cos(angle);
    y_off = radius * Sin(angle);
    z_off = height / 2.0;

    top_poly[i].x = ToI64(x_off);
    top_poly[i].y = ToI64(y_off);
    top_poly[i].z = ToI64(z_off);

    bottom_poly[i].x = ToI64(x_off);
    bottom_poly[i].y = ToI64(y_off);
    bottom_poly[i].z = ToI64(-z_off);
}

dc->color=ROPF_PROBABILITY_DITHER+DKGRAY<<16+WHITE;
GrFillPoly3(dc,NUM_SIDES,&bottom_poly);

dc->color=ROPF_PROBABILITY_DITHER+CYAN<<16+BLUE;
GrFillPoly3(dc,NUM_SIDES,&top_poly);

for(i=0; i<NUM_SIDES; i++) {
    next = (i + 1) % NUM_SIDES;

    MemCpy(&side_face[i][0],&bottom_poly[i],sizeof(CD3I32));
    MemCpy(&side_face[i][1],&bottom_poly[next],sizeof(CD3I32));
    MemCpy(&side_face[i][2],&top_poly[next],sizeof(CD3I32));
    MemCpy(&side_face[i][3],&top_poly[i],sizeof(CD3I32));

    dc->color=ROPF_PROBABILITY_DITHER+(BLUE+8+i)<<16+(BLUE+i);
    
    GrFillPoly3(dc,4,&side_face[i]);
}
```

### 240x240 Texas dithersparkle flag
<center><img src="https://tinkeros.github.io/HolyGFX/TXDS.gif"></center>
!hgds

```
dc->color=WHITE;
GrPrint(dc,0,8,"       I've been sent to\n      spread the message!");
static CD3I32 t1[3] = { {40, 90, 0}, {47, 110, 0}, {33, 110, 0} };
static CD3I32 t2[3] = { {68, 110, 0}, {52, 124, 0}, {47, 110, 0} };
static CD3I32 t3[3] = { {59, 145, 0}, {40, 132, 0}, {52, 124, 0} };
static CD3I32 t4[3] = { {21, 145, 0}, {28, 124, 0}, {40, 132, 0} };
static CD3I32 t5[3] = { {12, 110, 0}, {33, 110, 0}, {28, 124, 0} };
static CD3I32 p[5] = { {47, 110, 0}, {52, 124, 0}, {40, 132, 0}, {28, 124, 0}, {33, 110, 0} };
dc->thick=1;
dc->dither_probability_u16=1<<15;
dc->color=ROPF_PROBABILITY_DITHER+BLUE<<16+LTBLUE;
GrRect3(dc,0,40,0,240,160);
dc->color=ROPF_PROBABILITY_DITHER+RED<<16+LTRED;
GrRect3(dc,80,120,0,160,80);
dc->color=ROPF_PROBABILITY_DITHER+LTGRAY<<16+WHITE;
GrRect3(dc,80,40,0,160,80);
GrFillPoly3(dc,3,&t1);
GrFillPoly3(dc,3,&t2);
GrFillPoly3(dc,3,&t3);
GrFillPoly3(dc,3,&t4);
GrFillPoly3(dc,3,&t5);
GrFillPoly3(dc,5,&p);
GrPrint(dc,0,216,"       God Bless Texas!");
```

