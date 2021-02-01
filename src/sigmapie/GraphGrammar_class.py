import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import write_dot
from sigmapie.evaluators.vowel_frontness import evaluate_vfr_words
from sigmapie.generators.vowel_frontness import generate_vfr
from random import choice
from collections import Counter
from itertools import combinations, product

class GraphGrammar():
    """
    track the position of each node
    We can guess gramatical words not in the dictionary.
    it might be interesting to reverse the polarity of the graph
    """
    def __init__(self, data, max_word_length=6):
        self.graph = self.word_list_graph(data)
        self.alphabet = self._get_alphabet(data)
        self.restricted_pairs = self._get_restricted_pairs(data)
        self.max_word_length = max_word_length

    def _get_alphabet(self, data):
        alphabet = set()
        for word in data:
            alphabet.update(set(word))
        return alphabet
        
    def word_graph(self, graph, word):
        if graph is None:
            graph = nx.DiGraph()
        for i, character in enumerate(word):
            graph.add_node(character + "." + str(i))
        for i in range(len(word)-1):
            graph.add_edge(word[i] + "." + str(i), word[i+1] + "." + str(i+1))
        return graph

    def word_list_graph(self, word_list):
        graph = nx.DiGraph()
        for word in word_list:
            self.word_graph(graph, word)
        return graph

    def plot_graph(self):
        plt.subplot(121)
        nx.draw(self.graph, with_labels=True, font_weight='bold')


    '''
    def find_only_once(self, data):
        only_once = self.alphabet
        for word in data:
            only_once = only_once.difference({letter for letter, value in Counter(word).items() if value > 1})        
        return only_once

    def wordsegment_sets(self, data):
        return {set(word) for word in data}
    '''

    def _get_restricted_pairs(self, data):
        all_pairs = set(product(self.alphabet, repeat=2))
        found_pairs = set()
        for word in data:
            found_pairs.update(combinations(word,2))
        not_found_pairs = all_pairs - found_pairs
        return not_found_pairs


    def allowed_neighbors(self, nodes_so_far, neighbors, i):
        previous_nodes = []
        for neighbor in neighbors:
            previous_nodes.append(nodes_so_far + [neighbor])
        #possible_next = [nodes_so_far.append(neighbor) for neighbor in neighbors]
        allowed_ones = []
        for nodes in previous_nodes:
            if not set(combinations(nodes, 2)).intersection(self.restricted_pairs):
                allowed_ones.append(nodes[-1])
        return [node + '.' + str(i) for node in allowed_ones]

    def generate_word(self, length):
        root_nodes = [node for node in self.graph.nodes() if node[-1] == '0']
        nodes = [choice(root_nodes)]
        for i in range(1, length):
            # Add a comment here about neighbors and directed edges.
            neighbors = list(self.graph.neighbors(nodes[-1])) 
            if not neighbors:
                return "".join([node.split('.')[0] for node in nodes])
            allowed = self.allowed_neighbors([node.split('.')[0] for node in nodes], [neighbor.split('.')[0] for neighbor in neighbors], i)
            if not allowed:
                return "".join([node.split('.')[0] for node in nodes])
            next_node = choice(allowed)
            nodes.append(next_node)
        return "".join([node.split('.')[0] for node in nodes])

    """ 
    def generate_word(self, length):
        root_nodes = [node for node in self.graph.nodes() if node[-1] == '0']
        nodes = [choice(root_nodes)]
        for i in range(length-1):
            for node in nodes:
                for pair in not_found_pairs:
                    if node in not_found_pairs:
            # Add a comment here about neighbors and directed edges.
                    neighbors = list(self.graph.neighbors(nodes[-1]))) 
                if not neighbors:
                    return "".join([node[0] for node in nodes])
            next_node = choice(neighbors)
            nodes.append(next_node)
        return "".join([node[0] for node in nodes])
    """

    def generate_sample(self, n):
        return [self.generate_word(self.max_word_length) for i in range(n)]

    def write_dot(self, path="graph.dot"):
        write_dot(self.graph, path)
    
    def percent_grammatical(self, wordlist):
        return sum([self.gramatical(word) for word in wordlist]) * 100/len(wordlist)

    def gramatical(self, word):
        for i in range(len(word)-1):
            if (word[i]+ "." + str(i), word[i+1]+ "." + str(i+1)) not in self.graph.edges:
                return False
        return True