"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos from the user. Then your program should compute
and display the total weight of the parts.
"""

widgets_number = int(input("Enter number of widgets: "))
gizmos_number = int(input("Enter number of gizmos: "))

widget_weight = 75 
gizmo_weight = 112 
total_weight = (widgets_number * widget_weight) + (gizmos_number * gizmo_weight)      

print("The total weight of all parts is {}g".format(total_weight))