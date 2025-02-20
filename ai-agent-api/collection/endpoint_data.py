# endpoint_data.py

# GET /idp/spConnections
get_sp_connections_data = {
    'url': "/idp/spConnections",
    'req_type': "GET",
    'param': {
        "entityId": "",
        "page": "",
        "numberPerPage": "",
        "filter": ""
    },
    'data': {
        "type": "ConnectionType",
        "id": "string",
        "entityId": "string",
        "name": "string",
        "active": "boolean",
        "baseUrl": "string",
        "defaultVirtualEntityId": "string",
        "spBrowserSso": {
            "protocol": "Protocol",
            "wsFedTokenType": "WsFedTokenType",
            "enabledProfiles": [
                "Profile"
            ],
            "incomingBindings": [
                "Binding"
            ],
            "artifact": {
                "lifetime": "integer",
                "resolverLocations": [
                    {
                        "index": "integer",
                        "url": "string"
                    }
                ],
                "sourceId": "string"
            },
            "urlWhitelistEntries": [
                {
                    "validDomain": "string",
                    "validPath": "string",
                    "allowQueryAndFragment": "boolean",
                    "requireHttps": "boolean"
                }
            ],
            "sloServiceEndpoints": [
                {
                    "binding": "Binding",
                    "url": "string",
                    "responseUrl": "string"
                }
            ],
            "defaultTargetUrl": "string",
            "ssoServiceEndpoints": [
                {
                    "binding": "Binding",
                    "url": "string",
                    "isDefault": "boolean",
                    "index": "integer"
                }
            ],
            "spSamlIdentityMapping": "SpSamlIdentityMapping",
            "spWsFedIdentityMapping": "SpWsFedIdentityMapping",
            "signAssertions": "boolean",
            "requireSignedAuthnRequests": "boolean",
            "encryptionPolicy": {
                "encryptAssertion": "boolean",
                "encryptedAttributes": [
                    "string"
                ],
                "encryptSloSubjectNameId": "boolean",
                "sloSubjectNameIDEncrypted": "boolean"
            },
            "attributeContract": {
                "coreAttributes": [
                    {
                        "nameFormat": "string",
                        "name": "string"
                    }
                ],
                "extendedAttributes": [
                    {
                        "nameFormat": "string",
                        "name": "string"
                    }
                ]
            },
            "adapterMappings": [
                {
                    "idpAdapterRef": {
                        "id": "string",
                        "location": "string"
                    },
                    "restrictVirtualEntityIds": "boolean",
                    "restrictedVirtualEntityIds": [
                        "string"
                    ],
                    "attributeSources": [
                        {
                            "type": "DataStoreType",
                            "dataStoreRef": {
                                "id": "string",
                                "location": "string"
                            },
                            "id": "string",
                            "description": "string",
                            "attributeContractFulfillment": {
                                "key": {
                                    "source": {
                                        "type": "SourceType",
                                        "id": "string"
                                    },
                                    "value": "string"
                                }
                            }
                        }
                    ],
                    "attributeContractFulfillment": {
                        "key": {
                            "source": {
                                "type": "SourceType",
                                "id": "string"
                            },
                            "value": "string"
                        }
                    },
                    "issuanceCriteria": {
                        "conditionalCriteria": [
                            {
                                "source": {
                                    "type": "SourceType",
                                    "id": "string"
                                },
                                "attributeName": "string",
                                "condition": "ConditionType",
                                "value": "string",
                                "errorResult": "string"
                            }
                        ],
                        "expressionCriteria": [
                            {
                                "expression": "string",
                                "errorResult": "string"
                            }
                        ]
                    }
                }
            ],
            "authenticationPolicyContractAssertionMappings": [
                {
                    "authenticationPolicyContractRef": {
                        "id": "string",
                        "location": "string"
                    },
                    "restrictVirtualEntityIds": "boolean",
                    "restrictedVirtualEntityIds": [
                        "string"
                    ],
                    "attributeSources": [
                        {
                            "type": "DataStoreType",
                            "dataStoreRef": {
                                "id": "string",
                                "location": "string"
                            },
                            "id": "string",
                            "description": "string",
                            "attributeContractFulfillment": {
                                "key": {
                                    "source": {
                                        "type": "SourceType",
                                        "id": "string"
                                    },
                                    "value": "string"
                                }
                            }
                        }
                    ],
                    "attributeContractFulfillment": {
                        "key": {
                            "source": {
                                "type": "SourceType",
                                "id": "string"
                            },
                            "value": "string"
                        }
                    },
                    "issuanceCriteria": {
                        "conditionalCriteria": [
                            {
                                "source": {
                                    "type": "SourceType",
                                    "id": "string"
                                },
                                "attributeName": "string",
                                "condition": "ConditionType",
                                "value": "string",
                                "errorResult": "string"
                            }
                        ],
                        "expressionCriteria": [
                            {
                                "expression": "string",
                                "errorResult": "string"
                            }
                        ]
                    }
                }
            ],
            "messageCustomizations": [
                {
                    "contextName": "string",
                    "messageExpression": "string"
                }
            ],
            "assertionLifetime": {
                "minutesBefore": "integer",
                "minutesAfter": "integer"
            }
        },
        "attributeQuery": {
            "attributes": [
                "string"
            ],
            "attributeSources": [
                {
                    "type": "DataStoreType",
                    "dataStoreRef": {
                        "id": "string",
                        "location": "string"
                    },
                    "id": "string",
                    "description": "string",
                    "attributeContractFulfillment": {
                        "key": {
                            "source": {
                                "type": "SourceType",
                                "id": "string"
                            },
                            "value": "string"
                        }
                    }
                }
            ],
            "attributeContractFulfillment": {
                "key": {
                    "source": {
                        "type": "SourceType",
                        "id": "string"
                    },
                    "value": "string"
                }
            },
            "issuanceCriteria": {
                "conditionalCriteria": [
                    {
                        "source": {
                            "type": "SourceType",
                            "id": "string"
                        },
                        "attributeName": "string",
                        "condition": "ConditionType",
                        "value": "string",
                        "errorResult": "string"
                    }
                ],
                "expressionCriteria": [
                    {
                        "expression": "string",
                        "errorResult": "string"
                    }
                ]
            },
            "policy": {
                "signResponse": "boolean",
                "signAssertion": "boolean",
                "encryptAssertion": "boolean",
                "requireSignedAttributeQuery": "boolean",
                "requireEncryptedNameId": "boolean"
            }
        },
        "virtualEntityIds": [
            "string"
        ],
        "metadataReloadSettings": {
            "metadataUrlRef": {
                "id": "string",
                "location": "string"
            },
            "enableAutoMetadataUpdate": "boolean"
        },
        "credentials": {
            "verificationSubjectDN": "string",
            "verificationIssuerDN": "string",
            "certs": [
                {
                    "certView": {
                        "id": "string",
                        "serialNumber": "string",
                        "subjectDN": "string",
                        "issuerDN": "string",
                        "validFrom": "string",
                        "expires": "string",
                        "keyAlgorithm": "string",
                        "keySize": "integer",
                        "signatureAlgorithm": "string",
                        "version": "integer",
                        "md5Fingerprint": "string",
                        "sha1Fingerprint": "string",
                        "sha256Fingerprint": "string",
                        "status": "CertificateValidity",
                        "cryptoProvider": "CryptoProvider"
                    },
                    "x509File": {
                        "fileData": "string",
                        "cryptoProvider": "CryptoProvider"
                    },
                    "primaryVerificationCert": "boolean",
                    "secondaryVerificationCert": "boolean",
                    "encryptionCert": "boolean"
                }
            ],
            "blockEncryptionAlgorithm": "string",
            "keyTransportAlgorithm": "string",
            "signingSettings": {
                "signingKeyPairRef": {
                    "id": "string",
                    "location": "string"
                },
                "algorithm": "string",
                "includeRawKeyInSignature": "boolean",
                "includeCertInSignature": "boolean"
            },
            "decryptionKeyPairRef": {
                "id": "string",
                "location": "string"
            },
            "secondaryDecryptionKeyPairRef": {
                "id": "string",
                "location": "string"
            },
            "outboundBackChannelAuth": {
                "type": "BackChannelAuthType",
                "httpBasicCredentials": {
                    "username": "string",
                    "password": "string",
                    "encryptedPassword": "string"
                },
                "digitalSignature": "boolean",
                "sslAuthKeyPairRef": {
                    "id": "string",
                    "location": "string"
                },
                "validatePartnerCert": "boolean"
            },
            "inboundBackChannelAuth": {
                "type": "BackChannelAuthType",
                "httpBasicCredentials": {
                    "username": "string",
                    "password": "string",
                    "encryptedPassword": "string"
                },
                "digitalSignature": "boolean",
                "verificationSubjectDN": "string",
                "verificationIssuerDN": "string",
                "certs": [
                    {
                        "certView": {
                            "id": "string",
                            "serialNumber": "string",
                            "subjectDN": "string",
                            "issuerDN": "string",
                            "validFrom": "string",
                            "expires": "string",
                            "keyAlgorithm": "string",
                            "keySize": "integer",
                            "signatureAlgorithm": "string",
                            "version": "integer",
                            "md5Fingerprint": "string",
                            "sha1Fingerprint": "string",
                            "sha256Fingerprint": "string",
                            "status": "CertificateValidity",
                            "cryptoProvider": "CryptoProvider"
                        },
                        "x509File": {
                            "fileData": "string",
                            "cryptoProvider": "CryptoProvider"
                        },
                        "primaryVerificationCert": "boolean",
                        "secondaryVerificationCert": "boolean",
                        "encryptionCert": "boolean"
                    }
                ],
                "requireSsl": "boolean"
            }
        },
        "contactInfo": {
            "company": "string",
            "email": "string",
            "firstName": "string",
            "lastName": "string",
            "phone": "string"
        },
        "licenseConnectionGroup": "string",
        "applicationName": "string",
        "applicationIconUrl": "string",
        "loggingMode": "LoggingMode"
    }
}

