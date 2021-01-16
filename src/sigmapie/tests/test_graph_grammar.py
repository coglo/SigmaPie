import networkx as nx
from networkx.drawing.nx_agraph import write_dot
from sigmapie.evaluators.vowel_frontness import evaluate_vfr_words
from sigmapie.generators.vowel_frontness import generate_vfr
from random import choice

class GraphGrammar():
    """
    track the position of each node
    We can guess gramatical words not in the dictionary.
    it might be interesting to reverse the polarity of the graph
    """
    def __init__(self, data, max_word_length=6):
        self.graph = self.word_list_graph(data)
        self.max_word_length = max_word_length

    def word_graph(self, graph, word):
        if graph is None:
            graph = nx.DiGraph()
        for i, character in enumerate(word):
            graph.add_node(character + str(i))
        for i in range(len(word)-1):
            graph.add_edge(word[i]+str(i), word[i+1]+str(i+1))
        return graph

    def word_list_graph(self, word_list):
        graph = nx.DiGraph()
        for word in word_list:
            self.word_graph(graph, word)
        return graph

    def generate_word(self, length):
        root_nodes = [node for node in self.graph.nodes() if node[-1] == '0']
        nodes = [choice(root_nodes)]
        
        for i in range(length-1):
            # Add a comment here about neighbors and directed edges.
            neighbors = list(self.graph.neighbors(nodes[-1]))
            if not neighbors:
                return "".join([node[0] for node in nodes])
            nodes.append(choice(neighbors))
        return "".join([node[0] for node in nodes])
        
    def generate_sample(self, n):
        return [self.generate_word(self.max_word_length) for i in range(n)]
    
    def acceptable(self, word):
        for i in range(len(word)-1):
            if (word[i]+str(i), word[i+1]+str(i+1)) not in self.graph.edges:
                return False
        return True


   ''' 
    def future_word(self, length):
        #using gradient grammar to predict future words might be better, find the new words in last 50 years and check their entropy.
        word = self.generate_word(self.max_word_length)
        if word in 
    '''


def evaluate_example(evaluator, data):
    graph_model = GraphGrammar(data)
    evaluator(data)
    evaluator(graph_model.generate_sample(1000))
  

def test_vowel_frontness():
    data =  generate_vfr(n=1000)
    evaluate_example(evaluate_vfr_words, data)