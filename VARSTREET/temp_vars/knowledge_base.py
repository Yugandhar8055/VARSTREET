"""Hardcoded knowledge base entries."""

KNOWLEDGE_BASE = {
  "CustomerScreen": {
    "advancedFilter": [
      {
        "label"    : "Company Name",
        "fieldtype": "PICKLIST",
        "fieldName": "customerId",
        "valueType": "STRING"
      },
      {
        "label": "Status",
        "fieldName": "isActive",
        "data": [
          {"text": "Active",   "value": 1},
          {"text": "Inactive", "value": 0}
        ],
        "fieldtype": "PICKLIST",
        "valueType": "NUMBER",
        "enableSearch": True
      },
      {
        "label"    : "Contacts",
        "fieldtype": "NUMBER",
        "fieldName": "contactCount",
        "valueType": "NUMBER",
        "format"   : "NUMERIC"
      },
      {
        "label"    : "Default Billing Address",
        "fieldtype": "TEXT",
        "fieldName": "defaultBillingAddress",
        "valueType": "STRING"
      },
      {
        "label"    : "Default Shipping Address",
        "fieldtype": "TEXT",
        "fieldName": "defaultShippingAddress",
        "valueType": "STRING"
      },
      {
        "label"    : "Phone Number",
        "fieldtype": "TEXT",
        "fieldName": "phoneNumber",
        "valueType": "STRING"
      },
      {
        "label"    : "Fax Number",
        "fieldtype": "TEXT",
        "fieldName": "workFax",
        "valueType": "STRING"
      },
      {
        "label"    : "CRM Reference Number",
        "fieldtype": "TEXT",
        "fieldName": "crmId",
        "valueType": "STRING"
      },
      {
        "label"    : "ERP Reference Number",
        "fieldtype": "TEXT",
        "fieldName": "erpId",
        "valueType": "STRING"
      },
      {
        "label"    : "E-Procurement Reference Number",
        "fieldtype": "TEXT",
        "fieldName": "eprocId",
        "valueType": "STRING"
      },
      {
        "label"    : "Dell Punchout Profile ID",
        "fieldtype": "TEXT",
        "fieldName": "punchoutAccNo",
        "valueType": "STRING"
      },
      {
        "label"    : "Type",
        "fieldtype": "PICKLIST",
        "fieldName": "customerType",
        "valueType": "STRING"
      },
      {
        "label"    : "Account No",
        "fieldtype": "TEXT",
        "fieldName": "accountNumber",
        "valueType": "STRING"
      },
      {
        "label"    : "Price List",
        "fieldtype": "PICKLIST",
        "fieldName": "priceListId",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Catalog",
        "fieldtype": "PICKLIST",
        "fieldName": "catalugeListId",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Sales Person",
        "fieldtype": "PICKLIST",
        "fieldName": "memberId",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Store",
        "fieldtype": "PICKLIST",
        "fieldName": "storeId",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Landing Page",
        "fieldtype": "PICKLIST",
        "fieldName": "landingPage",
        "valueType": "STRING"
      },
      {
        "label"    : "Default Payment Method",
        "fieldtype": "PICKLIST",
        "fieldName": "paymentMethod",
        "valueType": "STRING"
      },
      {
        "label"      : "Default Shipping Method",
        "fieldtype"  : "PICKLIST",
        "fieldName"  : "shippingMethodName",
        "dataItemKey": "text",
        "valueType"  : "STRING"
      },
      {
        "label"    : "Payment Term",
        "fieldtype": "TEXT",
        "fieldName": "paymentTerm",
        "valueType": "STRING"
      },
      {
        "label"    : "Bill Address Tax (%)",
        "fieldtype": "NUMBER",
        "fieldName": "billTax",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Ship Address Tax (%)",
        "fieldtype": "NUMBER",
        "fieldName": "shipTax",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Tax (%)",
        "fieldtype": "NUMBER",
        "fieldName": "taxPercentage",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Bill Address VAT (%)",
        "fieldtype": "NUMBER",
        "fieldName": "billTax",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Ship Address VAT (%)",
        "fieldtype": "NUMBER",
        "fieldName": "shipTax",
        "valueType": "NUMBER"
      },
      {
        "label"    : "VAT (%)",
        "fieldtype": "NUMBER",
        "fieldName": "taxPercentage",
        "valueType": "NUMBER"
      },
      {
        "label": "Bill Address Tax Exempt",
        "data": [
          {"text": "Yes", "value": "Y"},
          {"text": "No",  "value": "N"}
        ],
        "fieldtype": "PICKLIST",
        "initialFieldType": "CHECK BOX",
        "fieldName": "isTaxExemptUSBill",
        "valueType": "STRING"
      },
      {
        "label": "Ship Address Tax Exempt",
        "data": [
          {"text": "Yes", "value": "Y"},
          {"text": "No",  "value": "N"}
        ],
        "fieldtype": "PICKLIST",
        "fieldName": "isTaxExemptUSShip",
        "valueType": "STRING"
      },
      {
        "label": "Bill Address VAT Exempt",
        "data": [
          {"text": "Yes", "value": "Y"},
          {"text": "No",  "value": "N"}
        ],
        "fieldtype": "PICKLIST",
        "fieldName": "isTaxExemptUSBill",
        "valueType": "STRING"
      },
      {
        "label": "Ship Address VAT Exempt",
        "data": [
          {"text": "Yes", "value": "Y"},
          {"text": "No",  "value": "N"}
        ],
        "fieldtype": "PICKLIST",
        "fieldName": "isTaxExemptUSShip",
        "valueType": "STRING"
      },
      {
        "label": "VAT Exempt",
        "data": [
          {"text": "Yes", "value": "Y"},
          {"text": "No",  "value": "N"}
        ],
        "fieldtype": "PICKLIST",
        "fieldName": "isTaxExemptUS",
        "valueType": "STRING"
      },
      {
        "label": "Tax Exempt",
        "data": [
          {"text": "Yes", "value": "Y"},
          {"text": "No",  "value": "N"}
        ],
        "fieldtype": "PICKLIST",
        "initialFieldType": "CHECK BOX",
        "fieldName": "isTaxExemptUS",
        "valueType": "STRING"
      },
      {
        "label": "Tax Exempt",
        "data": [
          {"text": "GST only",             "value": "GST"   },
          {"text": "PST|QST only",         "value": "PST"   },
          {"text": "GST and PST|QST both", "value": "GSTPST"},
          {"text": "HST only",             "value": "HST"   }
        ],
        "fieldtype": "PICKLIST",
        "fieldName": "isTaxExemptCA",
        "valueType": "STRING"
      },
      {
        "label"    : "Special Pricing Available",
        "fieldtype": "PICKLIST",
        "fieldName": "specialDistributer",
        "valueType": "STRING"
      },
      {
        "label"    : "Contracts",
        "fieldtype": "PICKLIST",
        "fieldName": "selectedContracts",
        "valueType": "STRING"
      },
      {
        "label"    : "Parent Company",
        "fieldtype": "TEXT",
        "fieldName": "parentCompanyName",
        "valueType": "STRING"
      },
      {
        "label"    : "D-U-N-S Number",
        "fieldtype": "TEXT",
        "fieldName": "dunsNumner",
        "valueType": "STRING"
      },
      {
        "label"    : "SIC Code",
        "fieldtype": "TEXT",
        "fieldName": "sicCode",
        "valueType": "STRING"
      },
      {
        "label"    : "Rating",
        "fieldtype": "TEXT",
        "fieldName": "rating",
        "valueType": "STRING"
      },
      {
        "label"    : "Lead Source",
        "fieldtype": "TEXT",
        "fieldName": "leadSource",
        "valueType": "STRING"
      },
      {
        "label"    : "Annual Revenue",
        "fieldtype": "TEXT",
        "fieldName": "annualRevenue",
        "valueType": "STRING"
      },
      {
        "label"    : "Credit Rating",
        "fieldtype": "TEXT",
        "fieldName": "creditRating",
        "valueType": "STRING"
      },
      {
        "label"    : "Threshold Margin (%)",
        "fieldtype": "NUMBER",
        "fieldName": "thrasHoldMargin",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Credit Balance",
        "fieldtype": "NUMBER",
        "fieldName": "creditBalance",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Credit Limit",
        "fieldtype": "NUMBER",
        "fieldName": "creditLimit",
        "valueType": "NUMBER"
      },
      {
        "label": "Credit Hold",
        "data": [ {"text": "Yes", "value": 1}, {"text": "No", "value": 0} ],
        "fieldtype": "PICKLIST",
        "fieldName": "isCreditOnHeld",
        "valueType": "STRING"
      },
      {
        "label": "Drop Ship",
        "data": [
          {"text": "Yes", "value": "Y"},
          {"text": "No",  "value": "N"}
        ],
        "fieldtype": "PICKLIST",
        "fieldName": "isDropShip",
        "valueType": "STRING"
      },
      {
        "label"    : "Entered By",
        "fieldtype": "PICKLIST",
        "fieldName": "createdById",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Registration Date",
        "fieldtype": "DATE",
        "fieldName": "enteredOn",
        "valueType": "DATE"
      },
      {
        "label"    : "Modified On",
        "fieldtype": "DATE",
        "fieldName": "lastUpdatedOn",
        "valueType": "DATE"
      },
      {
        "label"    : "Modified By",
        "fieldtype": "PICKLIST",
        "fieldName": "updatedById",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Remarks",
        "fieldtype": "TEXT",
        "fieldName": "remarks",
        "valueType": "STRING"
      }
    ]
  },
  "SalesOrderScreen": {
    "advancedFilter": [
      {
        "label"    : "Number Prefix",
        "fieldtype": "TEXT",
        "fieldName": "A.AdvancedDocumentPrefix ",
        "valueType": "STRING"
      },
      {
        "label"    : "Number",
        "fieldtype": "NUMBER",
        "fieldName": "A.AdvancedDocumentNo",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Amount",
        "fieldtype": "NUMBER",
        "fieldName": "A.documentAmountAdvancedSearch",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Date",
        "fieldtype": "DATE",
        "fieldName": "A.DocumentDate",
        "valueType": "DATE"
      },
      {
        "label"    : "Customer",
        "fieldtype": "PICKLIST",
        "fieldName": "A.customerid",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Contact",
        "fieldtype": "PICKLIST",
        "fieldName": "A.contactid",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Sales Person",
        "fieldtype": "PICKLIST",
        "fieldName": "A.memberid",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Status",
        "fieldtype": "PICKLIST",
        "fieldName": "A.displaydocumentstatus",
        "valueType": "STRING"
      },
      {
        "label"    : "My Status",
        "fieldtype": "PICKLIST",
        "fieldName": "A.customertxnstatus",
        "valueType": "STRING"
      },
      {
        "label"    : "Title",
        "fieldtype": "TEXT",
        "fieldName": "A.documenttitle",
        "valueType": "STRING"
      },
      {
        "label"    : "Store",
        "fieldtype": "PICKLIST",
        "fieldName": "A.STOREID",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Default Payment Method",
        "fieldtype": "PICKLIST",
        "fieldName": "A.paymentmethodid",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Customer Comments",
        "fieldtype": "TEXT",
        "fieldName": "A.comments",
        "valueType": "STRING"
      },
      {
        "label"    : "Default Shipping Method",
        "fieldtype": "PICKLIST",
        "fieldName": "A.shipmediaid",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Delivery Note",
        "fieldtype": "TEXT",
        "fieldName": "A.deliverycomments",
        "valueType": "STRING"
      },
      {
        "label"    : "Entered On",
        "fieldtype": "DATE",
        "fieldName": "A.AdvancedEnteredOn",
        "valueType": "DATE"
      },
      {
        "label"    : "Entered By",
        "fieldtype": "PICKLIST",
        "fieldName": "A.enteredbyid",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Modified On",
        "fieldtype": "DATE",
        "fieldName": "A.AdvancedLastupdatetime",
        "valueType": "DATE"
      },
      {
        "label"    : "Modified By",
        "fieldtype": "PICKLIST",
        "fieldName": "A.lastupdatedbyid",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Attach Needed",
        "fieldtype": "PICKLIST",
        "fieldName": "A.SMARTNET",
        "valueType": "STRING"
      },
      {
        "label"    : "Terms & Conditions",
        "fieldtype": "TEXT",
        "fieldName": "A.terms",
        "valueType": "STRING"
      },
      {
        "label"    : "Contract",
        "fieldtype": "PICKLIST",
        "fieldName": "A.contractid",
        "valueType": "NUMBER"
      },
      {
        "label"    : "Customer PO",
        "fieldtype": "TEXT",
        "fieldName": "A.CustomerReference",
        "valueType": "STRING"
      },
      {
        "label"    : "Customer Type",
        "fieldtype": "PICKLIST",
        "fieldName": "A.customerType",
        "valueType": "STRING"
      },
      {
        "label"    : "End-User PO Number",
        "fieldtype": "TEXT",
        "fieldName": "A.CustomerReference2",
        "valueType": "STRING"
      },
      {
        "label"    : "Part#",
        "fieldtype": "TEXT",
        "fieldName": "DOCUMENTPART.MANUFACTURERPART",
        "valueType": "STRING"
      },
      {
        "label"    : "Part Description",
        "fieldtype": "TEXT",
        "fieldName": "DOCUMENTPART.PARTDESCRIPTION",
        "valueType": "STRING"
      },
      {
        "label"    : "CLIN#",
        "fieldtype": "TEXT",
        "fieldName": "DOCUMENTPART.CLINNO",
        "valueType": "STRING"
      },
      {
        "label"    : "Manufacturer",
        "fieldtype": "PICKLIST",
        "fieldName": "DOCUMENTPART.MANUFACTURERNAME",
        "valueType": "STRING"
      },
      {
        "label"    : "Distributor",
        "fieldtype": "PICKLIST",
        "fieldName": "DOCUMENTPART.DISTRIBUTORNAME",
        "valueType": "STRING"
      },
      {
        "label"    : "SKU",
        "fieldtype": "TEXT",
        "fieldName": "DOCUMENTPART.DISTRIBUTORSKU",
        "valueType": "STRING"
      },
      {
        "label"    : "Tax Code",
        "fieldtype": "TEXT",
        "fieldName": "DOCUMENTPART.TAXCODE",
        "valueType": "STRING"
      },
      {
        "label"    : "Tax Code",
        "fieldtype": "PICKLIST",
        "fieldName": "DOCUMENTPART.TAXCODE",
        "valueType": "STRING"
      },
      {
        "label"    : "UNSPSC",
        "fieldtype": "TEXT",
        "fieldName": "DOCUMENTPART.UNSPSCCODE",
        "valueType": "STRING"
      },
      {
        "label"    : "UPC",
        "fieldtype": "TEXT",
        "fieldName": "DOCUMENTPART.UPC",
        "valueType": "STRING"
      },
      {
        "label"    : "Price Unit Measure (UOM)",
        "fieldtype": "TEXT",
        "fieldName": "DOCUMENTPART.PRICEUNITMEASURE",
        "valueType": "STRING"
      },
      {
        "label"    : "Serialized Product",
        "fieldtype": "PICKLIST",
        "fieldName": "DOCUMENTPART.ISSERIALIZED",
        "valueType": "STRING"
      },
      {
        "label"    : "Instance Number",
        "fieldtype": "TEXT",
        "fieldName": "DOCUMENTPART.INSTANCENO",
        "valueType": "STRING"
      },
      {
        "label"    : "Line item serial number",
        "fieldtype": "TEXT",
        "fieldName": "DOCUMENTPART.SERIALNO",
        "valueType": "STRING"
      },
      {
        "label"    : "Subscription Term",
        "fieldtype": "TEXT",
        "fieldName": "DOCUMENTPART.SUBSCRIPTIONTERM",
        "valueType": "STRING"
      },
      {
        "label"    : "Hazardous Material",
        "fieldtype": "PICKLIST",
        "fieldName": "DOCUMENTPART.ISHAZARDOUS",
        "valueType": "STRING"
      },
      {
        "label"    : "Start Date",
        "fieldtype": "DATE",
        "fieldName": "DOCUMENTPART.EFFECTIVEFROM",
        "valueType": "DATE"
      },
      {
        "label"    : "End Date",
        "fieldtype": "DATE",
        "fieldName": "DOCUMENTPART.EFFECTIVETO",
        "valueType": "DATE"
      },
      {
        "label"    : "Tracking Number",
        "fieldtype": "TEXT",
        "fieldName": "TRACK.TRACKINGNO",
        "valueType": "STRING"
      },
      {
        "label"    : "Shipped Date",
        "fieldtype": "DATE",
        "fieldName": "TRACK.shipDate",
        "valueType": "DATE"
      },
      {
        "label"    : "Serial Number",
        "fieldtype": "TEXT",
        "fieldName": "TRACK.ITEMSRL",
        "valueType": "STRING"
      },
      {
        "label"    : "Estimated Ship Date",
        "fieldtype": "DATE",
        "fieldName": "TRACK.ESTSHIPDATE",
        "valueType": "DATE"
      },
      {
        "label"    : "Ship To Address",
        "fieldtype": "TEXT",
        "fieldName": "A.shippingaddress",
        "valueType": "STRING"
      },
      {
        "label"    : "External Invoice#",
        "fieldtype": "TEXT",
        "fieldName": "A.externalinvoiceno",
        "valueType": "STRING"
      }
    ]
  }
}
