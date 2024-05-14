import tkinter as tk
from tkinter import ttk
from geopy.distance import geodesic
import requests


def get_coordinates(address):
    """
    Fetches the geographic coordinates (latitude and longitude) for a given address using the Nominatim API.

    Parameters:
    address (str): The address to geocode.

    Returns:
    tuple: A tuple containing the latitude and longitude of the address, or None if the address could not be found.
    """
    # URL for the Nominatim API with the address query
    url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json"
    # Send a GET request to the Nominatim API
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        if data:
            # Extract latitude and longitude from the first result
            lat = float(data[0]['lat'])
            lon = float(data[0]['lon'])
            return (lat, lon)
    return None


def calculate_distance():
    """
    Calculates the geodesic distance between the start and end locations entered by the user.
    Fetches the coordinates for each location and updates the result label with the distance in kilometers.
    """
    # Get the user input from the entry widgets
    start_location = start_entry.get()
    end_location = end_entry.get()

    # Fetch coordinates for the start and end locations
    start_coords = get_coordinates(start_location)
    end_coords = get_coordinates(end_location)

    if start_coords and end_coords:
        # Calculate the geodesic distance between the coordinates
        distance = geodesic(start_coords, end_coords).kilometers
        # Update the result label with the calculated distance
        result_label.config(text=f"Distance: {distance:.2f} km")
    else:
        # Display an error message if the coordinates could not be fetched
        result_label.config(text="Invalid locations provided or API error")


def switch_points():
    """
    Switches the values between the start and end location entry widgets.
    """
    # Get the current values from the entry widgets
    start_location = start_entry.get()
    end_location = end_entry.get()
    # Swap the values in the entry widgets
    start_entry.delete(0, tk.END)
    start_entry.insert(0, end_location)
    end_entry.delete(0, tk.END)
    end_entry.insert(0, start_location)


# Create the main application window
root = tk.Tk()
root.title("Distance Calculator")

# Create and position the start location label and entry widget
ttk.Label(root, text="Start Location:").grid(column=0, row=0, padx=10, pady=10)
start_entry = ttk.Entry(root, width=30)
start_entry.grid(column=1, row=0, padx=10, pady=10)

# Create and position the switch button between the start and end location entry widgets
switch_button = ttk.Button(root, text="Switch", command=switch_points)
switch_button.grid(column=2, row=0, padx=10, pady=10)

# Create and position the end location label and entry widget
ttk.Label(root, text="End Location:").grid(column=0, row=1, padx=10, pady=10)
end_entry = ttk.Entry(root, width=30)
end_entry.grid(column=1, row=1, padx=10, pady=10)

# Create and position the calculate distance button
calculate_button = ttk.Button(root, text="Calculate Distance", command=calculate_distance)
calculate_button.grid(column=0, row=2, columnspan=3, pady=20)

# Create and position the result label to display the calculated distance
result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=3, columnspan=3, pady=10)

# Create and position the exit button to close the application
exit_button = ttk.Button(root, text="Exit", command=root.quit)
exit_button.grid(column=0, row=4, columnspan=3, pady=10)

# Start the Tkinter event loop to run the application
root.mainloop()
