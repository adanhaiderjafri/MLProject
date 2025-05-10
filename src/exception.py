import sys
import logging

def error_message_detail(error, error_detail: sys):
    """
    This function returns a detailed error message.
    Args:
        error: The error object
        error_detail: The error detail object
    Returns:
        A string containing the error message
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = "Error occurred in script: [{0}] at line number: [{1}] error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    """
    Custom exception class to handle exceptions in the project.
    Args:
        error_message: The error message
        error_detail: The error detail object
    """
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message_detail(error_message, error_detail)
        super().__init__(self.error_message)
    
    def __str__(self):
        return self.error_message
    
