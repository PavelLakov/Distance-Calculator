
# Distance Calculator

This is a simple Tkinter-based GUI application that calculates the distance between two locations. Users can input start and end locations, and the application fetches the geographic coordinates for these locations using the Nominatim API. It then calculates the geodesic distance between the coordinates and displays the result in kilometers.

## Features

- Input start and end locations.
- Fetch geographic coordinates using the Nominatim API.
- Calculate the geodesic distance between two locations.
- Switch start and end locations.
- Exit the application gracefully.

## Prerequisites

Make sure you have Python installed on your system. You also need to install the following Python libraries:

- `geopy`
- `requests`
- `pillow` (for handling images, if required)

You can install these libraries using pip:

```sh
pip install geopy requests pillow
```

## Usage

1. Clone the repository to your local machine:

```sh
git clone https://github.com/your-username/distance-calculator.git
```

2. Navigate to the project directory:

```sh
cd distance-calculator
```

3. Ensure you have an image file named `arrow.png` in the project directory or update the code to point to the correct path of your arrow image.

4. Run the application:

```sh
python distance_calculator.py
```

## Code Explanation

The main script `distance_calculator.py` includes the following key functions:

- `get_coordinates(address)`: Fetches the geographic coordinates (latitude and longitude) for a given address using the Nominatim API.
- `calculate_distance()`: Calculates the geodesic distance between the start and end locations entered by the user.
- `switch_points()`: Switches the values between the start and end location entry widgets.

The GUI is built using Tkinter and includes:

- Labels and entry widgets for start and end locations.
- A switch button to swap the start and end locations.
- A button to calculate the distance.
- A result label to display the calculated distance.
- An exit button to close the application.

## License

This project is free to use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- This application uses the [Nominatim API](https://nominatim.openstreetmap.org) from OpenStreetMap for geocoding.
- Distance calculations are performed using the `geopy` library.

