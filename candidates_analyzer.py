{
    "nodes": [
        {
            "parameters": {
                "operation": "pdf",
                "options": {}
            },
            "type": "n8n-nodes-base.extractFromFile",
            "typeVersion": 1,
            "position": [
                -2040,
                100
            ],
            "id": "6b8eba88-fe51-4a1a-9f6b-4658b2c6f401",
            "name": "Extract from File"
        },
        {
            "parameters": {
                "model": {
                    "__rl": true,
                    "mode": "list",
                    "value": "gpt-4o-mini"
                },
                "options": {}
            },
            "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
            "typeVersion": 1.2,
            "position": [
                -1260,
                460
            ],
            "id": "23606fbf-7d1e-4dbe-aa7d-b20a436d2213",
            "name": "OpenAI Chat Model",
            "credentials": {
                "openAiApi": {
                    "id": "itdQkm1FKULykRHF",
                    "name": "OpenAi account"
                }
            }
        },
        {
            "parameters": {
                "text": "={{ $json.text }}",
                "schemaType": "manual",
                "inputSchema": "{\n  \"type\": \"object\",\n  \"properties\": {\n    \"name\": {\n      \"type\": \"string\"\n    },\n    \"telephone\": {\n      \"type\": \"string\"\n    },\n    \"city\": {\n      \"type\": \"string\"\n    },\n    \"street\": {\n      \"type\": \"string\"\n    },\n    \"linkedin\": {\n      \"type\": \"string\"\n    },\n    \"email\": {\n      \"type\": \"string\"\n    },\n    \"birthdate\": {\n      \"type\": \"string\"\n    }\n  }\n}",
                "options": {
                    "systemPromptTemplate": "You are an expert extraction algorithm.\nOnly extract personal information from the text provided.\nIf you do not know the value of an attribute asked to extract, you may omit the attribute's value."
                }
            },
            "type": "@n8n/n8n-nodes-langchain.informationExtractor",
            "typeVersion": 1,
            "position": [
                -1780,
                100
            ],
            "id": "4c0391f8-ce1c-44c4-ae44-dbd1dec76f99",
            "name": "Personal data"
        },
        {
            "parameters": {
                "text": "={{ $json.text }}",
                "attributes": {
                    "attributes": [
                        {
                            "name": "Education",
                            "description": "Summary of your academic career. Focus on your high school and university studies. Summarize in 100 words maximum and also include your grade if applicable.",
                            "required": true
                        },
                        {
                            "name": "Experience",
                            "description": "Work history summary. Focus on your most recent work experiences. Summarize in 100 words maximum",
                            "required": true
                        },
                        {
                            "name": "Skills",
                            "description": "Extract the candidate’s technical skills. What software and frameworks they are proficient in. Make a bulleted list."
                        }
                    ]
                },
                "options": {
                    "systemPromptTemplate": "You are an expert extraction algorithm.\nOnly extract information related to the education background, job history and skills of this person from the text.\nIf you do not know the value of an attribute asked to extract, you may omit the attribute's value."
                }
            },
            "type": "@n8n/n8n-nodes-langchain.informationExtractor",
            "typeVersion": 1,
            "position": [
                -1780,
                280
            ],
            "id": "1dbbd044-f894-4f67-9408-d2ab38276459",
            "name": "Skills"
        },
        {
            "parameters": {
                "mode": "combine",
                "combineBy": "combineByPosition",
                "options": {}
            },
            "type": "n8n-nodes-base.merge",
            "typeVersion": 3,
            "position": [
                -1380,
                180
            ],
            "id": "6dfe0664-724a-4bbd-bc47-bfc68eb0aef1",
            "name": "Merge"
        },
        {
            "parameters": {
                "options": {
                    "summarizationMethodAndPrompts": {
                        "values": {
                            "combineMapPrompt": "=Write a concise summary of this professional profile of a candidate:\n\nCity: {{ $json.output.city }}\nBirthdate: {{ $json.output.birthdate }}\nEducational qualification: {{ $json.output.Education }}\nJob History: {{ $json.output.Experience }}\nSkills: {{ $json.output.Skills }}\n\nUse 100 words or less. Be concise and conversational.",
                            "prompt": "=Write a concise summary of the following:\n\nCity: {{ $json.output.city }}\nBirthdate: {{ $json.output.birthdate }}\nEducational qualification: {{ $json.output.Education }}\nJob History: {{ $json.output.Experience }}\nSkills: {{ $json.output.Skills }}\n\nUse 100 words or less. Be concise and conversational."
                        }
                    }
                }
            },
            "type": "@n8n/n8n-nodes-langchain.chainSummarization",
            "typeVersion": 2,
            "position": [
                -1180,
                180
            ],
            "id": "dd772b9e-3441-43a3-a7e5-59f7fc4a5fcf",
            "name": "Summarization Chain"
        },
        {
            "parameters": {
                "assignments": {
                    "assignments": [
                        {
                            "id": "b9c737ac-87e3-4a3d-b933-de52d9916e2a",
                            "name": "profile_wanted",
                            "value": "={{ $json.text }}",
                            "type": "string"
                        }
                    ]
                },
                "options": {}
            },
            "type": "n8n-nodes-base.set",
            "typeVersion": 3.4,
            "position": [
                -320,
                180
            ],
            "id": "2e86cc95-2b06-4390-af60-ce1b599f1ce4",
            "name": "Edit Fields"
        },
        {
            "parameters": {
                "promptType": "define",
                "text": "=Profile wanted:\n{{ $json.profile_wanted }}\n\nCandidate:\n{{ $('Summarization Chain').item.json.response.text }}\n",
                "hasOutputParser": true,
                "messages": {
                    "messageValues": [
                        {
                            "message": "Eres un experto en Recursos Humanos y debes reflexionar sobre si el candidato se alinea con el perfil que se busca en la empresa. Debes votar del 1 al 10 donde el 1 significa que el candidato no está alineado con el puesto de trabajo publicado, mientras que un 10 significa que el perfil es exactamente lo que se pide en el puesto. Por último, en el campo de \"consideraciones\", quiero que des una explicación de tu voto."
                        }
                    ]
                }
            },
            "type": "@n8n/n8n-nodes-langchain.chainLlm",
            "typeVersion": 1.5,
            "position": [
                -80,
                180
            ],
            "id": "11173a24-6e23-4287-beef-d4b047a46caf",
            "name": "Basic LLM Chain"
        },
        {
            "parameters": {
                "schemaType": "manual",
                "inputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"vote\": {\n\t\t\t\"type\": \"string\"\n\t\t},\n\t\t\"consideration\": {\n\t\t\t\"type\": \"string\"\n\t\t}\n\t}\n}"
            },
            "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
            "typeVersion": 1.2,
            "position": [
                80,
                360
            ],
            "id": "87e6f6c2-23bd-4f93-8ecf-644f7c0fc682",
            "name": "Structured Output Parser"
        },
        {
            "parameters": {
                "conditions": {
                    "options": {
                        "caseSensitive": true,
                        "leftValue": "",
                        "typeValidation": "strict",
                        "version": 2
                    },
                    "conditions": [
                        {
                            "id": "efb95815-7513-4331-b2f7-009f5da5d688",
                            "leftValue": "={{ Number($('Basic LLM Chain').item.json.output.vote) }}",
                            "rightValue": 6,
                            "operator": {
                                "type": "number",
                                "operation": "gt"
                            }
                        }
                    ],
                    "combinator": "and"
                },
                "options": {}
            },
            "type": "n8n-nodes-base.if",
            "typeVersion": 2.2,
            "position": [
                760,
                180
            ],
            "id": "5f75d773-98f6-4670-8235-f097d4444018",
            "name": "If"
        },
        {
            "parameters": {
                "chatId": "858152362",
                "text": "={{ $json.html }}",
                "additionalFields": {
                    "appendAttribution": false,
                    "parse_mode": "HTML"
                }
            },
            "type": "n8n-nodes-base.telegram",
            "typeVersion": 1.2,
            "position": [
                1240,
                80
            ],
            "id": "5d88700c-4ded-4696-9617-549ee8813922",
            "name": "Telegram",
            "webhookId": "de19bcdc-4025-456d-b75a-c3cf69453672",
            "credentials": {
                "telegramApi": {
                    "id": "08dztuPerc5ty2R4",
                    "name": "tlgm account candidates_analyzer"
                }
            }
        },
        {
            "parameters": {
                "jsCode": "const data = {\n  \"NAME\": $('add_candidate_info').first().json.NAME,\n  \"PHONE NUMBER\": $('add_candidate_info').first().json['PHONE NUMBER'],\n  \"CITY\": $('add_candidate_info').first().json.CITY,\n  \"EMAIL\": $('add_candidate_info').first().json.EMAIL,\n  \"LINKEDIN\": $('add_candidate_info').first().json.LINKEDIN,\n  \"CONSIDERATIONS\": $('add_candidate_info').first().json.CONSIDERATIONS\n};\n\n// Format the message\nconst htmlMessage = `\n<b>📋 Possible Candidate!!</b>\n\n<b>👤 Name:</b> ${data.NAME}\n<b>📍 City:</b> ${data.CITY}\n<b>📞 Phone:</b> ${data[\"PHONE NUMBER\"].replace(/\"/g, '')}\n<b>📧 Email:</b> ${data.EMAIL}\n<b>🔗 LinkedIn:</b> <a href=\"https://${data.LINKEDIN}\">${data.LINKEDIN}</a>\n\n<b>📝 Considerations:</b>\n${data.CONSIDERATIONS}\n`;\n\n// Return the message as output\nreturn [\n  {\n    json: {\n      html: htmlMessage\n    }\n  }\n];\n"
            },
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [
                1020,
                80
            ],
            "id": "2cfbbdd3-41ba-4b8a-a3a1-c2fd9dafc820",
            "name": "Code"
        },
        {
            "parameters": {
                "operation": "pdf",
                "options": {}
            },
            "type": "n8n-nodes-base.extractFromFile",
            "typeVersion": 1,
            "position": [
                -580,
                180
            ],
            "id": "aea15bfc-b2d3-4b83-8d7f-67f4e8290ba2",
            "name": "Extract from File1"
        },
        {
            "parameters": {
                "operation": "download",
                "fileId": {
                    "__rl": true,
                    "value": "={{ $json.id }}",
                    "mode": "id"
                },
                "options": {}
            },
            "type": "n8n-nodes-base.googleDrive",
            "typeVersion": 3,
            "position": [
                -2280,
                100
            ],
            "id": "8335416c-327e-4064-9c54-0067a4b5254f",
            "name": "download_candidate_cv",
            "credentials": {
                "googleDriveOAuth2Api": {
                    "id": "PGRgMM0fa2Bi77rT",
                    "name": "account"
                }
            }
        },
        {
            "parameters": {
                "operation": "download",
                "fileId": {
                    "__rl": true,
                    "value": "1AtSu4psqK52TLBlVm4C2hD3lmjN7nkkO",
                    "mode": "list",
                    "cachedResultName": "Puesto_ Software Engineer Full Stack (Mid-Senior Level).pdf",
                    "cachedResultUrl": "https://drive.google.com/file/d/1AtSu4psqK52TLBlVm4C2hD3lmjN7nkkO/view?usp=drivesdk"
                },
                "options": {}
            },
            "type": "n8n-nodes-base.googleDrive",
            "typeVersion": 3,
            "position": [
                -800,
                180
            ],
            "id": "5285e50a-632f-474e-9711-5723246676f9",
            "name": "download_job_post",
            "credentials": {
                "googleDriveOAuth2Api": {
                    "id": "PGRgMM0fa2Bi77rT",
                    "name": "account"
                }
            }
        },
        {
            "parameters": {
                "operation": "move",
                "fileId": {
                    "__rl": true,
                    "value": "={{ $('download_candidate_cv').item.json.id }}",
                    "mode": "id"
                },
                "driveId": {
                    "__rl": true,
                    "value": "My Drive",
                    "mode": "list",
                    "cachedResultName": "My Drive",
                    "cachedResultUrl": "https://drive.google.com/drive/my-drive"
                },
                "folderId": {
                    "__rl": true,
                    "value": "1rZwUT9LwVUbH-WIWLPJePLmw1PzsveQm",
                    "mode": "list",
                    "cachedResultName": "analyzed",
                    "cachedResultUrl": "https://drive.google.com/drive/folders/1rZwUT9LwVUbH-WIWLPJePLmw1PzsveQm"
                }
            },
            "type": "n8n-nodes-base.googleDrive",
            "typeVersion": 3,
            "position": [
                540,
                180
            ],
            "id": "23ae2d9e-fe8d-4f8b-98b9-063a21c2b8bd",
            "name": "move_cv_to_analyzed",
            "credentials": {
                "googleDriveOAuth2Api": {
                    "id": "PGRgMM0fa2Bi77rT",
                    "name": "account"
                }
            }
        },
        {
            "parameters": {
                "operation": "append",
                "documentId": {
                    "__rl": true,
                    "value": "1FmKumQcD3_RZgbZ_ljX4TrkAYnnVGG3KaXr2V5Vwv6k",
                    "mode": "id"
                },
                "sheetName": {
                    "__rl": true,
                    "value": "gid=0",
                    "mode": "list",
                    "cachedResultName": "summary",
                    "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1FmKumQcD3_RZgbZ_ljX4TrkAYnnVGG3KaXr2V5Vwv6k/edit#gid=0"
                },
                "columns": {
                    "mappingMode": "defineBelow",
                    "value": {
                        "CONSIDERATIONS": "={{ $json.output.consideration }}",
                        "VOTE ": "={{ $json.output.vote }}",
                        "NAME": "={{ $('Merge').item.json.output.name }}",
                        "PHONE NUMBER": "=\"{{ $('Merge').item.json.output.telephone }}\"",
                        "CITY": "={{ $('Merge').item.json.output.city }}",
                        "EMAIL": "={{ $('Merge').item.json.output.email }}",
                        "LINKEDIN": "={{ $('Merge').item.json.output.linkedin }}"
                    },
                    "matchingColumns": [],
                    "schema": [
                        {
                            "id": "NAME",
                            "displayName": "NAME",
                            "required": false,
                            "defaultMatch": false,
                            "display": true,
                            "type": "string",
                            "canBeUsedToMatch": true
                        },
                        {
                            "id": "EMAIL",
                            "displayName": "EMAIL",
                            "required": false,
                            "defaultMatch": false,
                            "display": true,
                            "type": "string",
                            "canBeUsedToMatch": true
                        },
                        {
                            "id": "LINKEDIN",
                            "displayName": "LINKEDIN",
                            "required": false,
                            "defaultMatch": false,
                            "display": true,
                            "type": "string",
                            "canBeUsedToMatch": true,
                            "removed": false
                        },
                        {
                            "id": "CITY",
                            "displayName": "CITY",
                            "required": false,
                            "defaultMatch": false,
                            "display": true,
                            "type": "string",
                            "canBeUsedToMatch": true
                        },
                        {
                            "id": "PHONE NUMBER",
                            "displayName": "PHONE NUMBER",
                            "required": false,
                            "defaultMatch": false,
                            "display": true,
                            "type": "string",
                            "canBeUsedToMatch": true
                        },
                        {
                            "id": "VOTE ",
                            "displayName": "VOTE ",
                            "required": false,
                            "defaultMatch": false,
                            "display": true,
                            "type": "string",
                            "canBeUsedToMatch": true
                        },
                        {
                            "id": "CONSIDERATIONS",
                            "displayName": "CONSIDERATIONS",
                            "required": false,
                            "defaultMatch": false,
                            "display": true,
                            "type": "string",
                            "canBeUsedToMatch": true
                        }
                    ],
                    "attemptToConvertTypes": false,
                    "convertFieldsToString": false
                },
                "options": {}
            },
            "type": "n8n-nodes-base.googleSheets",
            "typeVersion": 4.5,
            "position": [
                320,
                180
            ],
            "id": "f3428b92-72a0-4fbd-933a-fdd8f6f9bb99",
            "name": "add_candidate_info",
            "credentials": {
                "googleSheetsOAuth2Api": {
                    "id": "nThsUaAnp89gpg1D",
                    "name": "account"
                }
            }
        },
        {
            "parameters": {
                "pollTimes": {
                    "item": [
                        {
                            "mode": "everyMinute"
                        }
                    ]
                },
                "triggerOn": "specificFolder",
                "folderToWatch": {
                    "__rl": true,
                    "value": "1K2xQ0HCpO2ZgqSMY-NZAnrf_CclyAmX4",
                    "mode": "list",
                    "cachedResultName": "to_analyze",
                    "cachedResultUrl": "https://drive.google.com/drive/folders/1K2xQ0HCpO2ZgqSMY-NZAnrf_CclyAmX4"
                },
                "event": "fileCreated",
                "options": {}
            },
            "type": "n8n-nodes-base.googleDriveTrigger",
            "typeVersion": 1,
            "position": [
                -2520,
                100
            ],
            "id": "c0958cfa-f169-465b-9bb0-34d8ced301c6",
            "name": "new_candidate_added",
            "credentials": {
                "googleDriveOAuth2Api": {
                    "id": "PGRgMM0fa2Bi77rT",
                    "name": "account"
                }
            }
        },
        {
            "parameters": {
                "content": "## Extracción de datos",
                "height": 400,
                "width": 1100,
                "color": 3
            },
            "type": "n8n-nodes-base.stickyNote",
            "typeVersion": 1,
            "position": [
                -2580,
                20
            ],
            "id": "8e588f44-c10f-44d9-811f-4ed5000aec5c",
            "name": "Sticky Note"
        },
        {
            "parameters": {
                "content": "## Resumen de la información",
                "height": 400,
                "width": 560
            },
            "type": "n8n-nodes-base.stickyNote",
            "typeVersion": 1,
            "position": [
                -1440,
                20
            ],
            "id": "f0c842f4-2e0a-4b6e-9ff2-7338c7af62ca",
            "name": "Sticky Note1"
        },
        {
            "parameters": {
                "content": "## Estimación del voto y la explicación",
                "height": 500,
                "width": 1080,
                "color": 5
            },
            "type": "n8n-nodes-base.stickyNote",
            "typeVersion": 1,
            "position": [
                -840,
                20
            ],
            "id": "4a6a50bb-dea4-487c-99e6-ccc7f4ed690d",
            "name": "Sticky Note2"
        },
        {
            "parameters": {
                "content": "## Guardado de datos y comunicación con el responsable RRHH",
                "height": 500,
                "width": 1180,
                "color": 7
            },
            "type": "n8n-nodes-base.stickyNote",
            "typeVersion": 1,
            "position": [
                260,
                20
            ],
            "id": "b7af20a1-e38a-4697-a97f-9227b64cad47",
            "name": "Sticky Note3"
        }
    ],
    "connections": {
        "Extract from File": {
            "main": [
                [
                    {
                        "node": "Personal data",
                        "type": "main",
                        "index": 0
                    },
                    {
                        "node": "Skills",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "OpenAI Chat Model": {
            "ai_languageModel": [
                [
                    {
                        "node": "Personal data",
                        "type": "ai_languageModel",
                        "index": 0
                    },
                    {
                        "node": "Skills",
                        "type": "ai_languageModel",
                        "index": 0
                    },
                    {
                        "node": "Summarization Chain",
                        "type": "ai_languageModel",
                        "index": 0
                    },
                    {
                        "node": "Basic LLM Chain",
                        "type": "ai_languageModel",
                        "index": 0
                    }
                ]
            ]
        },
        "Personal data": {
            "main": [
                [
                    {
                        "node": "Merge",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "Skills": {
            "main": [
                [
                    {
                        "node": "Merge",
                        "type": "main",
                        "index": 1
                    }
                ]
            ]
        },
        "Merge": {
            "main": [
                [
                    {
                        "node": "Summarization Chain",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "Summarization Chain": {
            "main": [
                [
                    {
                        "node": "download_job_post",
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
                        "node": "Basic LLM Chain",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "Basic LLM Chain": {
            "main": [
                [
                    {
                        "node": "add_candidate_info",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "Structured Output Parser": {
            "ai_outputParser": [
                [
                    {
                        "node": "Basic LLM Chain",
                        "type": "ai_outputParser",
                        "index": 0
                    }
                ]
            ]
        },
        "If": {
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
        },
        "Extract from File1": {
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
        "download_candidate_cv": {
            "main": [
                [
                    {
                        "node": "Extract from File",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "download_job_post": {
            "main": [
                [
                    {
                        "node": "Extract from File1",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "move_cv_to_analyzed": {
            "main": [
                [
                    {
                        "node": "If",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "add_candidate_info": {
            "main": [
                [
                    {
                        "node": "move_cv_to_analyzed",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "new_candidate_added": {
            "main": [
                [
                    {
                        "node": "download_candidate_cv",
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
