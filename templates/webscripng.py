# import requests

# cookies = {
#     'HAB_Var': 'Apothecary',
#     'HAB_XDI': 'Apothecary',
#     '_cg': '4000',
#     'X-Default-City': '1',
#     'X-Pincode': '400001',
#     'pe_utm_source': 'google',
#     'XdI': '9d05deafb420047365184e5780a70b54',
#     '_gcl_au': '1.1.2086274472.1699101362',
#     'utmsourcesession': 'google',
#     '_gid': 'GA1.2.238728407.1699101362',
#     'WZRK_G': '6f96ffe7bc13483389a9fd87c78dece7',
#     '_fbp': 'fb.1.1699101367419.1688320650',
#     'dtm_token_sc': 'AAAL-JjDigEJ4wBGAesuAAAAAAE',
#     'dtm_token': 'AAAL-JjDigEJ4wBGAesuAAAAAAE',
#     'pe_utm_data': '%7B%22isSEM%22%3A%22true%22%2C%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22GSB_New_CX_FP%22%2C%22utm_adgroup%22%3A%22OTC_Healthcare%22%2C%22gclid%22%3A%22CjwKCAjw15eqBhBZEiwAbDomEnZm69AK6M_bG_MzashwP-u-Kwct2Iza0SXLPcosXg9zwd0soZmezBoCHWoQAvD_BwE%22%7D',
#     'XPESD': '%7B%22session_id%22%3A%22s_w_6f96ffe7bc13483389a9fd87c78dece7_1699103387000%22%2C%22session_id_flag%22%3A%22ct_id%22%2C%22media_source%22%3A%22google%22%2C%22campaign%22%3A%22GSB_New_CX_FP%22%2C%22gclid%22%3A%22CjwKCAjw15eqBhBZEiwAbDomEnZm69AK6M_bG_MzashwP-u-Kwct2Iza0SXLPcosXg9zwd0soZmezBoCHWoQAvD_BwE%22%2C%22medium%22%3A%22cpc%22%2C%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm_adgroup%22%3A%22OTC_Healthcare%22%2C%22session_start_time%22%3A%222023-11-04T13%3A09%3A47.022Z%22%7D',
#     'XPESS_v2': 's_w_6f96ffe7bc13483389a9fd87c78dece7_1699103387000',
#     'XPEINTID': '1699103389610',
#     '_gcl_aw': 'GCL.1699103406.CjwKCAjw15eqBhBZEiwAbDomEnZm69AK6M_bG_MzashwP-u-Kwct2Iza0SXLPcosXg9zwd0soZmezBoCHWoQAvD_BwE',
#     '_ga_J4XE9SW84F': 'GS1.1.1699101362.1.1.1699103406.40.0.0',
#     '_uetsid': 'b6d2f8e07b0e11ee906283a1fb749e4c',
#     '_uetvid': 'b6d329907b0e11ee9e84733f666fc530',
#     '_ga': 'GA1.2.476845178.1699101362',
#     '_gac_UA-60621013-1': '1.1699103407.CjwKCAjw15eqBhBZEiwAbDomEnZm69AK6M_bG_MzashwP-u-Kwct2Iza0SXLPcosXg9zwd0soZmezBoCHWoQAvD_BwE',
#     '_ga_YLL6W14B3J': 'GS1.2.1699101362.1.1.1699103407.0.0.0',
#     '_ga_XJY1F0EN7Z': 'GS1.2.1699101362.1.1.1699103407.40.0.0',
#     'WZRK_S_R9Z-WWR-854Z': '%7B%22p%22%3A5%2C%22s%22%3A1699101363%2C%22t%22%3A1699103452%7D',
# }

