
import requests
import json

class GetPrograms:

  def get_programs(self):
    try:
      URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
      response=requests.get(URL)
      
      return response.content
    except Exception as e:
      print("we got this error", str(e))

  def program_school(self):
    program_list=[]
    programs=json.loads(self.get_programs())
    for program in programs:
      program_list.append(program["agency"])
    return program_list


intance =GetPrograms()
# print(intance.get_programs())
programs_school =intance.program_school()
for school in set(programs_school):
  print(school)