{
    "nodes": [
        {
            "parameters": {},
            "id": "b8d6e50f-3c92-4124-bc73-5099405a92eb",
            "name": "No operation",
            "type": "n8n-nodes-base.noOp",
            "typeVersion": 1,
            "position": [
                -300,
                440
            ]
        },
        {
            "parameters": {
                "url": "=https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={{ $('Wait 12 second').item.json.property_ticker }}&apikey={{ $json.API_KEY }}",
                "options": {}
            },
            "id": "1e889c59-163f-48f2-bd93-64c364795eee",
            "name": "Quote endpoint [VANTAGE ALPHA]",
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.1,
            "position": [
                120,
                80
            ]
        },
        {
            "parameters": {
                "rule": {
                    "interval": [
                        {}
                    ]
                }
            },
            "id": "934aae1a-cf51-464c-a66d-0d6aebf49677",
            "name": "Schedule trigger",
            "type": "n8n-nodes-base.scheduleTrigger",
            "typeVersion": 1.1,
            "position": [
                -1040,
                300
            ]
        },
        {
            "parameters": {
                "amount": 12,
                "unit": "seconds"
            },
            "id": "d1d483bd-1632-41ed-a5f4-5f2ac2651864",
            "name": "Wait 12 second",
            "type": "n8n-nodes-base.wait",
            "typeVersion": 1,
            "position": [
                -300,
                80
            ],
            "webhookId": "2f1d1415-8666-4564-be5f-da72eadd3dc8"
        },
        {
            "parameters": {
                "assignments": {
                    "assignments": [
                        {
                            "id": "35336fe3-5615-472f-8926-c93cd989826c",
                            "name": "API_KEY",
                            "value": "NH6E2O5BN4HNPRFN",
                            "type": "string"
                        }
                    ]
                },
                "options": {}
            },
            "type": "n8n-nodes-base.set",
            "typeVersion": 3.4,
            "position": [
                -100,
                80
            ],
            "id": "50e63201-5374-4d0f-8cb7-2190ff56768a",
            "name": "Edit Fields"
        },
        {
            "parameters": {
                "options": {}
            },
            "type": "n8n-nodes-base.splitInBatches",
            "typeVersion": 3,
            "position": [
                -560,
                300
            ],
            "id": "5b4f1992-44fa-440f-a835-09baba94e489",
            "name": "Loop Over Items"
        },
        {
            "parameters": {
                "resource": "databasePage",
                "operation": "getAll",
                "databaseId": {
                    "__rl": true,
                    "value": "1cce3634-db0f-80e6-91c2-f0b6bea6d83a",
                    "mode": "list",
                    "cachedResultName": "Stocks",
                    "cachedResultUrl": "https://www.notion.so/1cce3634db0f80e691c2f0b6bea6d83a"
                },
                "returnAll": true,
                "options": {}
            },
            "id": "3c881a6d-f9f2-47e2-8e02-aefa6c64842e",
            "name": "get_tickers",
            "type": "n8n-nodes-base.notion",
            "typeVersion": 2,
            "position": [
                -820,
                300
            ],
            "credentials": {
                "notionApi": {
                    "id": "L6ROGuxRBqWMdJpU",
                    "name": "Notion account"
                }
            }
        },
        {
            "parameters": {
                "resource": "databasePage",
                "operation": "update",
                "pageId": {
                    "__rl": true,
                    "value": "={{ $('get_tickers').item.json.id }}",
                    "mode": "id",
                    "__regex": "^([0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12})"
                },
                "propertiesUi": {
                    "propertyValues": [
                        {
                            "key": "Price|number",
                            "numberValue": "={{ Number($json['Global Quote']['05. price']) }}"
                        },
                        {
                            "key": "Extracted Date|date",
                            "includeTime": false,
                            "date": "={{ $json['Global Quote']['07. latest trading day'] }}",
                            "timezone": "America/New_York"
                        }
                    ]
                },
                "options": {}
            },
            "id": "b48a4713-0c07-49ef-8d48-30058e14feb7",
            "name": "update_rows",
            "type": "n8n-nodes-base.notion",
            "typeVersion": 2,
            "position": [
                320,
                80
            ],
            "credentials": {
                "notionApi": {
                    "id": "L6ROGuxRBqWMdJpU",
                    "name": "Notion account"
                }
            }
        },
        {
            "parameters": {
                "content": "## Llamada a la API\n### 1. Tenéis que crearos una cuenta aquí: https://www.alphavantage.co/\n### 2. Posteriormente, la clave secreta introducirla en la variable API_KEY",
                "height": 340,
                "width": 880
            },
            "type": "n8n-nodes-base.stickyNote",
            "position": [
                -380,
                -60
            ],
            "typeVersion": 1,
            "id": "c35ec301-10d1-4fd6-afb8-7ca61b8ccdcc",
            "name": "Sticky Note"
        },
        {
            "parameters": {
                "content": "## Obtener tickers de BBDD de Notions\n### 1. Crearos una integración en Notions para poder conectar n8n con Notions aquí: https://www.notion.so/profile/integrations/",
                "height": 340,
                "width": 460,
                "color": 3
            },
            "type": "n8n-nodes-base.stickyNote",
            "position": [
                -1120,
                140
            ],
            "typeVersion": 1,
            "id": "47a0bd81-7824-4ab6-9ba2-b5ede6e470c6",
            "name": "Sticky Note1"
        }
    ],
    "connections": {
        "Quote endpoint [VANTAGE ALPHA]": {
            "main": [
                [
                    {
                        "node": "update_rows",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "Schedule trigger": {
            "main": [
                [
                    {
                        "node": "get_tickers",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "Wait 12 second": {
            "main": [
                [
                    {
                        "node": "Edit Fields",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "Edit Fields": {
            "main": [
                [
                    {
                        "node": "Quote endpoint [VANTAGE ALPHA]",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "Loop Over Items": {
            "main": [
                [
                    {
                        "node": "No operation",
                        "type": "main",
                        "index": 0
                    }
                ],
                [
                    {
                        "node": "Wait 12 second",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "get_tickers": {
            "main": [
                [
                    {
                        "node": "Loop Over Items",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "update_rows": {
            "main": [
                [
                    {
                        "node": "Loop Over Items",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        }
    },
    "pinData": {},
    "meta": {
        "templateCredsSetupCompleted": true,
        "instanceId": "efaeb8c37ba2c2ae6d0671cdf19aac23ba8f6ef04cd9713239df6825b47a0c92"
    }
}
