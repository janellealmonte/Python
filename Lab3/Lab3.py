#!/usr/bin/env python3

def write_text(name):
    f= open("name.txt","w+")
    f.write(name)
    f.close()
    
if __name__ == '__main__':   # This section also referred to as a "main block"

    write_text('Janelle Marie Almonte')
