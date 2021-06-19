def type_of_triangle(a, b, c): 
    triangles = ["Equilateral","Isosceles","Scalene"]
    sides = [a,b,c]
    if all(type(d) == int for d in sides):
        sumSides = [b+c,a+c,b+a]         
        for index,value in enumerate(sides):
            if value >= sumSides[index]:
                return "Not a valid triangle"
        sides = len(set(sides))
        return triangles[sides-1]
    return "Not a valid triangle"