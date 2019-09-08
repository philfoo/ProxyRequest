from proxyrequest import ProxyRequest

_TEST_URLS = [
"https://www.amazon.com/gp/product/B00V2JMUHY?pf_rd_p=183f5289-9dc0-416f-942e-e8f213ef368b&pf_rd_r=8MMT2PXM0N81T959EXYH",

"https://www.amazon.com/dp/B07TCHVBZF/ref=sspa_dk_detail_3?psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExODdQNlo2UlFIQkMwJmVuY3J5cHRlZElkPUEwMTI3Nzk1MkRMUFk3NExFMUI3RSZlbmNyeXB0ZWRBZElkPUEwNDgzNTIzMklNTzNFTVRFSEZXMiZ3aWRnZXROYW1lPXNwX2RldGFpbDImYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl",

"https://www.uniqlo.com/us/en/men-dry-stretch-sweat-full-zip-hoodie-413436.html?dwvar_413436_color=COL03&cgid=men-sweatshirts-and-sweatpants#start=2&cgid=men-sweatshirts-and-sweatpants",

"https://www.gap.com/browse/product.do?pid=496157032&cid=80811&pcid=80799&grid=productSearch_1_56_1#pdp-page-content"]

prxyReq = ProxyRequest()

for url in _TEST_URLS:
    response = prxyReq.makeProxyRequest(url)
    print(response)
