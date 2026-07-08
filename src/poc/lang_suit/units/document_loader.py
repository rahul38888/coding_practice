from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders.pdf import PyPDFLoader


if __name__ == '__main__':

    print("CSV loader ----------------")
    loader = CSVLoader("./data/episodes.csv")
    data = loader.load()

    for d in data:
        print(" ---- ", d.page_content, "\n", d.metadata)

    print("\n\n\n\nPDF loader ----------------")
    loader = PyPDFLoader("./data/Hamlet.pdf")
    data = loader.load()

    for d in data:
        print(" ---- ", d.page_content, d.metadata)
