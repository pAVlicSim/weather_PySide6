from PySide6.QtGui import QPen


class MyPen(QPen):

    def __init__(self, pen_color=None, pen_width=None):
        super().__init__()
        self.setColor(pen_color)
        self.setWidth(pen_width)
