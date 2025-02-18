# Use the official PostgreSQL 16.2 image based on Bullseye
FROM postgres:16.2-bullseye

# Step 1: Update and install required dependencies
RUN echo "Step 1: Installing required dependencies..." && \
    apt-get update && \
    apt-get install -y \
    build-essential \
    clang-13 \
    gcc \
    git \
    make \
    postgresql-server-dev-16 \
    wget && \
    echo "Dependencies installed successfully!" && \
    rm -rf /var/lib/apt/lists/*

# Step 2: Set Clang as default compiler
RUN echo "Step 2: Setting Clang as default compiler..." && \
    update-alternatives --install /usr/bin/clang clang /usr/bin/clang-13 100 && \
    update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-13 100 && \
    echo "Clang has been set as the default compiler successfully!"

# Step 3: Clone the pgvector repository
RUN echo "Step 3: Cloning the pgvector repository..." && \
    git clone https://github.com/pgvector/pgvector.git /pgvector && \
    echo "Successfully cloned pgvector repository!"

# Step 4: Build and install pgvector
WORKDIR /pgvector
RUN echo "Step 4: Building pgvector..." && \
    make && \
    echo "Build completed successfully!" && \
    echo "Step 5: Installing pgvector..." && \
    make install && \
    echo "Installation completed successfully!"

# Step 5: Cleanup pgvector files
RUN echo "Step 6: Cleaning up /pgvector directory..." && \
    rm -rf /pgvector && \
    echo "Cleanup completed successfully."

# Expose the default PostgreSQL port
EXPOSE 5432

# Print a message to indicate that the Dockerfile has been executed successfully
RUN echo "Dockerfile execution completed successfully."