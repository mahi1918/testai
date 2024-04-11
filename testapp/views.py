from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json,requests
import execute_tests as ebt

# Sample data for tests
tests = {"tests": [{"title": "Open google.com", "steps": ["Open Browser browser='chrome'", "Go To url='https://google.com'"]}]}

# View function to handle listing and adding tests
@csrf_exempt
def list_tests(request):
    # Handle GET request to list existing tests
    if request.method == "GET":
        return JsonResponse(tests, safe=False, status=200)
    # Handle POST request to add a new test
    elif request.method == "POST":
        # Get the request body containing the new test data
        test = request.body
        print(test)  # Print the request body (for debugging)
        print(type(test))  # Print the type of the request body (for debugging)

        # Convert the request body JSON string to a dictionary
        test_dict = json.loads(test)
        print(test_dict)  # Print the parsed dictionary (for debugging)
        print(type(test_dict))  # Print the type of the parsed dictionary (for debugging)

        # Append the new test dictionary to the tests list
        tests.append(test_dict)

        # Return a JSON response with the added test data
        return JsonResponse(test_dict, status=200)
    else:
        # Handle unsupported HTTP methods with a 404 response
        return HttpResponseNotFound("Sorry this method is not supported")


@csrf_exempt
def check_endpoint(request):
    response = requests.get('http://127.0.0.1:8000/testai/tests/v1/execute')
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        ebt.execute_robot_tests()
        # Return HttpResponse if successful
        return HttpResponse("Tests executed successfully") 
    else:
        # Handle unsuccessful request (optional)
        print("Failed to fetch data from API:", response.status_code)
        # Return HttpResponse if unsuccessful
        return HttpResponse("Failed to fetch data from API: {}".format(response.status_code))


        