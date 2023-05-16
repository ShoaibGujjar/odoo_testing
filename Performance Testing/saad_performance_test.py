import pytest
import psutil

@pytest.fixture
def project_manager():
    # Set up the project manager module, e.g., initialize necessary objects or connect to the Odoo server
    project_manager = ProjectManager()  # Replace with your project manager initialization logic
    yield project_manager
    # Clean up resources, if any

def test_create_project(project_manager, benchmark):
    def create_project():
        # Measure the execution time of creating a project
        project_manager.create_project("Test Project")
    
    # Run the test and measure its execution time
    execution_time = benchmark(create_project)
    
    # Print the execution time and CPU/memory utilization
    print(f"Execution Time: {execution_time}")
    print(f"CPU Utilization: {psutil.cpu_percent()}%")
    print(f"Memory Utilization: {psutil.virtual_memory().percent}%")

def test_assign_task(project_manager, benchmark):
    def assign_task():
        # Measure the execution time of assigning a task
        project_manager.assign_task(1, 1, 1)
    
    # Run the test and measure its execution time
    execution_time = benchmark(assign_task)
    
    # Print the execution time and CPU/memory utilization
    print(f"Execution Time: {execution_time}")
    print(f"CPU Utilization: {psutil.cpu_percent()}%")
    print(f"Memory Utilization: {psutil.virtual_memory().percent}%")

# Add more performance tests for other actions (e.g., track_progress, generate_report)

if __name__ == "__main__":
    pytest.main()
