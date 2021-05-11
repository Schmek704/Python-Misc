# Need to ensure the watsoncred.py file is created, and the ibm libraries are installed 

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from watsoncred import api_key, api_url

# Authenticator/API Credentials#
authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version = '2021-04-19',
    authenticator = authenticator
)
language_translator.set_service_url(api_url)

# English to French Translator #
def englishtofrench(text):
    if text == "":
        return print("Nothing to translate")
    result = language_translator.translate(
        text = text,
        model_id = 'en-fr'
    ).get_result()
    full_result = result.get('translations')
    translated_text_dict = full_result[0]
    translated_text = translated_text_dict.get('translation')
    return print(translated_text)

# English to German Translator #
def englishtogerman(text):
    if text == "":
        return print("Nothing to translate")
    result = language_translator.translate(
        text = text,
        model_id = 'en-de'
    ).get_result()
    full_result = result.get('translations')
    translated_text_dict = full_result[0]
    translated_text = translated_text_dict.get('translation')
    return print(translated_text)
