try:
            bagi = 8 / 0

            print (bagi)

except ZeroDivisionError:
        print("eror: pemagian nol")

finally:
        print ("block finaly tetap di eksekusi")