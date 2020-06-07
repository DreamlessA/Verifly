import base64
import sys

def string_to_base64(msg):
    msg_bytes = msg.encode('ascii')
    return byte_to_base64(msg_bytes)

def base64_to_string(base64_msg):
    msg_bytes = base64_to_byte(base64_msg)
    msg = msg_bytes.decode('ascii')
    return msg

def byte_to_base64(msg_bytes):
    b64_bytes = base64.b64encode(msg_bytes)
    b64_msg = b64_bytes.decode('ascii')
    return b64_msg 

def base64_to_byte(base64_msg):
    b64_bytes = base64_msg.encode('ascii')
    msg_bytes = base64.b64decode(b64_bytes)
    return msg_bytes 

if __name__ == "__main__":
    infile_path = sys.argv[1]
    infile = open(infile_path, 'r+b')
    data = infile.read()
    b64_data = byte_to_base64(data)
    outfile_path = infile_path + "_b64"
    outfile = open(outfile_path, 'w')
    outfile.write(b64_data)