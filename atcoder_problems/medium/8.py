N = int(input())
rates = list(map(int,input().split(" ")))
color_counter = [0] * 9

for rate in rates:
    if rate <= 399:
        color_counter[0] += 1
    elif 400 <= rate and rate <= 799: 
        color_counter[1] += 1        
    elif 800 <= rate and rate <= 1199: 
        color_counter[2] += 1
    elif 1200 <= rate and rate <= 1599: 
        color_counter[3] += 1
    elif 1600 <= rate and rate <= 1999: 
        color_counter[4] += 1
    elif 2000 <= rate and rate <= 2399: 
        color_counter[5] += 1
    elif 2400 <= rate and rate <= 2799:
        color_counter[6] += 1
    elif 2800 <= rate and rate <= 3199:
        color_counter[7] += 1        
    else: 
        color_counter[8] += 1

base_color_count = sum(1 for i in range(len(color_counter)-1) if color_counter[i] > 0)
min_count = 1 if base_color_count == 0 else base_color_count

print(f"{min_count} {base_color_count + color_counter[8]}")
