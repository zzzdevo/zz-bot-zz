from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="✵ْ وەستانی کاتی ✵ْ",
            description=f"•⎆┊ وەستاندنی پەخشکردن بۆ ماوەیەکی کاتی♥•",
            thumb_url="https://telegra.ph/file/224b2f3de8d7f12bd4fec.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="✵ْ دەستپێکردنەوە ✵ْ",
            description=f"•⎆┊ دەستپێکردنەوەی پەخشکردن کاتێك وەستێنراوە♥•",
            thumb_url="https://telegra.ph/file/224b2f3de8d7f12bd4fec.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="✵ْ تێپەڕاندن ✵ْ",
            description=f"•⎆┊ تێپەڕاندنی گۆرانی یان ڤیدیۆی پەخشکراو بۆ پەخشێکی تر♥•",
            thumb_url="https://telegra.ph/file/224b2f3de8d7f12bd4fec.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="✵ْ وەستان ✵ْ",
            description="•⎆┊ کۆتایی هێنان بە پەخشکردن♥•",
            thumb_url="https://telegra.ph/file/224b2f3de8d7f12bd4fec.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="✵ْ تێکەڵکردن ✵ْ",
            description="•⎆┊ تێکەڵکردنی گۆرانییە ڕیزبەندەکان لە لیستی پەخشکردن♥•",
            thumb_url="https://telegra.ph/file/224b2f3de8d7f12bd4fec.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="✵ْ دووبارەکردنەوە ✵ْ",
            description="•⎆┊ دووبارە کردنەوەی گۆرانی♥•",
            thumb_url="https://telegra.ph/file/224b2f3de8d7f12bd4fec.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
