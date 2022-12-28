class Rectangle:
    def __init__(self,width,height):
        self.width = 0
        self.height = 0
        self.set_width(width)
        self.set_height(height)
    
    def set_width(self,width):
        self.width = width
    
    def set_height(self,height):
        self.height = height
    
    def get_area(self):
        return (self.width * self.height)
    
    def get_perimeter(self):
        return ((2 * self.width) + (2 * self.height))
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        if self.width>50 or self.height>50:
            return 'Too big for picture.'
        s = ''
        for h in range(self.height):
            for w in range(self.width):
                s = s+'*'
            s = s +'\n'
        
        return s
    
    def get_amount_inside(self,c):
        a = (self.width - (self.width%c.width))/c.width
        b = (self.height - (self.height%c.height))/c.height
        return int(a*b)
        
    def __str__(self):
        a = 'Rectangle(width={}, height={})'.format(self.width, self.height)
        return a
class Square(Rectangle):
    def __init__(self,side):
        self.width = 0
        self.height = 0
        self.set_side(side)
    
    def set_side(self,side):
        self.set_width(side)
        self.set_height(side)
    
    def __str__(self):
        a = 'Square(side={})'.format(self.width)
        return a
