# print 1 to 100 numbers without using loops 

# def num(a):
#     if a>0 :
#         num (a-1)
#         print(a)

# num(100)        

# print 1 to 100 numbers with using loops   syntax:-(expression in itrable using loop)

# Z = (n for n in range(1,101) )
# print(list(Z))

# A_string = ("a")
# print(len(A_string))


# def num(a):
#     if a>0 :
#         num(a-1)
#         print(a)

# num(100)


z = [1,2,3,4,5,6,7,8,9,10]

l = list(map(lambda x:x*x,z))

print(l)


z = [1,2,3,4,5,6,7,8,9,10]

l = list(filter(lambda x:x %2==0,z))

print(l)


# question_id_list = [{"id":1},{"id":2},{"id":3},{"id":4}]

# topic_id_list = [
#     {"topic_id":6,"question_ref":1,"name":"Network","mapping_status":"Completed"},
#     {"topic_id":5,"question_ref":50,"name":"Network","mapping_status":"Completed"},
#     {"topic_id":4,"question_ref":1,"name":"Network","mapping_status":"Completed"},
#     {"topic_id":3,"question_ref":1,"name":"Network","mapping_status":"Completed"},
#     {"topic_id":6,"question_ref":2,"name":"Network","mapping_status":"Completed"},
#     {"topic_id":7,"question_ref":2,"name":"Scoping","mapping_status":"Not_started"},
#     {"topic_id":19,"question_ref":3,"name":"Configuration Management","mapping_status":"Not_started"},
#     {"topic_id":20,"question_ref":3,"name":"Configuration Management","mapping_status":"Not_started"},
#     {"topic_id":25,"question_ref":4,"name":"Data Encryption at rest","mapping_status":"Not_started"}
# ]

# mapped_data_list = [
#     {"id":15,"name":"CHANGE RECORD","topic_ref":6},
#     {"id":156,"name":"CHANGE RECORD","topic_ref":6}
# ]

# unmap_data_list = [
#     {"id":115,"name":"CHANGE RECORD","topic_ref":6},
#     {"id":123,"name":"CHANGE RECORD","topic_ref":3},
#     {"id":122,"name":"CHANGE RECORD","topic_ref":3},
#     {"id":121,"name":"CHANGE RECORD","topic_ref":2},
#     {"id":17,"name":"NW DIAGRAM","topic_ref":7},
#     {"id":31,"name":"VENDOR","topic_ref":19},
#     {"id":351,"name":"WIRELESS ENCRYPTION KEY CHANGE RECORD","topic_ref":19},
#     {"id":22,"name":"STD","topic_ref":20},
#     {"id":54,"name":"DATA DELETION PROCESS","topic_ref":25},
#     {"id":55,"name":"DATA MATRIX","topic_ref":25}
# ] 



question_id_list = [{"id":1},{"id":2},{"id":3},{"id":4}]

topic_id_list = [
    {"topic_id":6,"question_ref":2,"name":"Network","mapping_status":"Completed"},
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
            # print(mapped_items)
        
        unmapped_items = {item["id"]: item["name"] for item in unmap_data_list if item["topic_ref"] == topic_id}
        if mapped_items: 
            output["data"][str(question_id)][str(topic_id)]["unmap"] = unmapped_items
        
print(output)

       














# question_id_list = [{"id":1},{"id":2},{"id":3},{"id":4}]

# topic_id_list = [
#     {"topic_id":6,"question_ref":2,"name":"Network","mapping_status":"Completed"},
#     {"topic_id":7,"question_ref":2,"name":"Scoping","mapping_status":"Not_started"},
#     {"topic_id":19,"question_ref":3,"name":"Configuration Management","mapping_status":"Not_started"},
#     {"topic_id":20,"question_ref":3,"name":"Configuration Management","mapping_status":"Not_started"},
#     {"topic_id":25,"question_ref":4,"name":"Data Encryption at rest","mapping_status":"Not_started"}
# ]

# mapped_data_list = [
#     {"id":15,"name":"CHANGE RECORD","topic_ref":6}
# ]

# unmap_data_list = [
#     {"id":17,"name":"NW DIAGRAM","topic_ref":7},
#     {"id":31,"name":"VENDOR","topic_ref":19},
#     {"id":351,"name":"WIRELESS ENCRYPTION KEY CHANGE RECORD","topic_ref":19},
#     {"id":22,"name":"STD","topic_ref":20},
#     {"id":54,"name":"DATA DELETION PROCESS","topic_ref":25},
#     {"id":55,"name":"DATA MATRIX","topic_ref":25}
# ]

# output = {
#     "status":"success",
#     "message":"Document data fetch successfully",
#     "data": {}
# }



















