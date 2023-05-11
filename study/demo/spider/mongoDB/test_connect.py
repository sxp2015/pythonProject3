import pymongo

# 这个方法也可以
client1 = pymongo.MongoClient('mongodb://localhost:27017/')
# client2 = pymongo.MongoClient(host='localhost', port=27017)

db1 = client1['test']
# db2 = client2['test']

collection1 = db1['test']

student1 = {
    'id': 'A202305001',
    'name': 'apple',
    'age': 23,
    'gender': 'male'
}
student2 = {
    'id': 'A202305002',
    'name': 'banana',
    'age': 23,
    'gender': 'female'
}

documents = [
    {'id': '9101', 'name': 'Charlie', 'age': 20},
    {'id': '9102', 'name': 'David', 'age': 22},
    {'id': '9103', 'name': 'Eve', 'age': 24}
]

# 如果你打算插入重复值，那么你需要修改你的数据库设计，删除唯一索引，
# 或者在插入文档时使用 update_one() 而不是 insert_one()，通过设置 upsert 参数为 True
# 来避免唯一性冲突
# result1 = connection1.insert_one(student1) 只能插入一次
query = {'id': 'A202305004'}
# 使用 $gte 操作符来查找所有 age 大于或等于 18 的数据
query_gte_age = {'age': {'$gte': 18}}
# 使用 $lt 操作符来查找所有 age 小于或等于 18 的数据
query_lt_age = {'age': {'$lt': 18}}
# 使用 $set操作符 来更新数据
update = {'$set': {'name': 'Orange-1', 'age': 25}}

# 更新
result1 = collection1.update_one(query, update)
print(result1.modified_count, "数据更新了！")

# 查找
value1 = collection1.find_one(query)
value2s = collection1.find(query_gte_age)
value3s = collection1.find(query_lt_age)

print('找到数据：', value1)
for value in value2s:
    value_text = f' id = {value["id"]}, - name = {value["name"]} - age= {value["age"]}'
    print('找到数据大于18：', value_text)

for value in value3s:
    value_text2 = f' id = {value["id"]}, - name = {value["name"]} - age= {value["age"]}'
    print('找到数据小于18：', value_text2)

# 插入多条数据
result2 = collection1.insert_many(documents)
# 按要求查找并且排序 -1是降序 limit是分段几条
query_and_sort = collection1.find(query_gte_age).sort('age', -1).limit(10)
for query_item in query_and_sort:
    print('查找并排序的结果是：', query_item)


""""
在 MongoDB 中，用于比较查询的常用操作符有以下几个：

1. `$eq` - 匹配等于条件的文档
2. `$ne` - 匹配不等于条件的文档
3. `$gt` - 匹配大于条件的文档
4. `$gte` - 匹配大于等于条件的文档
5. `$lt` - 匹配小于条件的文档
6. `$lte` - 匹配小于等于条件的文档
7. `$in` - 匹配包含在指定数组中的值的文档
8. `$nin` - 匹配不包含在指定数组中的值的文档

这些操作符可以结合 `$and`、`$or` 和 `$not` 等逻辑操作符来进行复杂的查询。除此之外，还有一些字符串匹配、数组查询、类型查询等其他类型的操作符，可以满足更多的查询需求。
"""