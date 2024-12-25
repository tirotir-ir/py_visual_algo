import matplotlib.pyplot as plt


def plot_sorting(data_gen, title="Sorting Visualization", speed=0.5):
    """
    Visualize sorting algorithm steps.

    Args:
        data_gen (generator): Generator yielding sorting steps (list of numbers).
        title (str): Title of the visualization.
        speed (float): Pause duration (in seconds) between updates.

    Displays a bar chart showing the sorting process in real time.
    """
    try:
        # Set up the interactive plot
        plt.ion()
        fig, ax = plt.subplots()
        ax.set_title(title)
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")

        for data in data_gen:
            ax.clear()
            ax.bar(range(len(data)), data, color="skyblue")
            ax.set_title(title)
            ax.set_xlabel("Index")
            ax.set_ylabel("Value")
            plt.pause(speed)

        plt.ioff()  # Turn off interactive mode
        plt.show()  # Display the final state

    except Exception as e:
        print(f"An error occurred during plotting: {e}")
        plt.close()  # Close the plot in case of errors
