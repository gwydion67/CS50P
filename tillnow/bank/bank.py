st = (input("Greeting: ")).strip().lower()
if(st.startswith('hello')):
    print("$0")
elif(st.startswith("h")):
    print("$20")
else:
    print("$100")