import subprocess


def run_neofetch():
    try:
        # Run the neofetch command and capture its output
        result = subprocess.run(['neofetch'], capture_output=True, text=True, check=True)

        # Return the captured output
        return result.stdout
    except subprocess.CalledProcessError as e:
        # If the command fails, return the error message
        return f"Error running neofetch: {e}"
    except FileNotFoundError:
        # If neofetch is not installed or not in PATH
        return "Error: neofetch command not found. Make sure it's installed and in your PATH."


# Example usage
if __name__ == "__main__":
    output = run_neofetch()
    print(output)