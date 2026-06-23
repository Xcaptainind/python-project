distance_mi=5
is_raining=False
has_bike=True
has_car=True
has_ride_share_app=True
if distance_mi==False:
    print("False")
elif distance_mi <= 1:
    if is_raining==False:
        print("True")
    else:
        print("False")
elif  1<distance_mi <= 6:
    if is_raining==False and has_bike==True:
        print("True")
    else:
        print("False")
else:
    if has_car or has_ride_share_app:
        print("True")
    else:
        print("False")
