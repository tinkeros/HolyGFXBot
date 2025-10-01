import sys

# convert_raw_to_c.py
with open(sys.argv[1], "rb") as f:
    data = f.read()

width = int(sys.argv[2])
height = int(sys.argv[3])

if len(data) == 2*width*height:
    print("Your image is double the size it should be!  Remove the alpha channel and re-export it!")
    sys.exit(1)

if len(data) != width*height:
    print(f"Your image dimensions are incorrect! {sys.argv[1]} is not exactly {width} x {height} = {width*height} bytes!  Make sure you exported it as RAW!")
    sys.exit(1)

print("static U8 image[{}][{}] = {{".format(height, width))
for y in range(height):
    row = data[y*width:(y+1)*width]
    print("    {" + ", ".join(f"{b}" for b in row) + "},")
print("};")

prg='''
I64 x,y;
for (x=0;x<%d;x++)
  for (y=0;y<%d;y++)
    dc->body[%d*y+x]=image[y][x];
'''%(width,height,width)
print("\n")
print(prg)
print("\n")

