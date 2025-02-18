from utils import endpoint_request
from langchain_core.tools import tool


export_metabody_data = {
    'data': {
        "connectionType": "ConnectionType",
        "connectionId": "string",
        "virtualServerId": "string",
        "signingSettings": {
            "signingKeyPairRef": {
                "id": "string",
                "location": "string"
            },
            "algorithm": "string",
            "includeRawKeyInSignature": "boolean",
            "includeCertInSignature": "boolean"
        },
        "useSecondaryPortForSoap": "boolean"
    },
    'param': {},
    'url': "/connectionMetabody/export",
    'req_type': 'POST'
}

convert_metabody_data = {
    'data': {
        "connectionType": "ConnectionType",
        "expectedProtocol": "MetadataProtocol",
        "expectedEntityId": "string",
        "samlMetadata": "string",
        "verificationCertificate": "string",
        "templateConnection": {
            "type": "ConnectionType",
            "id": "string",
            "entityId": "string",
            "name": "string",
            "active": "boolean",
            "baseUrl": "string",
            "defaultVirtualEntityId": "string",
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
            "loggingMode": "LoggingMode"
        }
    },
    'param': {},
    'url': "/connectionMetabody/convert",
    'req_type': 'POST'
}

@tool
def export_metabody():
    "export the connection metadata"
    return endpoint_request(
        url=export_metabody_data['url'],
        data=export_metabody_data['data'],
        req_type=export_metabody_data['req_type']
    )

@tool
def convert_metabody():
    "convert the connection metadata"
    return endpoint_request(
        url=convert_metabody_data['url'],
        data=convert_metabody_data['data'],
        req_type=convert_metabody_data['req_type']
    )




connection_meta_tools = [export_metabody,
                         convert_metabody]