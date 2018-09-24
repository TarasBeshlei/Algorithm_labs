from lift import Lift
from quick_sort import Quicksort
from selection_sort import selection_sort




if __name__ == "__main__":
    lifts_list = []

    lift1 = Lift(234, 124)
    lift2 = Lift(124, 4224)
    lift3 = Lift(7654, 14224)
    lift4 = Lift(544, 3224)
    lift5 = Lift(5434, 2324)

    lifts_list.append(lift1)
    lifts_list.append(lift2)
    lifts_list.append(lift3)
    lifts_list.append(lift4)
    lifts_list.append(lift5)

    for lift in lifts_list:
        print (lift.power)
    print "------------------------------------------------------------------------------------------------"

    selection_sort(lifts_list)

    for lift in lifts_list:
        print (lift.power)
    print "------------------------------------------------------------------------------------------------"

    for lift in lifts_list:
        print (lift.capacity)
    print "------------------------------------------------------------------------------------------------"

    quicksort = Quicksort(lifts_list)
    quicksort.quick_sort(0, len(lifts_list) - 1)

    for lift in lifts_list:
        print (lift.capacity)
