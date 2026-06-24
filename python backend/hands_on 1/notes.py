# TASK 1: Understanding the Django Request–Response Cycle

# 1. Request Lifecycle: GET 
# When a client (browser, mobile app, or API consumer) sends a GET request to /api/courses/, Django processes it through the following sequence:

# Step 1: Client Request

# The browser sends an HTTP GET request:

# GET /api/courses/

# Step 2: Middleware Processing (Request Phase)

# Incoming requests first pass through Django middleware.

# Middleware can inspect, modify, or reject requests before

# they reach the application logic.

# Step 3: URL Routing

# Django's URL dispatcher (urls.py) matches the requested URL

# pattern (/api/courses/) to the appropriate view.

# Step 4: View Execution

# The mapped view receives the request and contains the

# business logic required to process it.

# Step 5: Model Interaction

# The view communicates with the Model layer to retrieve

# or manipulate data.

# Example:

# courses = Course.objects.all()

# Django's ORM translates this query into SQL and executes

# it against the database.

# Step 6: Database Response

# The database returns the requested records to the Model,

# which passes the data back to the View.

# Step 7: Response Creation

# The View formats the data and creates an HTTP response,

# typically JSON for APIs or HTML for web pages.

# Step 8: Middleware Processing (Response Phase)

# The response passes back through middleware where it may

# be modified before leaving the application.

# Step 9: Client Receives Response

# Django returns the final HTTP response to the browser.

# Request Flow Diagram:
# 1. Browser/Client

#2. Middleware (Request)
#3. URL Router (urls.py)
#4. View
#5. Model (ORM)
#6. Database
#7. View
#8. Middleware (Response)
#9. Browser/Client

# TASK 2. Middleware in Django

# Middleware is a framework-level component that sits between

# the incoming request and the view, as well as between the

# outgoing response and the client.



# Responsibilities include:

# - Authentication and authorization

# - Session management

# - Security enhancements

# - Request/response modification

# - Logging and monitoring


# Examples of Built-in Middleware:

# 1. SecurityMiddleware

# (django.middleware.security.SecurityMiddleware)


# Purpose:

# - Adds security-related HTTP headers.

# - Supports HTTPS redirection.

# - Helps protect against common web vulnerabilities.


# 2. SessionMiddleware

# (django.contrib.sessions.middleware.SessionMiddleware)



# Purpose:

# - Enables session support.

# - Stores and retrieves user session data.

# - Maintains state across multiple requests.



#TASK 3. WSGI vs ASGI

# WSGI (Web Server Gateway Interface)

# - Traditional Python web application standard.

# - Supports synchronous request handling.

# - Well-suited for conventional web applications.

# - Common deployment servers include Gunicorn and uWSGI.


# ASGI (Asynchronous Server Gateway Interface)



# - Modern successor to WSGI.

# - Supports asynchronous programming using async/await.

# - Handles WebSockets and long-lived connections.

# - Better suited for real-time and high-concurrency systems.

# Key Differences:
# WSGI:

# - Synchronous

# - Request/response only

# - Suitable for traditional web applications



# ASGI:

# - Asynchronous and synchronous support

# - Supports WebSockets, background tasks, and streaming

# - Suitable for real-time applications


# Which one does Django use?

# Django traditionally uses WSGI and automatically generates

# a wsgi.py file for deployment.

# Modern Django versions also provide asgi.py, enabling

# deployment with ASGI-compatible servers.


# When should ASGI be used?

# - Real-time chat applications

# - Live notifications

# - WebSocket-based communication

# - Streaming services

# - High-concurrency asynchronous workloads



# TASK 4. MVC Pattern and Django's MVT Architecture

# MVC (Model–View–Controller) is a software design pattern

# used to separate application concerns.


# Components:


# Model:

# - Manages application data and database operations.



# View:

# - Represents the user interface.



# Controller:

# - Handles user requests and application logic.

# - Coordinates communication between the Model and View.



# Django follows the MVT (Model–View–Template) architecture.



# Components:



# Model:

# - Handles data and database interactions.



# View:

# - Contains business logic and request handling.



# Template:

# - Responsible for presentation and rendering UI.


# MVC to Django MVT Mapping:



# MVC Component        Django Component



# Model            --> Model

# Controller       --> View

# View             --> Template



# Explanation:


# Django's View performs the responsibilities typically

# associated with a Controller in MVC by processing requests,

# executing business logic, and interacting with Models.



# Django's Template is responsible for presenting data to

# users and therefore corresponds to the View layer in MVC.


