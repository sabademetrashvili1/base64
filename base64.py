import base64

def base64_encode():
    string = input("Enter string: ")
    string_bytes = string.encode("ascii")


    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")

    print("Encoded string: %s" % base64_string)


base64_encode()

def base64_decode():
    base64_string = input("Enter decoded string: ")
    base64_bytes = base64_string.encode('ascii')

    string = base64.b64decode(base64_bytes)
    string_bytes = string.decode('ascii')

    print("Decoded string: %s" % string_bytes)

base64_decode()
