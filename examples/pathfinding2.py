import networkx as nx
import matplotlib.pyplot as plt
from py_visual_algo.algorithms.pathfinding import dijkstra, a_star

# Create a weighted graph using networkx
graph = nx.Graph()
graph.add_weighted_edges_from(
    [
        ("A", "B", 1),
        ("A", "C", 4),
        ("B", "C", 2),
        ("B", "D", 5),
        ("C", "D", 1),
        ("D", "E", 3),
    ]
)

# Define heuristic values for A* (straight-line distance to the goal)
heuristic = {
    "A": 7,
    "B": 6,
    "C": 2,
    "D": 1,
    "E": 0,
}


def visualize_graph(graph):
    """
    Visualize the graph using networkx and matplotlib.

    Args:
        graph (nx.Graph): The graph to visualize.
    """
    pos = nx.spring_layout(graph)  # Position nodes using the spring layout
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color="lightblue",
        font_weight="bold",
        node_size=700,
    )
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title("Graph Visualization")
    plt.show()


def run_dijkstra(graph, start):
    """
    Run Dijkstra's Algorithm on the graph.

    Args:
        graph (nx.Graph): The graph on which to run the algorithm.
        start (str): The starting node.

    Prints the current node and distances from the start node.
    """
    print("\nRunning Dijkstra's Algorithm:")
    generator = dijkstra(graph, start)
    for current_node, distances in generator:
        print(f"Current Node: {current_node}")
        for node, distance in distances.items():
            print(f"  {node}: {distance}")


def run_a_star(graph, start, goal, heuristic):
    """
    Run A* Algorithm on the graph.

    Args:
        graph (nx.Graph): The graph on which to run the algorithm.
        start (str): The starting node.
        goal (str): The target node.
        heuristic (dict): A dictionary mapping nodes to heuristic values.

    Prints the current node and f-scores during the algorithm's execution.
    """
    print("\nRunning A* Algorithm:")
    generator = a_star(graph, start, goal, heuristic)
    for current, f_score in generator:
        print(f"Current Node: {current}")
        for node, score in f_score.items():
            print(f"  {node}: {score}")


if __name__ == "__main__":
    # Starting and goal nodes
    start_node = "A"
    goal_node = "E"

    # Visualize the graph
    visualize_graph(graph)

    # Run Dijkstra's Algorithm
    run_dijkstra(graph, start_node)

    # Run A* Algorithm
    run_a_star(graph, start_node, goal_node, heuristic)
