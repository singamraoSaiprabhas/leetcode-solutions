class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closest_x = max(x1, min(xCenter, x2))
        
        # Find the y-coordinate of the closest point on the rectangle to the circle's center
        # We clamp the circle's yCenter to be within the rectangle's y-bounds [y1, y2]
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate the squared distance between the circle's center and this closest point
        distance_x = xCenter - closest_x
        distance_y = yCenter - closest_y
        
        # Check if the squared distance is less than or equal to the squared radius
        # Using squared distances avoids floating-point inaccuracies from square root calculations
        return (distance_x ** 2 + distance_y ** 2) <= (radius ** 2)