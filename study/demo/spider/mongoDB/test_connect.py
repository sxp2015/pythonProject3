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

"""
功能操作符号

以下是 MongoDB 中常见的所有聚合管道（aggregation pipeline）操作符号，以及它们的作用：

1. **$project** — 用于将文档中的一个或多个字段投射到输出文档中或从输出文档中删除某些字段。

2. **$match** — 对输入文档进行筛选，只输出符合条件的文档。

3. **$limit** — 对输入文档进行分页，只输出前n条文档。

4. **$skip** — 对输入文档进行分页，跳过前n条文档并输出剩下的文档。

5. **$sort** — 对输入文档进行排序并输出。

6. **$group** — 将集合中的文档分组，可用于统计结果等。

7. **$lookup** — 左连接其他集合中的文档，并将这些文档添加到输出文档中。

8. **$unwind** — 将数组类型的字段拆分成多个文档。

9. **$out** — 将聚合结果输出到新集合中。

10. **$redact** — 控制文档的访问级别，用于数据安全等场景。

11. **$count** — 统计满足条件的文档数，并将其输出到下一个阶段。

12. **$addFields** — 将新字段添加到输出文档中。

13. **$replaceRoot** — 用指定字段的值替换整个文档，常用于将内嵌文档“拉平”为顶层文档。

14. **$bucket** — 将输入文档分组到固定数量的桶（buckets）中，通常用于数据分析和可视化。

15. **$facet** — 在同一个输入文档集合上执行多个聚合操作，并将每个结果作为一组文档输出。

16. **$graphLookup** — 通过递归查找连接到集合的其他文档来查询关系型数据，常用于构建社交网络、地理信息系统等应用。

17. **$regex** - 用于在聚合时对文档中指定字段进行正则匹配。它支持多种正则表达式语法，可以实现高度灵活的文本匹配操作。

18. **$exists** - 用于过滤出某个字段存在或不存在的文档。通过指定布尔值参数来判断是否存在该字段。

19. **$type** - 用于选择指定类型的字段。MongoDB支持多种数据类型，如字符串、整数、日期等，该操作符可以帮助我们快速筛选指定类型的数据。

20. **$mod** - 用于判断数值型字段是否能被指定的除数整除。该操作符接收两个参数，第一个是除数，第二个是余数。

21. **$text** - 用于全文搜索，可以搜索指定文本是否存在于指定字段中。需要注意的是，使用该操作符需要先创建全文索引（text index）。

22. **$where** - 用于执行 JavaScript 表达式。它可以访问当前文档中所有的字段，在 JavaScript 中进行诸如比较、计算等操作，并返回一个布尔值表示当前文档是否符合要求。

这些操作符号同样也是 MongoDB 聚合管道 (Aggregation Pipeline) 的一部分，可以用于处理和转换文档数据。需要注意的是不同操作符号的用法和效果不同，需要根据实际情况灵活应用。

以上是 MongoDB 中常见的所有聚合管道（aggregation pipeline）操作符号。这些操作符号可以结合使用，来完成各种聚合计算、数据转换和处理等任务。

"""