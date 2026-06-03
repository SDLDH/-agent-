def qaz(wsx):
    for i in wsx:
        if i["dept"] == "财务部":
            print(f"姓名: {i['name']}, 工资: {i['salary']}")
edc = [{"name": "张三", "dept": "财务部", "salary": 2000},
                   {"name": "李四", "dept": "人事部", "salary": 3000}]
qaz(edc)