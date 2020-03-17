import docutils.nodes
import docutils.parsers.rst
import docutils.utils
import docutils.core

rst_path = "./source/restapi.rst"

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

class MyVisitor(docutils.nodes.NodeVisitor):

    f = None

    def File(self, f):
        self.f = f

    # def visit_literal_block(self, node: docutils.nodes.reference) -> None:
    #     f.write(node.astext())

    def visit_paragraph(self, node: docutils.nodes.reference) -> None:
        l = ['No directive entry for "restapi_parameters" in module "docutils.parsers.rst.languages.en".','Trying "restapi_parameters" as canonical directive name.','Unknown directive type "restapi_parameters".']
        s = node.astext()
        if s not in l:
            f.write(s + "\n")

    def visit_title(self, node: docutils.nodes.reference) -> None:
        print(node.astext())

    # def visit_strong(self, node: docutils.nodes.reference) -> None:
    #     print(node.astext())

    def unknown_visit(self, node: docutils.nodes.reference) -> None:
        """Called for all other node types."""
        pass


vt = MyVisitor(document)
f = open("result.txt","w")
vt.File(f)
document.walk(vt)
f.close()

f = open("origin.html", "w")
f.write(str(document))
f.close()