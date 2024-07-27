import json
from parse_html import HTMLParser

def lambda_handler(event, context):
    print(event)

test = HTMLParser.get_name


lambda_handler(test, None)

import json
from parse_html import HTMLParser

def lambda_handler(event, context):
    print(event)
    # Extracting the file path from the event, if provided
    file_path = event.get('file_path', 'sample.html')  # Use a default if file_path is not in the event

    # Create an instance of HTMLParser
    parser = HTMLParser(file_path)
    
    # Retrieve data using the methods of HTMLParser
    json_output = {
        'name': parser.get_name(),
        'metascore': parser.get_metascore(),
        'image_url': parser.get_image_url()
    }
    
    # Print the extracted JSON data
    print(json.dumps(json_output, indent=4))

    # Return the extracted JSON data
    return {
        'statusCode': 200,
        'body': json.dumps(json_output)
    }

# For local testing, you can call lambda_handler directly with a sample payload
if __name__ == "__main__":
    sample_event = {
        'file_path': 'sample.html'  # Update this if your test file is located elsewhere
    }
    lambda_handler(sample_event, None)