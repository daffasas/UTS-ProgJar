import json
import socket

def create_comment(url, comment_data):
  """Posts a new comment to the specified URL using a socket connection.

  Args:
      url: The URL of the endpoint to post the comment to. (e.g., "jsonplaceholder.typicode.com/comments")
      comment_data: A dictionary containing the comment details (postId, name, email, body).

  Returns:
      The ID of the newly created comment, or None if an error occurs.
  """
  try:
    # Convert comment data to JSON string
    json_data = json.dumps(comment_data)
    # Encode data and calculate content length
    data = json_data.encode()
    content_length = len(data)

    # Create a socket connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect((url, 80))  # Connect to server on port 80 (default for HTTP)

      # Build the HTTP request message
      request = f"POST /comments HTTP/1.1\r\nHost: {url}\r\nContent-Type: application/json\r\nContent-Length: {content_length}\r\nConnection: close\r\n\r\n{data.decode()}"

      # Send the request
      sock.sendall(request.encode())

      # Receive the response
      response = sock.recv(4096).decode()

      # Check for successful response (status code 201)
      if "201 Created" in response:
        # Extract the ID from the response (assuming JSON format)
        for line in response.splitlines():
          if line.startswith("Location: "):
            return int(line.split("/")[-1])
      else:
        print(f"Error creating comment: {response}")
        return None

  except Exception as e:
    print(f"An error occurred: {e}")
    return None

# Comment data
comment = {
    "postId": 1,
    "name": "Test Name",
    "email": "test@example.com",
    "body": "This is a test comment."
}

# Target URL
url = "jsonplaceholder.typicode.com/comments"

# Create the comment and print the ID
new_comment_id = create_comment(url, comment)

if new_comment_id:
  print(f"New comment ID: {new_comment_id}")
else:
  print("Failed to create comment.")
