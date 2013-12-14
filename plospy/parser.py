from BeautifulSoup import BeautifulSoup


class PlosXml:
    def __init__(self, path):
        self.raw = None
        with open(path, 'rb') as f:
            self.raw = f.read()

        self.xml = BeautifulSoup(self.raw)
        docs_list = self.xml.findAll('doc')

        self.docs = []

        for doc in docs_list:
            doc_dict = {}
            children = doc.findChildren()

            identifiers = []
            for child in children:
                try:
                    identifiers = identifiers + [child['name']]
                except KeyError:
                    continue

            for ident in identifiers:
                contents = doc.find(True, {'name': ident}).contents
                contents = [str(cont).replace('<str>', '').
                            replace('</str>', '') for cont in contents]
                doc_dict[ident] = contents

            self.docs = self.docs + [doc_dict]
