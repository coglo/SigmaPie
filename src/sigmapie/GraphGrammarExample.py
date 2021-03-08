from sigmapie.generators.no_lab_lab import generate_nll, no_lab_lab
from sigmapie.generators.no_fro_fro import generate_nff, no_fro_fro
from sigmapie.generators.no_high_high import generate_nhh, no_high_high
from sigmapie.generators.no_vc import generate_nvc, no_vc 
from sigmapie.generators.schwa_roundness import generate_sro, generate_sro_io, schwa_roundness, schwa_roundness_io
from sigmapie.generators.vowel_frontness import generate_vfr, generate_vfr_io, vowel_frontness, vowel_frontness_io
from sigmapie.GraphGrammar_class import GraphGrammar


def show_graph(data):
    graph_model = GraphGrammar(data)
    graph_model.write_dot()
    graph_model.plot_graph()
    return graph_model


# ipython   %pylab   g.plot_graph()
#show_graph(generate_nll(n=500, length=4))
g = show_graph(generate_nll(n=10000, length=4))
print(g.graph.edges, g.graph.nodes)