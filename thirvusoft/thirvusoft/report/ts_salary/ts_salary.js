// Copyright (c) 2016, TS and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["TS_Salary"] = {
	"filters": [
		{
			fieldname: "role",
			label: __("Role"),
			fieldtype: "Select",
			options: [
				{ "value": "Developer", "label": __("Developer") },
				{ "value": "HR", "label": __("HR") },
				{ "value": "Trainee", "label": __("Trainee") },
				{ "value": "Designer", "label": __("Designer") }
			],
		},

	]
};
