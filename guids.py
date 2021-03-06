"""
Common EFI GUIDs and utility functions
"""

from uuid import UUID


ZERO_GUID                           = UUID('{00000000-0000-0000-0000-000000000000}')

EFI_CAPSULE_GUID                    = UUID('{3B6686BD-0D76-4030-B70E-B5519E2FC5A0}')
EFI_SIGNED_CAPSULE_GUID             = UUID('{4A3CA68B-7723-48FB-803D-578CC1FEC44D}')

EFI_FIRMWARE_FILE_SYSTEM_GUID       = UUID('{7A9354D9-0468-444A-81CE-0BF617D890DF}')
EFI_FIRMWARE_FILE_SYSTEM2_GUID      = UUID('{8C8CE578-8A3D-4F1C-9935-896185C32DD3}')
EFI_FIRMWARE_FILE_SYSTEM3_GUID      = UUID('{5473C07A-3DCB-4DCA-BD6F-1E9689E7349A}')
EFI_SYSTEM_NV_DATA_FV_GUID          = UUID('{FFF12B8D-7696-4C8B-A985-2747075B4F50}')

EFI_FFS_VOLUME_TOP_FILE_GUID        = UUID('{1BA0062E-C779-4582-8566-336AE8F78F09}')

EFI_CERT_TYPE_RSA2048_SHA256_GUID   = UUID('{A7717414-C616-4977-9420-844712A735BF}')
EFI_CERT_TYPE_PKCS7_GUID            = UUID('{4AAFD29D-68DF-49EE-8AA9-347D375665A7}')
EFI_CERT_SHA256_GUID                = UUID('{C1C41626-504C-4092-ACA9-41F936934328}')
EFI_CERT_RSA2048_GUID               = UUID('{3C5766E8-269C-4E34-AA14-ED776E85B3B6}')
EFI_CERT_RSA2048_SHA256_GUID        = UUID('{E2B36190-879B-4A3D-AD8D-F2E7BBA32784}')
EFI_CERT_SHA1_GUID                  = UUID('{826CA512-CF10-4AC9-B187-BE01496631BD}')
EFI_CERT_RSA2048_SHA1_GUID          = UUID('{67F8444F-8743-48F1-A328-1EAAB8736080}')
EFI_CERT_X509_GUID                  = UUID('{A5C059A1-94E4-4AA7-87B5-AB155C2BF072}')
EFI_CERT_SHA224_GUID                = UUID('{0B6E5233-A65C-44C9-9407-D9AB83BFC8BD}')
EFI_CERT_SHA384_GUID                = UUID('{FF3E5307-9FD0-48C9-85F1-8AD56C701E01}')
EFI_CERT_SHA512_GUID                = UUID('{093E0FAE-A6C4-4F50-9F1B-D41E2B89C19A}')

EFI_HASH_ALGORITHM_SHA1_GUID        = UUID('{2AE9D80F-3FB2-4095-B7B1-E93157B946B6}')
EFI_HASH_ALGORITHM_SHA224_GUID      = UUID('{8DF01A06-9BD5-4BF7-B021-DB4FD9CCF45B}')
EFI_HASH_ALGORITHM_SHA256_GUID      = UUID('{51AA59DE-FDF2-4EA3-BC63-875FB7842EE9}')
EFI_HASH_ALGORITHM_SHA384_GUID      = UUID('{EFA96432-DE33-4DD2-AEE6-328C33DF777A}')
EFI_HASH_ALGORITHM_SHA512_GUID      = UUID('{CAA4381E-750C-4770-B870-7A23B4E42130}')
EFI_HASH_ALGORTIHM_MD5_GUID         = UUID('{0AF7C79C-65B5-4319-B0AE-44EC484E4AD7}')

EFI_SECTION_CRC32_GUID              = UUID('{FC1BCDB0-7D31-49AA-936A-A4600D9DD083}')
EFI_SECTION_TIANO_COMPRESS_GUID     = UUID('{A31280AD-481E-41B6-95E8-127F4C984779}')
EFI_SECTION_LZMA_COMPRESS_GUID      = UUID('{EE4E5898-3914-4259-9D6E-DC7BD79403CF}')
EFI_SECTION_LZMAF86_COMPRESS_GUID   = UUID('{D42AE6BD-1352-4BFB-909A-CA72A6EAE889}')
EFI_SECTION_VPDTOOL_GUID            = UUID('{8C3D856A-9BE6-468E-850A-24F7A8D38E08}')


CAPSULE_GUIDS = (
    EFI_CAPSULE_GUID.bytes_le,
    EFI_SIGNED_CAPSULE_GUID.bytes_le,
)

