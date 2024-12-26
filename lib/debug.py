#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb


Department.drop_table()
Department.create_table()

payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)

payroll.save()
print(payroll)

hr = Department.create("Human Resources", "Building C, 3rd Floor")
print(hr)


hr.name = "Human Resources"
hr.location = "Building C, 3rd Floor"
hr.update()
print(hr)



print("Delete payroll")
payroll.delete()
print(payroll)

hr.save()
print(hr)





ipdb.set_trace()
