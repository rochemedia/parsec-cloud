# Parsec Cloud (https://parsec.cloud) Copyright (c) AGPLv3 2016-2021 Scille SAS

from parsec.api.data.pki import PkiRequest
from parsec.api.data.pki import PkiReply
from parsec.api.protocol.base import BaseRepSchema, BaseReqSchema, CmdSerializer
from parsec.serde import fields
from parsec.serde.schema import BaseSchema
from parsec.serde.serializer import MsgpackSerializer
from parsec.types import UUID4


class PkiCertificateID(UUID4):
    __slots__ = ()


PkiCertificateIDField = fields.enum_field_factory(PkiCertificateID)

# pki_enrolement_request


class PkiEnrollmentRequestReqSchema(BaseSchema):
    request = fields.Nested(PkiRequest.SCHEMA_CLS, required=True)
    certificate_id = fields.String(required=True)  # TODO Move to PkiCertificateIDField
    request_id = fields.String(required=True)
    force_flag = fields.Boolean(required=True)


class PkiEnrollmentRequestRepSchema(BaseRepSchema):
    timestamp = fields.DateTime(required=True)


# pki_enrolement_get_requests


class PkiEnrollmentGetRequestsReqSchema(BaseReqSchema):
    pass


class PkiEnrollmentGetRequestsRepSchema(BaseRepSchema):
    requests = fields.List(
        fields.Tuple(
            fields.String(required=True),
            fields.String(required=True),
            fields.Nested(PkiRequest.SCHEMA_CLS, required=True),
        ),
        required=True,
    )


# pki_enrolement_reply


class PkiEnrollmentReplyReqSchema(BaseReqSchema):
    certificate_id = fields.String(required=True)
    request_id = fields.String(required=True)
    reply = fields.Nested(PkiReply.SCHEMA_CLS, Required=True)
    user_id = fields.String(required=False)  # TODO Move to userid ?


class PkiEnrollmentReplyRepSchema(BaseRepSchema):
    status = fields.String(required=True)
    timestamp = fields.DateTime(required=True)


# pki_enrolement_get_reply


class PkiEnrollmentGetReplyReqSchema(BaseReqSchema):
    certificate_id = fields.String(required=True)
    request_id = fields.String(required=True)


class PkiEnrollmentGetReplyRepSchema(BaseRepSchema):
    reply = fields.Nested(PkiReply.SCHEMA_CLS, Required=True)
    timestamp = fields.DateTime(Required=False)


# Serializer

pki_enrollment_request_serializer = None
pki_enrollment_request_req_serializer = MsgpackSerializer(PkiEnrollmentRequestReqSchema)

pki_enrollment_request_rep_serializer = MsgpackSerializer(PkiEnrollmentRequestRepSchema)

pki_enrollment_get_reply_serializer = CmdSerializer(
    PkiEnrollmentGetReplyReqSchema, PkiEnrollmentGetReplyRepSchema
)


pki_enrollment_get_requests_serializer = CmdSerializer(
    PkiEnrollmentGetRequestsReqSchema, PkiEnrollmentGetRequestsRepSchema
)

pki_enrollment_reply_serializer = MsgpackSerializer(
    PkiEnrollmentReplyReqSchema, PkiEnrollmentReplyRepSchema
)
