from st2actions.runners.pythonrunner import Action
import requests

class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self.url = None
        self.headers = None

    def _headers(self):
        if not self.headers:
            api_token = self.config.get('api_token', None)

            if not api_token:
               raise ValueError('Missing "api_token" config option')
            else:
                self.headers = {
                    "Authorization": "Bearer {}".format(api_token)
                }

        return self.headers

    def _url(self):
        if not self.url:
            url = self.config.get('api_endpoint', None)

            if not url:
                raise ValueError('Missing "api_endpoint" config option')
            else:
                self.url = url

        return self.url

    def _get(self, endpoint):
        url = "{}{}".format(self._url(), endpoint)
        headers = self._headers()

        return requests.get(url, headers=headers)

    def _put(self, endpoint, params):
        url = "{}{}".format(self._url(), endpoint)
        headers = self._headers()

        return requests.put(url, data=params, headers=headers)