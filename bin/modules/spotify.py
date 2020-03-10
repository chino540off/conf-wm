import requests

# (curl -X GET https://api.spotify.com/v1/me/player/currently-playing \
#    -H "Accept: application/json" \
#    -H "Content-Type: application/json" \
#    -H "Authorization: Bearer BQDEEYATcy9Si7uisaiXCjKRP93b0FfWNisquOhihJIqoSRFN1FZ3vzKWpn9FlqMtr2DiQZ75pQUO-6kiN6c4mqzRYM3D96B-F_fokccS-HOF8_pEyThAELTU3GiFDNi2BY6wQKwxs7-hMjV7gTKfQ"


class Module:
    def __init__(self):
        self._url = "https://api.spotify.com/v1/me/player/currently-playing"
        self._headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer BQDY8-74G-qySySkUaUEqqdBPKzBQikN3wcaLi_RshORskDxglp5AEw8OhsWNLRLGbXiQr-v5fLlxOD1sOZQZ6bH5ppgpYm_CckyW0ShhWvIOJHu8yM9X6_cKx4rln044aJl5UnYukYI1uPwVAelYA",
        }

    def get_data(self):
        # resp = requests.get(url=self._url, headers=self._headers)
        # data = resp.json()
        # print(data)
        # song = data["item"]["name"]
        song = "FIXME"
        return {"full_text": "%s - " % (song), "name": "spotify", "color": "#1ED760"}
