import numpy

def Main():
    print("\n")
    print("--- Return Calculator ---")
    print("The investment horizon is two periods long.")
    n = int(input("How many periods are there in one year? "))
    values = []
    flows = []
    initial = int(input("What is the value of your initial investment? "))
    values.append(initial)
    cfinitial = initial*(-1)
    flows.append(cfinitial)
    period = 1
    while period == 1:
        value = int(input("Please enter the value of the investment at t = " + str(period) + ": "))
        values.append(value)
        cf = int(input("Please enter the value of any additional cash flow at t = " + str(period) + ": "))
        if cf != 0:
            sign = input("Is this a cash inflow or outflow? ")
            if sign.lower() == "inflow":
                flows.append(cf)
            elif sign.lower() == "outflow":
                cf = cf*(-1)
                flows.append(cf)
            else:
                print("Error 1")
        elif cf == 0:
            flows.append(cf)
        period += 1
    while period == 2:
        sale = int(input("Please enter the value from selling your shares at t = " + str(period) + ": "))
        values.append(sale)
        flows.append(sale)
        period += 1
    print("-----------------------------------------")
    print("At t=0, the investment cost: " + str("${0:.0f}".format(values[0])))
    print("At t=1, the investment was valued at: " + str("${0:.0f}".format(values[1])))
    if cf != 0:
        print("At t=1, there was a cash " + str(sign.lower()) + " of: " + str("${0:.0f}".format(abs(cf))))
    print("At t=2, you sold your shares for: " + str("${0:.0f}".format(sale)))
    print("-----------------------------------------")
    x = (-flows[1]+numpy.sqrt((flows[1]**2)-4*flows[2]*flows[0]))/(2*flows[2])
    dwr = ((1-x)/x)
    dwa = (1+dwr)**n
    dwr = dwr*100
    dwa = (dwa-1)*100
    dwr = "{0:.3f}%".format(dwr)
    print("The dollar-weighted return is: " + str(dwr))
    dwa = "{0:.3f}%".format(dwa)
    print("The annualized return is: " + str(dwa))
    print("\n")
    twreturns = []
    rt1 = (values[1] - values[0])/values[0]
    rt1 = rt1 + 1
    rt2 = (values[2] - values[1] + flows[1])/(values[1]-flows[1])
    rt2 = rt2 + 1
    twreturns.append(rt1)
    twreturns.append(rt2)
    xy = numpy.prod(twreturns)
    exp = n/2
    twr = (xy - 1)*100
    twa = ((((.01*twr)+1)**exp)-1)*100
    twr = "{0:.3f}%".format(twr)
    print("The time-weighted return is: " + str(twr))
    twa = "{0:.3f}%".format(twa)
    print("The annualized return is: " + str(twa))
 
    
Main()
