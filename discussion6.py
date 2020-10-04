# Discuission 7 Debugger

# This function returns the largest number and assign to "top"
def top_list(num_list):
    print("top_list start")
    sortA = sorted(num_lis)
    top = sortA
    print("top_list end")
    return top

# This function returns the key-value pair of most populate city and assign to "top"
def top_dict(city_dict):
    print("top_dict start")
    sortB = city_dict.items(), key=lambda x: x[1]
    top = sortB[0]
    print("top_dict end")
    ret top

# Task 1: Find out the largest number in the list
num_list = [3,5,22,110,238,12,183,62,682,0,532,991,3,1023,1983,1829,11,193,121,1538,10099,1223,432,5552,1083,1023,1983,1829,11,193,121,1538,10099,1223,432,5552,1083,1023,1983,1829,11,193,121,1538,10099,1223,432,5552,108243,1023,1983,1829,11,193,121,15338,10099,1223,432,5552,1083]
top_list(num_list)

# Task 2: Find out the most populated city
city_list = {'Lima':8481415,'Bangkok':8249117,'Cairo':10230350,'Tehran':846782,'Moscow':11541000,'New Delhi':16787949,'Jakarta':10187595,'Kinshasa':10125000,'Seoul':9989795,'Mexico City':8985339,'Manila':12877253,'Dhaka':8906000,'London':8630100,'Hanoi':7587800,'Hong Kong':7482500,'Tokyo':13742906}
top_dict(city_list)
