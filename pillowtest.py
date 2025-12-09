from PIL import Image, ImageDraw
W, H = 800, 600
cx, cy = W // 2, H // 2
canvas = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(canvas)
side = 500
h_tri = (3**0.5 / 2) * side

points = [
    (cx, cy - h_tri/2),                # top
    (cx - side/2, cy + h_tri/2),       # bottom-left
    (cx + side/2, cy + h_tri/2)        # bottom-right
]

draw.polygon(points, outline="black", width=4)
canvas.save("triangle.png")
