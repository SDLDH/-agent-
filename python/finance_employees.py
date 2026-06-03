def print_finance_employees(employees):
    """打印所有财务部员工的姓名和工资"""
    for emp in employees:
        if emp.get("dept") == "财务部":
            try:
                print(f"姓名: {emp['name']}, 工资: {emp['salary']}")
            except KeyError as e:
                print(f"警告：员工数据缺少字段 {e}，已跳过该员工")


if __name__ == "__main__":
    employees = [
        {"name": "张三", "salary": 8000, "dept": "财务部"},
        {"name": "李四", "salary": 9000, "dept": "技术部"},
        {"name": "王五", "salary": 8500, "dept": "财务部"},
        {"name": "赵六", "salary": 7000, "dept": "市场部"},
    ]
    print_finance_employees(employees)
