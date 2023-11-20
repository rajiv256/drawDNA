import random
import re
import turtle
from globals import FONT_KWARGS
from src.dsDNA import Domain


class DNATurtle(object):
    def __init__(self, color='black', width=3,
                 label='Hello', pos=(0, 0), **kwargs):
        self.color = color
        self.width = width
        self.label = label
        self.pos = pos
        self.smalldashdims = kwargs.get('smalldashdims', 6)
        self.smalldashwidth = kwargs.get('smalldashwidth', 1)
        self.arrowlength = kwargs.get('arrowlength', 6)
        self.arrowangle = kwargs.get('arrowangle', 140)
        self.T = turtle.Turtle()
        self.T.shape('blank')

    def _goto(self, pos=(0, 0)):
        self.T.pu()
        self.T.setposition(pos)
        self.T.pd()

    def _set_color(self, color='blue'):
        self.T.color(color)

    def _set_width(self, width=2):
        self.T.width(width)

    def _set_label(self, label='Hello', **kwargs):
        self.T.write(label, **kwargs)

    def _reset_T(self, color='black', width=10, label=''):
        self._set_color(color)
        self._set_width(width)
        self.set_label(label)

    def _draw_small_dash(self):
        # Use this cautiously
        self._set_width(self.smalldashwidth)
        self.T.rt(90)
        self.T.fd(self.smalldashdims // 2)
        self.T.lt(180)
        self.T.fd(self.smalldashdims)
        self.T.rt(180)
        self.T.fd(self.smalldashdims // 2)
        self.T.lt(90)

    def _draw_arrow(self):
        self.T.rt(self.arrowangle)
        self.T.fd(self.arrowlength)
        self.T.fd(-self.arrowlength)
        self.T.lt(2*self.arrowangle)
        self.T.fd(self.arrowlength)
        self.T.fd(-self.arrowlength)
        self.T.rt(self.arrowangle)

    def draw_domain(self, domain, terminal=False):
        """
        """
        self._goto(domain.startpos)
        self.T.setheading(domain.angle)
        self._draw_small_dash()
        # Draw the domain
        self._set_width(domain.width)
        self.T.fd(domain.distance//2)
        self.T.write(domain.label, **FONT_KWARGS)
        self.T.fd(domain.distance // 2)

        if not terminal:
            self._draw_small_dash()
        else:
            self._draw_arrow()


if __name__ == '__main__':
    dt = DNATurtle()
    dt.draw_domain(startpos=(0, 0), angle=30, terminal=True)
    turtle.mainloop()
