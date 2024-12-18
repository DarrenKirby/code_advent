using DelimitedFiles

dim_array = readdlm("./advent/input2.txt", 'x', Int)
arr_l, _ = size(dim_array)

total_sqft = 0
total_feet = 0

for i in 1:arr_l
    # l * w * h
    # side areas
    a1 = dim_array[i,1] * dim_array[i,2] # l * w
    a2 = dim_array[i,2] * dim_array[i,3] # w * h
    a3 = dim_array[i,3] * dim_array[i,1] # h * l
    smallest_area = min(a1, a2, a3)
    this_sqtf = smallest_area + a1*2 + a2*2 + a3*2
    total_sqft += this_sqtf

    # side perimeters
    p1 = (dim_array[i,1] + dim_array[i,2]) * 2
    p2 = (dim_array[i,2] + dim_array[i,3]) * 2
    p3 = (dim_array[i,3] + dim_array[i,1]) * 2
    smallest_perimeter = min(p1, p2, p3)
    this_feet = smallest_perimeter + (dim_array[i,1] * dim_array[i,2] * dim_array[i,3])
    total_feet += this_feet

end
println("Wrapping paper needed: $total_sqft sqft")
println("Ribbon needed: $total_feet feet")
