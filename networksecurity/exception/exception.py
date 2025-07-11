# import sys
# from networksecurity.logging import logger

# class NetworkSecurityException(Exception):
#     def __init__(self, error_message,error_detail:sys):
#         self.error_message = error_message
#         _,_,exc_tb = error_detail.exc_info()

#         self.lineno = exc_tb.tb_lineno
#         self.file_name = exc_tb.tb_frame.f_code.co_filename


#     def __str__(self) :
#         return "Errror occured in python script name [{0}] line number [{1}] error message [{2}]".format(self.file_name,self.lineno,str(self.error_message))
    

# if __name__=='__main__':
#     try:
#         logger.logging.info("Enter the try block")
#         a = 1/0
#         print("this will not be printted",a)
#     except Exception as e:
#         raise NetworkSecurityException(e,sys)


import sys
import traceback
from networksecurity.logging import logger  # Optional if not used

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message

        _, _, exc_tb = error_detail
        if exc_tb:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = None
            self.file_name = None

    def __str__(self):
        return "Error occurred in Python script [{0}] at line [{1}]: {2}".format(
            self.file_name if self.file_name else "Unknown",
            self.lineno if self.lineno else "Unknown",
            str(self.error_message)
        )
