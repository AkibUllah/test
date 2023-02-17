from flask import Flask, request
from error_codes import ERROR_CODE
import os.path
import json

app = Flask(__name__)



@app.route('/user_details',methods = ['POST', 'GET'])
def user_details():
   if request.method == 'POST':
       error_dict, error_found = {}, False
       if type(request.json["address"]) != str:
           error_dict["address"] = "Address Must Be String"
           error_found = True
       if type(request.json["ageInYears"]) != int:
           error_dict["ageInYears"] = "Age In Years Must Be Integer"
           error_found = True
       if type(request.json["creditScore"]) != float:
           error_dict["creditScore"] = "Credit Score Must Be Float"
           error_found = True
       if type(request.json["firstName"]) != str:
           error_dict["firstName"] = "First Name Must Be String"
           error_found = True
       if type(request.json["secondName"]) != str:
           error_dict["secondName"] = "Second Name Must Be String"
           error_found = True
       if error_found:
           return ERROR_CODE.http_codes.prepare_error_response(error_dict), 400

       address = request.json["address"]
       age_in_years = request.json["ageInYears"]
       credit_score = request.json["creditScore"]
       first_name = request.json["firstName"]
       second_name = request.json["secondName"]

       if address == '':
           error_dict["address"] = "Missing Data In Address"
           return ERROR_CODE.http_codes.prepare_error_response(error_dict), 400
       if age_in_years == '':
           error_dict["ageInYears"] = "Missing Age In Years"
           return ERROR_CODE.http_codes.prepare_error_response(error_dict), 400
       if credit_score == '':
           error_dict["creditScore"] = "Missing Data In Credit Score"
           return ERROR_CODE.http_codes.prepare_error_response(error_dict), 400
       if first_name == '':
           error_dict["firstName"] = "Missing Data In First Name"
           return ERROR_CODE.http_codes.prepare_error_response(error_dict), 400
       if second_name == '':
           error_dict["secondName"] = "Missing Data In Second Name"
           return ERROR_CODE.http_codes.prepare_error_response(error_dict), 400


       user_data = request.json
       with open('configuration-file.json', 'w', encoding='utf-8') as f:
           json.dump(user_data, f, indent=2)
           return ERROR_CODE.http_codes.prepare_success_response(user_data), 200

   else:
       try:
           with open('configuration-file.json', 'r') as json_file:
              if json_file:
                  user_data = json.load(json_file)
                  return ERROR_CODE.http_codes.get_prepare_success_response(user_data), 200
              else:
                  message = "Data Not Found"
                  return ERROR_CODE.http_codes.get_prepare_error_response(message), 404
       except Exception as e:
           return ERROR_CODE.http_codes.get_prepare_error_response(str(e)), 404


if __name__ == '__main__':
   app.run(debug = True)
