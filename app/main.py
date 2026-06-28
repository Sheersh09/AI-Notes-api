from fastapi import FastAPI

# Create the FastAPI app instance that will handle incoming requests.
app = FastAPI()

# Register a GET endpoint for the root URL path "/".
@app.get("/")
def read_root() -> dict[str, str]:     # Define the function that will run when someone visits the root endpoint.
    return {"message": "Welcome to the AI Notes API"}    # Return a simple welcome message as JSON.


@app.get("/about")   # Register a GET endpoint for the "/about" URL path.
def read_about() -> dict[str, str]:      # Define the function that will run when someone visits the about endpoint.
    return {
        "project": "AI Notes API",
        "phase": "Phase 0 - Project Setup",
        "description": "This is a FastAPI backend for the AI Notes app.",
    }
