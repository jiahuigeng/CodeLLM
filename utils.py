import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://numpy.org/doc/stable/reference/generated/numpy.bitwise_count.html"


def numpy_crawler(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the title of the page
        title = soup.title.string
        print(f"Page Title: {title}")
        
        to_remove = ['col-lg-9 navbar-header-items', "sidebar-primary-items__start sidebar-primary__section", "bd-footer__inner bd-page-width", "sidebar-secondary-item"]
        
        # for item in to_remove:
        #     div_to_remove = soup.find('div', class_=item)
            
        # print(soup.text)
        div_to_remove = soup.find("div", class_="sidebar-primary-items__start sidebar-primary__section")
        if div_to_remove:
            div_to_remove.decompose() 
        
            
        div_to_remove = soup.find('div', class_="bd-footer__inner bd-page-width")
        if div_to_remove:
            div_to_remove.decompose() 
            
        div_to_remove = soup.find('div', class_="sidebar-secondary-item")
        if div_to_remove:
            div_to_remove.decompose() 
            
        div_to_remove = soup.find('div', class_="bd-header__inner bd-page-width")
        if div_to_remove:
            div_to_remove.decompose() 
            
        div_to_remove = soup.find('div', class_="prev-next-area")
        if div_to_remove:
            div_to_remove.decompose()  
            
        text = soup.text
        to_remove_words = ["NumPy reference", "Skip to main content", "Back to top", "Mathematical functions",
                        "API reference", "Development", "Release notes", "Learn", "NEPs", "Miscellaneous routines",
                        "Ctrl+K", "User Guide", "Building from source", "GitHub"]
        for item in to_remove_words:
            text = text.replace(item, "")
        text = text.split("\n")
        text = [item.strip() for item in text if item.strip()]
        text = "\n".join(text)
        print(text) 

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        text = ""
        
    return text

    





# if __name__ == "__main__":
    
#     page_url = "https://numpy.org/doc/stable/reference/generated/numpy.bitwise_count.html"