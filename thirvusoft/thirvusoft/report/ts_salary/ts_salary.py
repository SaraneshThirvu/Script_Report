# Copyright (c) 2013, TS and contributors
# For license information, please see license.txt

import frappe
from frappe import _

from erpnext.accounts.utils import get_balance_on


def execute(filters=None):
	filters = frappe._dict(filters or {})
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters):
	columns = [
		{
			"label": "Emp ID",
			"fieldtype": "Data",
			"fieldname": "emp_id",
			"width": 100
		},
		{
			"label": "Emp Name",
			"fieldtype": "Data",
			"fieldname": "emp_name",
			"width": 100
		},
		{
			"label": "Role",
			"fieldtype": "Select",
			"fieldname": "role",
			"options": [
				{ "value": "Developer", "label":("Developer") },
				{ "value": "HR", "label":"HR" },
				{ "value": "Trainee", "label":("Trainee") },
				{ "value": "Designer", "label":("Designer") }
			],
			"width": 100
		}
	]

	return columns

def get_conditions(filters):
	conditions = {}

	if filters.role:
		conditions["role"] = filters.role
		return conditions
	return conditions

def get_data(filters):

	data = []
	conditions = get_conditions(filters)
	accounts = frappe.db.get_all("TS_Payroll", fields=["emp_id", "emp_name","role"],
		filters=conditions, order_by='emp_name')

	for d in accounts:
		row = {"emp_id": d.emp_id, "emp_name": d.emp_name, "role": d.role}

		data.append(row)

	return data
