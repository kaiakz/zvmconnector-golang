import docutils.nodes
import docutils.parsers.rst
import docutils.utils
import docutils.core

rst_path = "./source/restapi.copy.rst"

# def parse_rst(text: str) -> docutils.nodes.document:
#     parser = docutils.parsers.rst.Parser()
#     components = (docutils.parsers.rst.Parser,)
#     settings = docutils.frontend.OptionParser(components=components).get_default_values()
#     settings.pep_references = None
#     settings.rfc_references = None
#     document = docutils.utils.new_document('<restapi>', settings=settings)
#     parser.parse(text, document)
#     return document


f = open(rst_path, "r")
# text = f.read()
# f.close()
# doc = parse_rst(text)
# visitor = MyVisitor(doc)
# doc.walk(visitor)
# print(doc)

document = docutils.core.publish_doctree(f.read())
# print(document)
nodes = list(document)
description = ''
# f.close()
# f=open("result.txt","w")
# f.write(str(document))

# for node in nodes:
#     if str(node).startswith('<topic classes="contents"'):
#         break
#     if type(node) is docutils.nodes.comment\
#     or type(node) is docutils.nodes.title:
#         continue
#     if type(node) is docutils.nodes.:
#         description += node.astext() + '\n'

# print(nodes)
# print(description)

def make_golang_func(api: str) -> str:
    return api.title().replace(" ", "")

Part = ['Version', 'Guest(s)', 'Host', 'Image(s)', 'VSwitch', 'Files']

class MyVisitor(docutils.nodes.NodeVisitor):

    f = None
    current = None
    l = {}

    def File(self, f):
        self.f = f

    # def visit_literal_block(self, node: docutils.nodes.reference) -> None:
    #     f.write(node.astext())

    # def visit_paragraph(self, node: docutils.nodes.reference) -> None:
    #     f.write(node.astext() + "\n")

    def visit_list_item(self, node: docutils.nodes.Node) -> None:
        print(node.astext())

    def visit_title(self, node: docutils.nodes.Node) -> None:
        s = node.astext()
        if s not in Part:
            self.current = s
            print(make_golang_func(s))

    def visit_strong(self, node: docutils.nodes.Node) -> None:
        self.l[self.current] = node.astext()
        print(node.astext())

    def unknown_visit(self, node: docutils.nodes.Node) -> None:
        """Called for all other node types."""
        pass

    def close(self):
        # print(self.l)
        return


v = MyVisitor(document)
f = open("result.txt","w")
v.File(f)
document.walk(v)
v.close()
f.close()

f = open("origin.html", "w")
f.write(str(document))
f.close()