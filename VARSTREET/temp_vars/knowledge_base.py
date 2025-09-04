filter_operators = {
  "TEXT": [
    { "filterOperator": "Equal", "value": "eq" },
    { "filterOperator": "Not Equal", "value": "neq" },
    { "filterOperator": "Includes", "value": "contains" },
    { "filterOperator": "Not Includes", "value": "doesnotcontain" }
  ],
  "PICKLIST": [
    { "filterOperator": "Equal", "value": "eq" },
    { "filterOperator": "Not Equal", "value": "neq" },
    { "filterOperator": "In The List", "value": "MULTISELECTFILTEROPERATOR" },
    { "filterOperator": "Not In The List", "value": "MULTISELECTFILTEROPERATORNOT" }
  ],
  "DATE or DATE_RANGE": [
    { "filterOperator": "Equal", "value": "eq" },
    { "filterOperator": "Not Equal", "value": "neq" },
    { "filterOperator": "Is Greater Than", "value": "gt" },
    { "filterOperator": "Is Less Than", "value": "lt" },
    { "filterOperator": "Is Greater Than Or Equal To", "value": "gte" },
    { "filterOperator": "Is Less Than Or Equal To", "value": "lte" },
    { "filterOperator": "In Between", "value": "RANGE" }
  ],
  "NUMBER or NUMBER_RANGE": [
    { "filterOperator": "Equal", "value": "eq" },
    { "filterOperator": "Not Equal", "value": "neq" },
    { "filterOperator": "Is Greater Than", "value": "gt" },
    { "filterOperator": "Is Less Than", "value": "lt" },
    { "filterOperator": "Is Greater Than Or Equal To", "value": "gte" },
    { "filterOperator": "Is Less Than Or Equal To", "value": "lte" },
    { "filterOperator": "In Between", "value": "NUMBER_RANGE" }
  ],
  "BOOLEAN": [
    { "filterOperator": "Equal", "value": "eq" }
  ]
}