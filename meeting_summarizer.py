{
    "nodes": [
        {
            "parameters": {
                "operation": "getAll",
                "calendar": {
                    "__rl": true,
                    "value": "asusrid.info@gmail.com",
                    "mode": "list",
                    "cachedResultName": "asusrid.info@gmail.com"
                },
                "returnAll": true,
                "timeMin": "={{ $now.toUTC(60) }}",
                "timeMax": "={{ $now.set({ hour:23, minutes:59, seconds:59 }) }}",
                "options": {}
            },
            "type": "n8n-nodes-base.googleCalendar",
            "typeVersion": 1.3,
            "position": [
                220,
                160
            ],
            "id": "177b3fd0-76e6-43ab-bfd4-a538f86ea737",
            "name": "Google Calendar",
            "credentials": {
                "googleCalendarOAuth2Api": {
                  "id": "KSrBqUmAuBvjO5AW",
                  "name": "account"
                }
            }
        },
        {
            "parameters": {
                "operation": "formatDate",
                "date": "={{ $json.start.dateTime }}",
                "format": "yyyy-MM-dd",
                "options": {}
            },
            "type": "n8n-nodes-base.dateTime",
            "typeVersion": 2,
            "position": [
                440,
                160
            ],
            "id": "05743293-6f7e-4178-a738-754bf0bf8ec8",
            "name": "Date & Time"
        },
        {
            "parameters": {
                "assignments": {
                    "assignments": [
                        {
                            "id": "938b5484-a89d-45f9-b72f-f4f0d1bb0755",
                            "name": "summary",
                            "value": "={{ $('Google Calendar').item.json.summary }}",
                            "type": "string"
                        },
                        {
                            "id": "cbd75a6e-6296-47c4-bc76-72890d0e4431",
                            "name": "formattedDate",
                            "value": "={{ $json.formattedDate }}",
                            "type": "string"
                        },
                        {
                            "id": "a09fc54f-eacf-4d9c-a46f-768f466875ac",
                            "name": "description",
                            "value": "={{ $('Google Calendar').item.json.description }}",
                            "type": "string"
                        },
                        {
                            "id": "efd101eb-9439-4958-b66f-c19d267ceb09",
                            "name": "calendar_url",
                            "value": "={{ $('Google Calendar').item.json.htmlLink }}",
                            "type": "string"
                        }
                    ]
                },
                "options": {}
            },
            "type": "n8n-nodes-base.set",
            "typeVersion": 3.4,
            "position": [
                660,
                160
            ],
            "id": "b4cfa918-939c-42ad-b8a6-dd1d02af25ee",
            "name": "Edit Fields"
        },
        {
            "parameters": {
                "rule": {
                    "interval": [
                        {
                            "triggerAtHour": 8
                        }
                    ]
                }
            },
            "type": "n8n-nodes-base.scheduleTrigger",
            "typeVersion": 1.2,
            "position": [
                0,
                160
            ],
            "id": "f88ce6d3-1827-4832-9e6b-eed7ee4d2ffc",
            "name": "Schedule Trigger"
        },
        {
            "parameters": {
                "language": "python",
                "pythonCode": "# Loop over input items and add a new field called 'myNewField' to the JSON of each one\nmsg = \"\"  # Initialize msg variable outside the loop\nfor idx, item in enumerate(_input.all()):\n  if idx == 0:\n    # Format with emoji and HTML tags for Telegram\n    msg = f\"<b>📅 Meetings for: {item.json.formattedDate}</b>\\n\\n\"\n\n  msg += f\"<b>Title:</b> {item.json.summary}\\n\"\n  # Description with conditional check\n  msg += f\"<b>Description:</b>\\n{item.json.description if item.json.description else 'NO_DATA'}\\n\"\n  # Calendar URL with conditional check\n  msg += f\"<b>Calendar:</b>\\n{item.json.calendar_url if item.json.calendar_url else 'NO_DATA'}\\n\\n\"\n\n# Return the JSON structure with parse_mode for HTML formatting\nreturn [{\"json\": {\"msg\": msg, \"parse_mode\": \"HTML\"}}]"
            },
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [
                880,
                160
            ],
            "id": "2f1cc35c-680d-469d-9e7d-591c6577c0b8",
            "name": "Code"
        },
        {
            "parameters": {
                "chatId": "858152362",
                "text": "={{ $json.msg }}",
                "additionalFields": {
                    "appendAttribution": false,
                    "parse_mode": "HTML"
                }
            },
            "type": "n8n-nodes-base.telegram",
            "typeVersion": 1.2,
            "position": [
                1100,
                160
            ],
            "id": "b2d1f081-688a-4632-baed-b46b9d2a9901",
            "name": "Telegram",
            "webhookId": "c241dcde-f14a-49aa-bafa-4dd906c87326",
            "credentials": {
                "telegramApi": {
                    "id": "ki4AMeO8SdjOrh85",
                    "name": "account"
                }
            }
        }
    ],
    "connections": {
        "Google Calendar": {
            "main": [
                [
                    {
                        "node": "Date & Time",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "Date & Time": {
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
                        "node": "Code",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "Schedule Trigger": {
            "main": [
                [
                    {
                        "node": "Google Calendar",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "Code": {
            "main": [
                [
                    {
                        "node": "Telegram",
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