# POST /idp/spConnections
create_sp_connections_data = {
    'url': "/idp/spConnections",
    'req_type': "POST",
    'param': {},
    'data': {}
}

# GET /idp/spConnections/{id}
get_sp_connection_by_id_data = {
    'url': "/idp/spConnections/{id}",
    'req_type': "GET",
    'param': {},
    'data': {}
}

# PUT /idp/spConnections/{id}
update_sp_connection_data = {
    'url': "/idp/spConnections/{id}",
    'req_type': "PUT",
    'param': {},
    'data': {
        "type": "ConnectionType",
        "id": "string",
        "entityId": "string",
        "name": "string",
        "active": "boolean",
        "baseUrl": "string",
        "defaultVirtualEntityId": "string",
        "spBrowserSso": {
            "protocol": "Protocol",
            "wsFedTokenType": "WsFedTokenType",
            "enabledProfiles": [
                "Profile"
            ],
            "incomingBindings": [
                "Binding"
            ],
            "artifact": {
                "lifetime": "integer",
                "resolverLocations": [
                    {
                        "index": "integer",
                        "url": "string"
                    }
                ],
                "sourceId": "string"
            },
            "urlWhitelistEntries": [
                {
                    "validDomain": "string",
                    "validPath": "string",
                    "allowQueryAndFragment": "boolean",
                    "requireHttps": "boolean"
                }
            ],
            "sloServiceEndpoints": [
                {
                    "binding": "Binding",
                    "url": "string",
                    "responseUrl": "string"
                }
            ],
            "defaultTargetUrl": "string",
            "ssoServiceEndpoints": [
                {
                    "binding": "Binding",
                    "url": "string",
                    "isDefault": "boolean",
                    "index": "integer"
                }
            ],
            "spSamlIdentityMapping": "SpSamlIdentityMapping",
            "spWsFedIdentityMapping": "SpWsFedIdentityMapping",
            "signAssertions": "boolean",
            "requireSignedAuthnRequests": "boolean",
            "encryptionPolicy": {
                "encryptAssertion": "boolean",
                "encryptedAttributes": [
                    "string"
                ],
                "encryptSloSubjectNameId": "boolean",
                "sloSubjectNameIDEncrypted": "boolean"
            },
            "attributeContract": {
                "coreAttributes": [
                    {
                        "nameFormat": "string",
                        "name": "string"
                    }
                ],
                "extendedAttributes": [
                    {
                        "nameFormat": "string",
                        "name": "string"
                    }
                ]
            },
            "adapterMappings": [
                {
                    "idpAdapterRef": {
                        "id": "string",
                        "location": "string"
                    },
                    "restrictVirtualEntityIds": "boolean",
                    "restrictedVirtualEntityIds": [
                        "string"
                    ],
                    "attributeSources": [
                        {
                            "type": "DataStoreType",
                            "dataStoreRef": {
                                "id": "string",
                                "location": "string"
                            },
                            "id": "string",
                            "description": "string",
                            "attributeContractFulfillment": {
                                "key": {
                                    "source": {
                                        "type": "SourceType",
                                        "id": "string"
                                    },
                                    "value": "string"
                                }
                            }
                        }
                    ],
                    "attributeContractFulfillment": {
                        "key": {
                            "source": {
                                "type": "SourceType",
                                "id": "string"
                            },
                            "value": "string"
                        }
                    },
                    "issuanceCriteria": {
                        "conditionalCriteria": [
                            {
                                "source": {
                                    "type": "SourceType",
                                    "id": "string"
                                },
                                "attributeName": "string",
                                "condition": "ConditionType",
                                "value": "string",
                                "errorResult": "string"
                            }
                        ],
                        "expressionCriteria": [
                            {
                                "expression": "string",
                                "errorResult": "string"
                            }
                        ]
                    }
                }
            ],
            "authenticationPolicyContractAssertionMappings": [
                {
                    "authenticationPolicyContractRef": {
                        "id": "string",
                        "location": "string"
                    },
                    "restrictVirtualEntityIds": "boolean",
                    "restrictedVirtualEntityIds": [
                        "string"
                    ],
                    "attributeSources": [
                        {
                            "type": "DataStoreType",
                            "dataStoreRef": {
                                "id": "string",
                                "location": "string"
                            },
                            "id": "string",
                            "description": "string",
                            "attributeContractFulfillment": {
                                "key": {
                                    "source": {
                                        "type": "SourceType",
                                        "id": "string"
                                    },
                                    "value": "string"
                                }
                            }
                        }
                    ],
                    "attributeContractFulfillment": {
                        "key": {
                            "source": {
                                "type": "SourceType",
                                "id": "string"
                            },
                            "value": "string"
                        }
                    },
                    "issuanceCriteria": {
                        "conditionalCriteria": [
                            {
                                "source": {
                                    "type": "SourceType",
                                    "id": "string"
                                },
                                "attributeName": "string",
                                "condition": "ConditionType",
                                "value": "string",
                                "errorResult": "string"
                            }
                        ],
                        "expressionCriteria": [
                            {
                                "expression": "string",
                                "errorResult": "string"
                            }
                        ]
                    }
                }
            ],
            "messageCustomizations": [
                {
                    "contextName": "string",
                    "messageExpression": "string"
                }
            ],
            "assertionLifetime": {
                "minutesBefore": "integer",
                "minutesAfter": "integer"
            }
        },
        "attributeQuery": {
            "attributes": [
                "string"
            ],
            "attributeSources": [
                {
                    "type": "DataStoreType",
                    "dataStoreRef": {
                        "id": "string",
                        "location": "string"
                    },
                    "id": "string",
                    "description": "string",
                    "attributeContractFulfillment": {
                        "key": {
                            "source": {
                                "type": "SourceType",
                                "id": "string"
                            },
                            "value": "string"
                        }
                    }
                }
            ],
            "attributeContractFulfillment": {
                "key": {
                    "source": {
                        "type": "SourceType",
                        "id": "string"
                    },
                    "value": "string"
                }
            },
            "issuanceCriteria": {
                "conditionalCriteria": [
                    {
                        "source": {
                            "type": "SourceType",
                            "id": "string"
                        },
                        "attributeName": "string",
                        "condition": "ConditionType",
                        "value": "string",
                        "errorResult": "string"
                    }
                ],
                "expressionCriteria": [
                    {
                        "expression": "string",
                        "errorResult": "string"
                    }
                ]
            },
            "policy": {
                "signResponse": "boolean",
                "signAssertion": "boolean",
                "encryptAssertion": "boolean",
                "requireSignedAttributeQuery": "boolean",
                "requireEncryptedNameId": "boolean"
            }
        },
        "virtualEntityIds": [
            "string"
        ],
        "metadataReloadSettings": {
            "metadataUrlRef": {
                "id": "string",
                "location": "string"
            },
            "enableAutoMetadataUpdate": "boolean"
        },
        "credentials": {
            "verificationSubjectDN": "string",
            "verificationIssuerDN": "string",
            "certs": [
                {
                    "certView": {
                        "id": "string",
                        "serialNumber": "string",
                        "subjectDN": "string",
                        "issuerDN": "string",
                        "validFrom": "string",
                        "expires": "string",
                        "keyAlgorithm": "string",
                        "keySize": "integer",
                        "signatureAlgorithm": "string",
                        "version": "integer",
                        "md5Fingerprint": "string",
                        "sha1Fingerprint": "string",
                        "sha256Fingerprint": "string",
                        "status": "CertificateValidity",
                        "cryptoProvider": "CryptoProvider"
                    },
                    "x509File": {
                        "fileData": "string",
                        "cryptoProvider": "CryptoProvider"
                    },
                    "primaryVerificationCert": "boolean",
                    "secondaryVerificationCert": "boolean",
                    "encryptionCert": "boolean"
                }
            ],
            "blockEncryptionAlgorithm": "string",
            "keyTransportAlgorithm": "string",
            "signingSettings": {
                "signingKeyPairRef": {
                    "id": "string",
                    "location": "string"
                },
                "algorithm": "string",
                "includeRawKeyInSignature": "boolean",
                "includeCertInSignature": "boolean"
            },
            "decryptionKeyPairRef": {
                "id": "string",
                "location": "string"
            },
            "secondaryDecryptionKeyPairRef": {
                "id": "string",
                "location": "string"
            },
            "outboundBackChannelAuth": {
                "type": "BackChannelAuthType",
                "httpBasicCredentials": {
                    "username": "string",
                    "password": "string",
                    "encryptedPassword": "string"
                },
                "digitalSignature": "boolean",
                "sslAuthKeyPairRef": {
                    "id": "string",
                    "location": "string"
                },
                "validatePartnerCert": "boolean"
            },
            "inboundBackChannelAuth": {
                "type": "BackChannelAuthType",
                "httpBasicCredentials": {
                    "username": "string",
                    "password": "string",
                    "encryptedPassword": "string"
                },
                "digitalSignature": "boolean",
                "verificationSubjectDN": "string",
                "verificationIssuerDN": "string",
                "certs": [
                    {
                        "certView": {
                            "id": "string",
                            "serialNumber": "string",
                            "subjectDN": "string",
                            "issuerDN": "string",
                            "validFrom": "string",
                            "expires": "string",
                            "keyAlgorithm": "string",
                            "keySize": "integer",
                            "signatureAlgorithm": "string",
                            "version": "integer",
                            "md5Fingerprint": "string",
                            "sha1Fingerprint": "string",
                            "sha256Fingerprint": "string",
                            "status": "CertificateValidity",
                            "cryptoProvider": "CryptoProvider"
                        },
                        "x509File": {
                            "fileData": "string",
                            "cryptoProvider": "CryptoProvider"
                        },
                        "primaryVerificationCert": "boolean",
                        "secondaryVerificationCert": "boolean",
                        "encryptionCert": "boolean"
                    }
                ],
                "requireSsl": "boolean"
            }
        },
        "contactInfo": {
            "company": "string",
            "email": "string",
            "firstName": "string",
            "lastName": "string",
            "phone": "string"
        },
        "licenseConnectionGroup": "string",
        "applicationName": "string",
        "applicationIconUrl": "string",
        "loggingMode": "LoggingMode"
    }
}

