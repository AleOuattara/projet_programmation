try:
    from surf_scrape.wget import wget_data
except ModuleNotFoundError:
    #import pip
    #pip.main(["install", "surf_scrape"])
    from surf_scrape.wget import wget_data

def load_data(url, link=None):
    if type(url) == type(None):
        url = "https://www.surf-report.com/meteo-surf/lacanau-s1043.html"
    wget_data(url, link)
    
    
# import sys
# sys.path.append("/path/to/your/custom/library")