from mouseMover import MouseMover
from appFrame import AppFrame

mover = MouseMover(10)
app = AppFrame(mover, 1000)
app.runApp()
