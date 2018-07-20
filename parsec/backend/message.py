from parsec.utils import to_jsonb64
from parsec.schema import BaseCmdSchema, fields


class _cmd_NEW_Schema(BaseCmdSchema):
    recipient = fields.String(required=True)
    body = fields.Base64Bytes(required=True)


cmd_NEW_Schema = _cmd_NEW_Schema()


class _cmd_GET_Schema(BaseCmdSchema):
    # TODO: accept negative offset to fetch only last message ?
    offset = fields.Integer(missing=0)


cmd_GET_Schema = _cmd_GET_Schema()


class BaseMessageComponent:
    async def perform_message_new(self, sender_device_id, recipient_user_id, body):
        raise NotImplementedError()

    async def perform_message_get(self, recipient_user_id, offset):
        raise NotImplementedError()

    async def api_message_new(self, client_ctx, msg):
        msg = cmd_NEW_Schema.load_or_abort(msg)
        await self.perform_message_new(
            sender_device_id=client_ctx.id, recipient_user_id=msg["recipient"], body=msg["body"]
        )
        return {"status": "ok"}

    async def api_message_get(self, client_ctx, msg):
        msg = cmd_GET_Schema.load_or_abort(msg)
        offset = msg["offset"]
        messages = await self.perform_message_get(client_ctx.user_id, offset)
        return {
            "status": "ok",
            "messages": [
                {"count": i, "body": to_jsonb64(data[1]), "sender_id": data[0]}
                for i, data in enumerate(messages, offset + 1)
            ],
        }
