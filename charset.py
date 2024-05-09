import requests

def get_charset(url):
  """Fetches the charset encoding from the Content-Type header of the response.

  Args:
      url: The URL of the website to visit.

  Returns:
      The charset string extracted from the Content-Type header, or None if not found.
  """
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for non-2xx status codes
    content_type = response.headers.get('Content-Type')
    if content_type:
      # Split and extract charset from Content-Type header
      charset = content_type.split("; charset=")[-1].strip()
      return charset
    else:
      return None
  except requests.exceptions.RequestException as e:
    print(f"Error occurred while fetching data: {e}")
    return None

# Example usage
url = "https://classroom.its.ac.id"
charset = get_charset(url)

if charset:
  print(f"Charset: {charset}")
else:
  print("Charset not found in response header.")
