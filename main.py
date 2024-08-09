import networkx as nx
import matplotlib.pyplot as plt


def create_graph_from_links(links):
    """
    Creates and displays a graph from a list of links. Also checks if the graph is connected.

    :param links: A list of tuples where each tuple represents a link between two nodes.
    """
    # Create a new graph
    G = nx.Graph()

    # Add edges to the graph from the links
    for link in links:
        G.add_edge(*link)

    # Check if the graph is connected
    is_connected = nx.is_connected(G)
    print(f"Is the graph connected? {'Yes' if is_connected else 'No'}")

    # Draw the graph
    nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700)
    plt.show()


# Example usage
if __name__ == "__main__":
    # Define a series of links (edges) between nodes
    links = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]

    create_graph_from_links(links)