# DELETE /idp/spConnections/{id}
delete_sp_connection_data = {
    'url': "/idp/spConnections/{id}",
    'req_type': "DELETE",
    'param': {},
    'data': {}
}

# GET /idp/spConnections/{id}/credentials/signingSettings
get_signing_settings_data = {
    'url': "/idp/spConnections/{id}/credentials/signingSettings",
    'req_type': "GET",
    'param': {},
    'data': {}
}

# PUT /idp/spConnections/{id}/credentials/signingSettings
update_signing_settings_data = {
    'url': "/idp/spConnections/{id}/credentials/signingSettings",
    'req_type': "PUT",
    'param': {},
    'data': {
        "signingKeyPairRef": {
            "id": "string",
            "location": "string"
        },
        "algorithm": "string",
        "includeCertInSignature": "boolean",
        "includeRawKeyInSignature": "boolean"
    }
}

# POST /idp/spConnections/{id}/credentials/certs
add_sp_connection_cert_data = {
    'url': "/idp/spConnections/{id}/credentials/certs",
    'req_type': "POST",
    'param': {},
    'data': {
        "certView": {
            "id": "string",
            "serialNumber": "string",
            "subjectDN": "string",
            "subjectAlternativeNames": [
                "string"
            ],
            "issuerDN": "string",
            "validFrom": "string",
            "expires": "string",
            "keyAlgorithm": "string",
            "keySize": "integer",
            "signatureAlgorithm": "string",
            "version": "integer",
            "sha1Fingerprint": "string",
            "sha256Fingerprint": "string",
            "status": "CertificateValidity",
            "cryptoProvider": "CryptoProvider"
        },
        "x509File": {
            "id": "string",
            "fileData": "string",
            "cryptoProvider": "CryptoProvider"
        },
        "activeVerificationCert": "boolean",
        "primaryVerificationCert": "boolean",
        "secondaryVerificationCert": "boolean",
        "encryptionCert": "boolean"
    }
}

