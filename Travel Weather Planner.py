distance_mi=5
is_raining=bool(input("Is it raining? (True/False): "))
has_bike=bool(input("Do you have a bike? (True/False): "))
has_car=bool(input("Do you have a car? (True/False): "))
has_ride_share_app=bool(input("Do you have a ride share app? (True/False): "))
if distance_mi<=1 and is_raining==False:
    print("True") 
elif distance_mi<=1 and is_raining==True:
    print("False")
elif distance_mi>1 and distance_mi<=6 and(has_bike==False and is_raining==True):
       print("False")
elif distance_mi>1 and distance_mi<=6 and (is_raining==False and has_bike==False):
        print("False")
elif distance_mi>1 and distance_mi<=6 and (has_bike==True and is_raining==False):
    print("True")
elif distance_mi>6 and has_ride_share_app==True:
    print("True")
elif distance_mi>=6 and has_car==True:
    print("True")
elif distance_mi>6 and (has_car==False and has_ride_share_app==False):
    print("False")  
else:
    print("Your data is incorrect")               