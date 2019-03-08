######################## collision code #############################
def IsColliding(x1, y1, width1, height1, x2, y2, width2, height2):
    return not(x1 > (x2 + width2) or \
               y1 > (y2 + height2) or \
               x2 > (x1 + width1) or \
               y2 > (y1 + height1))
#####################################################################