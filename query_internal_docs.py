{
  "nodes": [
    {
      "parameters": {
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "typeVersion": 1.1,
      "position": [
        -140,
        -200
      ],
      "id": "7935c338-5d51-4acd-bad7-49889ce3f325",
      "name": "When chat message received",
      "webhookId": "4aad9899-98b5-428e-8d5e-bc856d72253d"
    },
    {
      "parameters": {
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 1.8,
      "position": [
        80,
        -200
      ],
      "id": "4c5417ad-e00f-418d-bffb-3d8ba3e93b34",
      "name": "AI Agent"
    },
    {
      "parameters": {},
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "typeVersion": 1.3,
      "position": [
        140,
        20
      ],
      "id": "12542102-5107-4eea-82c2-238c36b192cc",
      "name": "Simple Memory"
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
        -20,
        20
      ],
      "id": "936ffb34-41c7-4420-be22-3991d63a285e",
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
        "name": "documents_info",
        "description": "Here there is information related to internal documents, in this case, these are the documents:\n- River Global Investors FUNDS ICVC"
      },
      "type": "@n8n/n8n-nodes-langchain.toolVectorStore",
      "typeVersion": 1,
      "position": [
        300,
        20
      ],
      "id": "24294ae4-15fd-49cb-b999-6eb16a558111",
      "name": "Answer questions with a vector store"
    },
    {
      "parameters": {
        "pineconeIndex": {
          "__rl": true,
          "value": "funds",
          "mode": "list",
          "cachedResultName": "funds"
        },
        "options": {
          "pineconeNamespace": "funds_info"
        }
      },
      "type": "@n8n/n8n-nodes-langchain.vectorStorePinecone",
      "typeVersion": 1,
      "position": [
        100,
        220
      ],
      "id": "2515959e-510a-4c6e-b326-775917ae6700",
      "name": "Pinecone Vector Store",
      "credentials": {
        "pineconeApi": {
          "id": "F1XVBnapLYl6sSHd",
          "name": "account"
        }
      }
    },
    {
      "parameters": {
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.embeddingsOpenAi",
      "typeVersion": 1.2,
      "position": [
        40,
        380
      ],
      "id": "fa0ab167-3a32-459a-acd6-15afdc101c15",
      "name": "Embeddings OpenAI",
      "credentials": {
        "openAiApi": {
          "id": "itdQkm1FKULykRHF",
          "name": "OpenAi account"
        }
      }
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
        440,
        220
      ],
      "id": "a4468bf7-db2e-4180-b2b8-0762ace50cbc",
      "name": "OpenAI Chat Model1",
      "credentials": {
        "openAiApi": {
          "id": "itdQkm1FKULykRHF",
          "name": "OpenAi account"
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
          "value": "1MEL5W2WHExbooyThWCE1UQJFRaR8A0XG",
          "mode": "list",
          "cachedResultName": "internal docs",
          "cachedResultUrl": "https://drive.google.com/drive/folders/1MEL5W2WHExbooyThWCE1UQJFRaR8A0XG"
        },
        "event": "fileCreated",
        "options": {}
      },
      "id": "cb282e5a-3498-4a6d-b5f8-f5b2b9220a68",
      "name": "Monitor Google Drive for New Files",
      "type": "n8n-nodes-base.googleDriveTrigger",
      "position": [
        -160,
        -800
      ],
      "typeVersion": 1,
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
          "mode": "id",
          "value": "={{ $json.id }}"
        },
        "options": {}
      },
      "id": "8b2edced-1823-4ced-9566-454a0a77b348",
      "name": "Download File from Google Drive",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        60,
        -800
      ],
      "typeVersion": 3,
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "PGRgMM0fa2Bi77rT",
          "name": "account"
        }
      }
    },
    {
      "parameters": {
        "operation": "pdf",
        "options": {}
      },
      "id": "4931a022-3f28-4b45-b66d-7c095103ab80",
      "name": "Extract PDF Content",
      "type": "n8n-nodes-base.extractFromFile",
      "position": [
        280,
        -800
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "mode": "insert",
        "pineconeIndex": {
          "__rl": true,
          "value": "funds",
          "mode": "list",
          "cachedResultName": "funds"
        },
        "options": {
          "pineconeNamespace": "funds_info"
        }
      },
      "id": "e9f13127-73d6-460c-beed-68ef1ce2162c",
      "name": "Insert Document into Pinecone Vector Store",
      "type": "@n8n/n8n-nodes-langchain.vectorStorePinecone",
      "position": [
        520,
        -800
      ],
      "typeVersion": 1,
      "credentials": {
        "pineconeApi": {
          "id": "F1XVBnapLYl6sSHd",
          "name": "account"
        }
      }
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "f7c95921-83fc-4974-a74d-e5752ffae4ee",
      "name": "Load Document Data for Processing",
      "type": "@n8n/n8n-nodes-langchain.documentDefaultDataLoader",
      "position": [
        600,
        -600
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "chunkSize": 3000,
        "chunkOverlap": 300,
        "options": {}
      },
      "id": "8419cc15-95c0-4e56-ac21-d040946b8004",
      "name": "Split Document Text into Chunks",
      "type": "@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter",
      "position": [
        540,
        -420
      ],
      "typeVersion": 1
    },
    {
      "parameters": {
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.embeddingsOpenAi",
      "typeVersion": 1.2,
      "position": [
        420,
        -600
      ],
      "id": "1ca6bb21-a27f-4ed3-a34c-b719a2858adb",
      "name": "Embeddings OpenAI1",
      "credentials": {
        "openAiApi": {
          "id": "itdQkm1FKULykRHF",
          "name": "OpenAi account"
        }
      }
    }
  ],
  "connections": {
    "When chat message received": {
      "main": [
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Simple Memory": {
      "ai_memory": [
        [
          {
            "node": "AI Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Answer questions with a vector store": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Pinecone Vector Store": {
      "ai_vectorStore": [
        [
          {
            "node": "Answer questions with a vector store",
            "type": "ai_vectorStore",
            "index": 0
          }
        ]
      ]
    },
    "Embeddings OpenAI": {
      "ai_embedding": [
        [
          {
            "node": "Pinecone Vector Store",
            "type": "ai_embedding",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "Answer questions with a vector store",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Monitor Google Drive for New Files": {
      "main": [
        [
          {
            "node": "Download File from Google Drive",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Download File from Google Drive": {
      "main": [
        [
          {
            "node": "Extract PDF Content",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract PDF Content": {
      "main": [
        [
          {
            "node": "Insert Document into Pinecone Vector Store",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Load Document Data for Processing": {
      "ai_document": [
        [
          {
            "node": "Insert Document into Pinecone Vector Store",
            "type": "ai_document",
            "index": 0
          }
        ]
      ]
    },
    "Split Document Text into Chunks": {
      "ai_textSplitter": [
        [
          {
            "node": "Load Document Data for Processing",
            "type": "ai_textSplitter",
            "index": 0
          }
        ]
      ]
    },
    "Embeddings OpenAI1": {
      "ai_embedding": [
        [
          {
            "node": "Insert Document into Pinecone Vector Store",
            "type": "ai_embedding",
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