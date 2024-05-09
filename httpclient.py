import socket
import re

def get_first_length(data: str) -> int:
    """
    Get the length of the header plus the content length (if exists).
    """
    # Split the response into header and body
    header, _, body = data.partition('\r\n\r\n')
    
    # Calculate the length of the header
    header_length = len(header.encode())
    
    # Extract Content-Length from the header using regular expression
    content_length_match = re.search(r'Content-Length: (\d+)', header)
    if content_length_match:
        content_length = int(content_length_match.group(1))
        return header_length + content_length
    else:
        return header_length

def create_socket() -> socket.socket:
    """
    Create a socket and connect it to the server at 'localhost' on port 8080.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8080))
    return s

def client() -> None:
    """
    Create a socket, send a GET request for 'index.html', and process the response.
    """
    s = create_socket()
    request = b'GET index.html HTTP/1.1\r\nHost: localhost\r\n\r\n'
    s.send(request)
    
    response = b''
    while True:
        data = s.recv(1024)
        if not data:
            break
        response += data
        if len(data) < 1024:
            break
    
    print(response.decode())
    s.close()

# Testing the functions
def test_client():
    print("Testing client ...")
    client()

def test_create_socket():
    print("Testing create_socket ...")
    s = create_socket()
    s.close()

def test_get_first_length_no_content_length():
    print("Testing get_first_length_no_content_length ...")
    data = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>Hello world!</title></head><body>Hello world!</body></html>"
    assert get_first_length(data) == 159, "Length should be 159"

def test_get_first_length_with_content_length():
    print("Testing get_first_length_with_content_length ...")
    data = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 188\r\n\r\n<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>Hello world!</title></head><body>Hello world!</body></html>"
    assert get_first_length(data) == 347, "Length should be 347"

# Run tests
test_client()
test_create_socket()
test_get_first_length_no_content_length()
test_get_first_length_with_content_length()
