"""

"""

question_id_list = [{"id":1},{"id":2},{"id":3},{"id":4}]

topic_id_list = [
    {"topic_id":6,"question_ref":2,"name":"Network","mapping_status":"Completed"},
    {"topic_id":10,"question_ref":4,"name":"Network","mapping_status":"Completed"},
    {"topic_id":9,"question_ref":3,"name":"Network","mapping_status":"Completed"},
    {"topic_id":7,"question_ref":2,"name":"Scoping","mapping_status":"Not_started"},
    {"topic_id":19,"question_ref":3,"name":"Configuration Management","mapping_status":"Not_started"},
    {"topic_id":20,"question_ref":3,"name":"Configuration Management","mapping_status":"Not_started"},
    {"topic_id":25,"question_ref":4,"name":"Data Encryption at rest","mapping_status":"Not_started"}
]

mapped_data_list = [
    {"id":15,"name":"CHANGE RECORD","topic_ref":6}
]

unmap_data_list = [
    {"id":17,"name":"NW DIAGRAM","topic_ref":7},
    {"id":34,"name":"NW DIAGRAM","topic_ref":8},
    {"id":347,"name":"NW DIAGRAM","topic_ref":8},
    {"id":31,"name":"VENDOR","topic_ref":19},
    {"id":351,"name":"WIRELESS ENCRYPTION KEY CHANGE RECORD","topic_ref":19},
    {"id":22,"name":"STD","topic_ref":20},
    {"id":54,"name":"DATA DELETION PROCESS","topic_ref":25},
    {"id":55,"name":"DATA MATRIX","topic_ref":25}
]

output = {
    "status":"success",
    "message":"Document data fetch successfully",
    "data": {}
}

for question in question_id_list:
    question_id = question["id"]  
    output["data"][str(question_id)] = {}

    related_topics = [topic for topic in topic_id_list if topic["question_ref"] == question_id]

    for topic in related_topics:
        topic_id = topic["topic_id"]  
    
        output["data"][str(question_id)][str(topic_id)] = {
            "mapping_status": topic["mapping_status"],
            "topic": topic["name"]
        }
        mapped_items = {item["id"]: item["name"] for item in mapped_data_list if item["topic_ref"] == topic_id}
        if mapped_items: 
            output["data"][str(question_id)][str(topic_id)]["map"] = mapped_items
        
        unmapped_items = {item["id"]: item["name"] for item in unmap_data_list if item["topic_ref"] == topic_id}
        if unmapped_items: 
            output["data"][str(question_id)][str(topic_id)]["unmap"] = unmapped_items
        
print(output)







# family = {
#     'grand_parent':{'Name':'dada','Age': 95},
#     'parent':{'Name':'son','Age': 50},
#     'child':{'Name':'sub_child','Age': 25},
# }    

# print(family)
# family['grand_parent']['Age'] = 100
# print(family['grand_parent']['Age']) 
# family
# print(family['child'])
# print(family['parent'])


# for k,v in family.items():
#     print(k,v['Name'],v['Age'])




# 1st Task 


# my_dict = input(""" Enter your dictionary: eg:-{101: 'Alice Smith', 102: 'Bob Johnson'}""")
# input = {
#   "company": {
#     "name": "Tech Innovators",
#     "location": "San Francisco",
#     "departments": [
#       {
#         "name": "Engineering",
#         "employees": [
#           {
#             "id": 101,
#             "name": "Alice Smith",
#             "role": "Software Engineer",
#             "skills": ["Python", "Django", "React"],
#             "contact": {
#               "email": "alice.smith@example.com",
#               "phone": "123-456-7890"
#             }
#           },
#           {
#             "id": 101,
#             "name": "Alice Smith",
#             "role": "Software Engineer",
#             "skills": ["Python", "Django", "React"],
#             "contact": {
#               "email": "alice.smith@example.com",
#               "phone": "123-456-7890"
#             }
#           },
#           {
#             "id": 102,
#             "name": "Bob Johnson",
#             "role": "DevOps Engineer",
#             "skills": ["AWS", "Docker", "Kubernetes"],
#             "contact": {
#               "email": "bob.johnson@example.com",
#               "phone": "987-654-3210"
#             }
#           }
#         ]
#       },
#       {
#         "name": "Marketing",
#         "employees": [
#           {
#             "id": 201,
#             "name": "Carol Taylor",
#             "role": "Marketing Manager",
#             "skills": ["SEO", "Content Strategy", "Analytics"],
#             "contact": {
#               "email": "carol.taylor@example.com",
#               "phone": "555-666-7777"
#             }
#           },
#           {
#             "id": 202,
#             "name": "Carol Taylor",
#             "role": "Marketing Manager",
#             "skills": ["SEO", "Content Strategy", "Analytics"],
#             "contact": {
#               "email": "carol.taylor@example.com",
#               "phone": "555-666-7777"
#             }
#           },
#           {
#             "id": 201,
#             "name": "Carol Taylor",
#             "role": "Marketing Manager",
#             "skills": ["SEO", "Content Strategy", "Analytics"],
#             "contact": {
#               "email": "carol.taylor@example.com",
#               "phone": "555-666-7777"
#             }
#           }
#         ]
#       }
#     ],
#     "established": 2010,
#     "isPublic": False
#   }
# }
# output = {}
# for department in input["company"]["departments"]:
#     for employee in department["employees"]:
#         output[employee["id"]] = employee["name"],employee["role"],employee["skills"],employee["contact"]
        
# print(output) 


# output = {}
# for department in input["company"]["departments"]:
#     for employee in department["employees"]:
#         output[employee["id"]] = employee["name"],employee["role"],employee["skills"],employee["contact"]
        
# print(output) 

