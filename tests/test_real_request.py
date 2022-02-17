import os

DEV_UP_ACCESS_KEY = os.environ.get('DEV_UP_ACCESS_KEY')
SPEECH_URL = "https://psv4.userapi.com/c533532//u460908267/audiomsg/d2/3de99000be.mp3"

# @pytest.mark.asyncio
# async def test_audio_speech():
#     _api = DevUpAPI(access_token=DEV_UP_ACCESS_KEY)
#
#     speech_response = await _api.audio.speech(SPEECH_URL)
#     assert speech_response.__class__ == models.AudioSpeechResponse
#     await _api.close()
#
#
# @pytest.mark.asyncio
# async def test_check_link():
#     _api = DevUpAPI(access_token=DEV_UP_ACCESS_KEY)
#     utils_check_link = await _api.utils.check_link()
#     assert utils_check_link.__class__ == models.UtilsCheckLinkResponse
#     await _api.close()
#
#
# @pytest.mark.asyncio
# async def test_create_short_link():
#     _api = DevUpAPI(access_token=DEV_UP_ACCESS_KEY)
#     utils_create_short_link = await _api.utils.create_short_link("https://fbhecosystem.ru")
#     assert utils_create_short_link.__class__ == models.UtilsCreateShortLinkResponse
#     await _api.close()
#
#
# @pytest.mark.asyncio
# async def test_get_server_time():
#     _api = DevUpAPI(access_token=DEV_UP_ACCESS_KEY)
#     utils_get_server_time = await _api.utils.get_server_time()
#     assert utils_get_server_time.__class__ == models.UtilsGetServerTimeResponse
#     await _api.close()
#
#
# @pytest.mark.asyncio
# async def test_get_server_time():
#     _api = DevUpAPI(access_token=DEV_UP_ACCESS_KEY)
#     utils_get_web_info = await _api.utils.get_web_info("https://fbhecosystem.ru")
#     assert utils_get_web_info.__class__ == models.UtilsGetWebInfoResponse
#     await _api.close()
#
#
# @pytest.mark.asyncio
# async def test_utils_md5_generate():
#     _api = DevUpAPI(access_token=DEV_UP_ACCESS_KEY)
#     utils_md5_generate = await _api.utils.md5_generate("111")
#     assert utils_md5_generate.__class__ == models.UtilsMD5GenerateResponse
#     await _api.close()
