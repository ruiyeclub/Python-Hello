from googletrans import Translator


def translate_text(text, dest_language):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text


# 示例：将中文翻译成英语
chinese_text = "你好，世界"
translated_text_en = translate_text(chinese_text, 'en')
print(f"中文: {chinese_text}")
print(f"英文: {translated_text_en}")

# 示例：将中文翻译成法语
translated_text_fr = translate_text(chinese_text, 'fr')
print(f"法语: {translated_text_fr}")
