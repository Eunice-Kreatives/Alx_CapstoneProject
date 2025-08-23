from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is not None:
        if response.status_code == 404 and 'detail' in response.data:
            if "Not found." in response.data['detail']:
                response.data['detail'] = "The requested resource could not be found."
        
        elif response.status_code == 403 and 'detail' in response.data:
             if "You do not have permission to perform this action." in response.data['detail']:
                 response.data['detail'] = "Access denied. You do not have the necessary permissions."

        
    else:
        print(f"Unhandled exception: {exc}")
        response = Response(
            {'detail': 'An unexpected server error occurred.'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response

