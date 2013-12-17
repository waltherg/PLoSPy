from lxml import etree


class PlosXml:
    def __init__(self, path):
        self.raw = None
        
        self.xml = etree.parse(path)

        docs_list = self.xml.xpath('//*[self::doc]')

        self.docs = []

        for doc in docs_list:
            doc_dict = {}
            children = list(doc)
            identifiers = []
            for child in children:
                name = child.attrib['name']
                content = child.text
                doc_dict[name] = content

            self.docs = self.docs + [doc_dict]
