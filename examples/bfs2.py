import networkx as nx
from py_visual_algo.algorithms.graph import bfs_with_edges
import matplotlib.pyplot as plt


def create_graph():
    """
    Create a sample graph for demonstration.
    """
    graph = nx.Graph()
    graph.add_edges_from(
        [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F"), ("E", "G")]
    )
    return graph


def visualize_graph(graph, edges=None, nodes=None, highlight_node=None):
    """
    Visualize the graph with optional highlighting of edges and nodes.
    """
    pos = nx.spring_layout(graph)

    # Draw the base graph
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", font_weight="bold")

    # Highlight specific edges
    if edges:
        nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color="red", width=2)

    # Highlight specific nodes
    if nodes:
        nx.draw_networkx_nodes(graph, pos, nodelist=nodes, node_color="orange")

    # Highlight the current node
    if highlight_node:
        nx.draw_networkx_nodes(
            graph, pos, nodelist=[highlight_node], node_color="green"
        )

    plt.show()


def run_bfs_example():
    """
    Run the BFS example, visualize the traversal, and log each step.
    """
    graph = create_graph()
    start_node = "A"

    print(f"Running BFS from node: {start_node}")
    generator = bfs_with_edges(graph, start=start_node)

    for step, output in enumerate(generator):
        if isinstance(output[0], tuple):  # Edge traversal
            edges = output
            print(f"Step {step + 1}: Traversed edges: {edges}")
            visualize_graph(graph, edges=edges)
        else:  # Node visitation
            nodes = output
            print(f"Step {step + 1}: Visited nodes: {nodes}")
            visualize_graph(graph, nodes=nodes)


if __name__ == "__main__":
    run_bfs_example()
