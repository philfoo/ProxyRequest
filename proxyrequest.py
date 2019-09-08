import random
import requests
from datetime import timedelta
from datetime import datetime

from lxml import html

_PROXY_SOURCES_URL = ["https://www.us-proxy.org",
                      "https://www.sslproxies.org",
                      "https://free-proxy-list.net/anonymous-proxy.html"]

_USER_AGENT_SOURCE_URL = "https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome"
_MAX_NUM_TRIES = 10

class ProxyRequest:
    def __init__(self, proxyRefreshTime=600, requestTimeout=5):
        self.lastProxyUpdate = None
        self.userAgentList = []
        self.proxyList = set()

        # In seconds
        self.proxyRefreshTime = proxyRefreshTime
        self.requestTimeout = requestTimeout


    def makeProxyRequest(self, url):
        numTries = 0

        while numTries < _MAX_NUM_TRIES:
            try:
                proxy = self.getRandomProxy()
                proxyDict = {"https": proxy}

                userAgent = self.getRandomUserAgent()
                headers = {"User-Agent": userAgent}

                response = requests.get(url,
                                        headers=headers,
                                        proxies=proxyDict,
                                        timeout=self.requestTimeout)

                if response.status_code == 200:
                    return response

                else:
                    print("Unsuccessful response code, trying again", response)

            except Exception as e:
                print("Error occurred during request, trying again", e)

            numTries += 1

    def getRandomProxy(self):
        minimumUpdateTime = datetime.now() - timedelta(seconds=self.proxyRefreshTime)

        if self.lastProxyUpdate is None or self.lastProxyUpdate < minimumUpdateTime:
            self.refreshProxyList()

        if len(self.proxyList) <= 0:
            return None

        # Sample method used to get random element from set
        return random.sample(self.proxyList, 1)[0]


    def refreshProxyList(self):
        print("REFRESHING PROXY LIST")
        self.proxyList.clear()

        for proxySource in _PROXY_SOURCES_URL:
            response = requests.get(proxySource)
            htmlTree = html.fromstring(response.content)

            for i in htmlTree.xpath('//tbody/tr')[:20]:
                # Proxy is https and located in US
                if i.xpath('.//td[7][contains(text(),"yes")]') and \
                   i.xpath('.//td[4][contains(text(), "United States")]'):

                    #Grab IP and corresponding PORT
                    proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                    self.proxyList.add("https://"+ proxy)

        self.lastProxyUpdate = datetime.now()


    def getRandomUserAgent(self):
        if len(self.userAgentList) <= 0:
            self.refreshUserAgentList()

        return random.choice(self.userAgentList)


    def refreshUserAgentList(self):
        print("REFRESHING USER AGENT LIST")

        response = requests.get(_USER_AGENT_SOURCE_URL)
        htmlTree = html.fromstring(response.content)

        for i in htmlTree.xpath('//tbody/tr')[:3]:
            userAgent = i.xpath('.//td[2]/span/text()')[0]
            self.userAgentList.append(userAgent)
