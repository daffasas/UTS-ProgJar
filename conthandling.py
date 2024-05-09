import hashlib
import requests

def get_content_encoding(url):
  """Fetches the Content-Encoding from the response header of the visited site.

  Args:
      url: The URL of the website to visit.

  Returns:
      The Content-Encoding string extracted from the response header, or None if not found.
  """
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for non-2xx status codes

    # Access the raw request data using str(response.request)
    request_data = str(response.request).encode()
    request_checksum = hashlib.sha256(request_data).hexdigest()

    # ... rest of the code for calculating other checksums and processing content encoding ...

  except requests.exceptions.RequestException as e:
    print(f"Error occurred while fetching data: {e}")
    return None

# ... example usage ...


# Example usage
url = "https://classroom.its.ac.id"
get_content_encoding(url)