# headers = {
#     'authority': 'pharmeasy.in',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
#     'cache-control': 'max-age=0',
#     # 'cookie': 'HAB_Var=Apothecary; HAB_XDI=Apothecary; _cg=4000; X-Default-City=1; X-Pincode=400001; pe_utm_source=google; XdI=9d05deafb420047365184e5780a70b54; _gcl_au=1.1.2086274472.1699101362; utmsourcesession=google; _gid=GA1.2.238728407.1699101362; WZRK_G=6f96ffe7bc13483389a9fd87c78dece7; _fbp=fb.1.1699101367419.1688320650; dtm_token_sc=AAAL-JjDigEJ4wBGAesuAAAAAAE; dtm_token=AAAL-JjDigEJ4wBGAesuAAAAAAE; pe_utm_data=%7B%22isSEM%22%3A%22true%22%2C%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22GSB_New_CX_FP%22%2C%22utm_adgroup%22%3A%22OTC_Healthcare%22%2C%22gclid%22%3A%22CjwKCAjw15eqBhBZEiwAbDomEnZm69AK6M_bG_MzashwP-u-Kwct2Iza0SXLPcosXg9zwd0soZmezBoCHWoQAvD_BwE%22%7D; XPESD=%7B%22session_id%22%3A%22s_w_6f96ffe7bc13483389a9fd87c78dece7_1699103387000%22%2C%22session_id_flag%22%3A%22ct_id%22%2C%22media_source%22%3A%22google%22%2C%22campaign%22%3A%22GSB_New_CX_FP%22%2C%22gclid%22%3A%22CjwKCAjw15eqBhBZEiwAbDomEnZm69AK6M_bG_MzashwP-u-Kwct2Iza0SXLPcosXg9zwd0soZmezBoCHWoQAvD_BwE%22%2C%22medium%22%3A%22cpc%22%2C%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm_adgroup%22%3A%22OTC_Healthcare%22%2C%22session_start_time%22%3A%222023-11-04T13%3A09%3A47.022Z%22%7D; XPESS_v2=s_w_6f96ffe7bc13483389a9fd87c78dece7_1699103387000; XPEINTID=1699103389610; _gcl_aw=GCL.1699103406.CjwKCAjw15eqBhBZEiwAbDomEnZm69AK6M_bG_MzashwP-u-Kwct2Iza0SXLPcosXg9zwd0soZmezBoCHWoQAvD_BwE; _ga_J4XE9SW84F=GS1.1.1699101362.1.1.1699103406.40.0.0; _uetsid=b6d2f8e07b0e11ee906283a1fb749e4c; _uetvid=b6d329907b0e11ee9e84733f666fc530; _ga=GA1.2.476845178.1699101362; _gac_UA-60621013-1=1.1699103407.CjwKCAjw15eqBhBZEiwAbDomEnZm69AK6M_bG_MzashwP-u-Kwct2Iza0SXLPcosXg9zwd0soZmezBoCHWoQAvD_BwE; _ga_YLL6W14B3J=GS1.2.1699101362.1.1.1699103407.0.0.0; _ga_XJY1F0EN7Z=GS1.2.1699101362.1.1.1699103407.40.0.0; WZRK_S_R9Z-WWR-854Z=%7B%22p%22%3A5%2C%22s%22%3A1699101363%2C%22t%22%3A1699103452%7D',
#     'referer': 'https://www.google.com/',
#     'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Linux"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
# }

# params = {
#     'isSEM': 'true',
#     'utm_source': 'google',
#     'utm_medium': 'cpc',
#     'utm_campaign': 'GSB_New_CX_FP',
#     'utm_adgroup': 'OTC_Healthcare',
#     'gclid': 'CjwKCAjw15eqBhBZEiwAbDomEnZm69AK6M_bG_MzashwP-u-Kwct2Iza0SXLPcosXg9zwd0soZmezBoCHWoQAvD_BwE',
# }

# response = requests.get('https://pharmeasy.in/online-medicine-order', params=params, cookies=cookies, headers=headers)
# import requests 
  
# # Scrapes the words from the URL below and stores  
# # them in a list 
# def getWords(): 
  
#     # contains about 2500 words 
#     # url = 'https://pharmeasy.in/online-medicine-order'
#     fetchData = requests.get(response) 
  
#     # extracts the content of the webpage 
#     wordList = fetchData.content 
  
#     # decodes the UTF-8 encoded text and splits the  
#     # string to turn it into a list of words 
#     wordList = wordList.decode("utf-8").split() 
  
#     return wordList 
  
  
# # function to determine whether a word is ordered or not 
# def isOrdered(): 
  
#     # fetching the wordList 
#     collection = getWords() 
  
#     # since the first few of the elements of the  
#     # dictionary are numbers, getting rid of those 
#     # numbers by slicing off the first 17 elements 
#     collection = collection[16:] 
#     word = '' 
  
#     for word in collection: 
#         result = 'Word is ordered'
#         i = 0
#         l = len(word) - 1
  
#         if (len(word) < 3): # skips the 1 and 2 lettered strings 
#             continue
  
#         # traverses through all characters of the word in pairs 
#         while i < l:          
#             if (ord(word[i]) > ord(word[i+1])): 
#                 result = 'Word is not ordered'
#                 break
#             else: 
#                 i += 1
  
#         # only printing the ordered words 
#         if (result == 'Word is ordered'): 
#             print(word,': ',result) 
  
  
# # execute isOrdered() function 
# if __name__ == '__main__': 
#     isOrdered() 
    

string="the broad road street "
if string==True:
    string[2]="rd"
    print(string)