FFS_GUIDS = (
    EFI_FIRMWARE_FILE_SYSTEM_GUID.bytes_le,
    EFI_FIRMWARE_FILE_SYSTEM2_GUID.bytes_le,
    EFI_FIRMWARE_FILE_SYSTEM3_GUID.bytes_le,
)

SECTION_GUIDS = (
    EFI_SECTION_CRC32_GUID.bytes_le,
    EFI_SECTION_TIANO_COMPRESS_GUID.bytes_le,
    EFI_SECTION_LZMA_COMPRESS_GUID.bytes_le,
    EFI_SECTION_LZMAF86_COMPRESS_GUID.bytes_le,
    EFI_SECTION_VPDTOOL_GUID.bytes_le,
)


GUID_NAME = {
    ZERO_GUID: 'ZERO_GUID',
    EFI_CAPSULE_GUID: 'EFI_CAPSULE_GUID',
    EFI_SIGNED_CAPSULE_GUID: 'EFI_SIGNED_CAPSULE_GUID',
    EFI_FIRMWARE_FILE_SYSTEM_GUID: 'EFI_FIRMWARE_FILE_SYSTEM_GUID',
    EFI_FIRMWARE_FILE_SYSTEM2_GUID: 'EFI_FIRMWARE_FILE_SYSTEM2_GUID',
    EFI_FIRMWARE_FILE_SYSTEM3_GUID: 'EFI_FIRMWARE_FILE_SYSTEM3_GUID',
    EFI_SYSTEM_NV_DATA_FV_GUID: 'EFI_SYSTEM_NV_DATA_FV_GUID',
    EFI_FFS_VOLUME_TOP_FILE_GUID: 'EFI_FFS_VOLUME_TOP_FILE_GUID',
    EFI_CERT_TYPE_RSA2048_SHA256_GUID: 'EFI_CERT_TYPE_RSA2048_SHA256_GUID',
    EFI_CERT_TYPE_PKCS7_GUID: 'EFI_CERT_TYPE_PKCS7_GUID',
    EFI_CERT_SHA256_GUID: 'EFI_CERT_SHA256_GUID',
    EFI_CERT_RSA2048_GUID: 'EFI_CERT_RSA2048_GUID',
    EFI_CERT_RSA2048_SHA256_GUID: 'EFI_CERT_RSA2048_SHA256_GUID',
    EFI_CERT_SHA1_GUID: 'EFI_CERT_SHA1_GUID',
    EFI_CERT_RSA2048_SHA1_GUID: 'EFI_CERT_RSA2048_SHA1_GUID',
    EFI_CERT_X509_GUID: 'EFI_CERT_X509_GUID',
    EFI_CERT_SHA224_GUID: 'EFI_CERT_SHA224_GUID',
    EFI_CERT_SHA384_GUID: 'EFI_CERT_SHA384_GUID',
    EFI_CERT_SHA512_GUID: 'EFI_CERT_SHA512_GUID',
    EFI_HASH_ALGORITHM_SHA1_GUID: 'EFI_HASH_ALGORITHM_SHA1_GUID',
    EFI_HASH_ALGORITHM_SHA224_GUID: 'EFI_HASH_ALGORITHM_SHA224_GUID',
    EFI_HASH_ALGORITHM_SHA256_GUID: 'EFI_HASH_ALGORITHM_SHA256_GUID',
    EFI_HASH_ALGORITHM_SHA384_GUID: 'EFI_HASH_ALGORITHM_SHA384_GUID',
    EFI_HASH_ALGORITHM_SHA512_GUID: 'EFI_HASH_ALGORITHM_SHA512_GUID',
    EFI_HASH_ALGORTIHM_MD5_GUID: 'EFI_HASH_ALGORTIHM_MD5_GUID',
    EFI_SECTION_CRC32_GUID: 'EFI_SECTION_CRC32_GUID',
    EFI_SECTION_TIANO_COMPRESS_GUID: 'EFI_SECTION_TIANO_COMPRESS_GUID',
    EFI_SECTION_LZMA_COMPRESS_GUID: 'EFI_SECTION_LZMA_COMPRESS_GUID',
    EFI_SECTION_LZMAF86_COMPRESS_GUID: 'EFI_SECTION_LZMAF86_COMPRESS_GUID',
    EFI_SECTION_VPDTOOL_GUID: 'EFI_SECTION_VPDTOOL_GUID',
}


def name(guid):
    if guid in GUID_NAME:
        return GUID_NAME[guid]
    else:
        return str(guid)