# GET /idp/spConnections/{id}/credentials/certs
get_sp_connection_certs_data = {
    'url': "/idp/spConnections/{id}/credentials/certs",
    'req_type': "GET",
    'param': {},
    'data': {}
}

# PUT /idp/spConnections/{id}/credentials/certs
update_sp_connection_certs_data = {
    'url': "/idp/spConnections/{id}/credentials/certs",
    'req_type': "PUT",
    'param': {},
    'data': {
        "items": [
            {
                "certView": {
                    "id": "string",
                    "serialNumber": "string",
                    "subjectDN": "string",
                    "subjectAlternativeNames": [
                        "string"
                    ],
                    "issuerDN": "string",
                    "validFrom": "string",
                    "expires": "string",
                    "keyAlgorithm": "string",
                    "keySize": "integer",
                    "signatureAlgorithm": "string",
                    "version": "integer",
                    "sha1Fingerprint": "string",
                    "sha256Fingerprint": "string",
                    "status": "CertificateValidity",
                    "cryptoProvider": "CryptoProvider"
                },
                "x509File": {
                    "id": "string",
                    "fileData": "string",
                    "cryptoProvider": "CryptoProvider"
                },
                "activeVerificationCert": "boolean",
                "primaryVerificationCert": "boolean",
                "secondaryVerificationCert": "boolean",
                "encryptionCert": "boolean"
            }
        ]
    }
}

# GET /idp/spConnections/{id}/credentials/decryptionKeys
get_sp_connection_decryption_keys_data = {
    'url': "/idp/spConnections/{id}/credentials/decryptionKeys",
    'req_type': "GET",
    'param': {},
    'data': {}
}

# PUT /idp/spConnections/{id}/credentials/decryptionKeys
update_sp_connection_decryption_keys_data = {
    'url': "/idp/spConnections/{id}/credentials/decryptionKeys",
    'req_type': "PUT",
    'param': {},
    'data': {
        "primaryKeyRef": {
            "id": "string",
            "location": "string"
        },
        "secondaryKeyPairRef": {
            "id": "string",
            "location": "string"
        }
    }
}
