import re

from bs4 import BeautifulSoup
from langchain_community.document_loaders import RecursiveUrlLoader


def bs4_extractor(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    return re.sub(r"\n\n+", "\n\n", soup.text).strip()


if __name__ == '__main__':
    loader = RecursiveUrlLoader("https://profile.thebendu.link/",
                                max_depth=5,
                                extractor=bs4_extractor)

    i = 0
    for d in loader.lazy_load():
        if i == 5:
            break
        print(" ---- ", d.page_content, d.metadata)
        print("------------------------------------")
        i += 1
