FROM python:3.12-slim

# Install uv and uvx
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory to /app
WORKDIR /app

# Pre-install the tools globally
RUN uv tool install duckduckgo-mcp-server
RUN uv tool install agentic-mcp-server

# Install FastMCP
RUN pip install fastmcp

# Copy the entire project into the container
COPY . .

# Ensure the uv tools path is in PATH
ENV PATH="/root/.local/bin:${PATH}"

# Run the gateway
CMD ["python", "-u", "app/gateway.py"]