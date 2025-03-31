# Q2: Set operations on veg_dis and non-veg_dis dishes

def set_operations(veg_dis, non_veg_dis):
    # Union
    all_dishes = veg_dis.union(non_veg_dis)
    
    # Intersection
    common_dishes = veg_dis.intersection(non_veg_dis)
    
    # Subset check
    is_subset = veg_dis.issubset(non_veg_dis)

    return all_dishes, common_dishes, is_subset

veg_dishes = {"Paneer Tikka", "Vegetable Biryani", "Aloo Paratha"}
non_veg_dishes = {"Chicken Curry", "Mutton Biryani", "fish Biryani"}
print(set_operations(veg_dishes, non_veg_dishes))