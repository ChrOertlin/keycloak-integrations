import sys
print(f"Python path: {sys.path}")

try:
    from app.main import app
    print("Successfully imported app from main")
except Exception as e:
    print(f"Error importing app: {e}")
    raise

if __name__ == "__main__":
    app.run()
