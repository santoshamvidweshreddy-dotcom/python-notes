#1)
try:
    x=10/0
except ZeroDivisionError:
    print("❌ cannot divide by zero")
finally:
    print("✅ program ended")

#2)
try:
    num=int("abc")
    result=10/0
except ValueError:
    print("❌ invalid numbers")
except ZeroDivisionError:
    print("❌ cannot divide by zero")
finally:
    print("✅ done")

#3)
try:
    f=open("data.txt")
except Exception as e:
    print("Error:",e)
finally:
    print("File handling attempted")