### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  JavaScript is a client-side programming language used for dynamic user interfaces and interactive web sites, 
  while Python is a server-side programming language used for web development, data analysis, and artificial intelligence.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  Using the get() method with a default value, like my_dict.get("c", "default_value").
  Using a try-except block, like try: value = my_dict["c"] except KeyError: value = "default_value".

- What is a unit test?
  A unit test is a sort of software testing that ensures that a software application's individual parts or units operate properly when 
  separated from the rest of the application. A single method or function in the code is tested via unit tests, which are often automated.

- What is an integration test?
  An integration test is a sort of software testing that determines if several parts or modules of a software program function properly together. 
  Usually carried out after unit tests, integration tests examine how the various components of the application interact with one another.

- What is the role of web application framework, like Flask?
  A web application framework, like Flask, provides a structured approach to building web applications. It provides pre-built components, libraries,
  and tools that make it easier to develop, deploy, and maintain web applications.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  Depending on the type of data being sent, one can choose between sending Flask information as a parameter in a route URL or by utilizing a URL query parameter. A parameter should be given in the route URL if the data is necessary to identify a particular resource, such as an ID or slug. The information should be provided as a URL query parameter if it is optional or is used to filter resources, such as a search query.

- How do you collect data from a URL placeholder parameter using Flask?
  To collect data from a URL placeholder parameter using Flask, you can define a route with a variable placeholder enclosed in angled brackets, like
  @app.route('/foods/<type>'). In the route function, you can access the data using the parameter name, like def foods(type):.

- How do you collect data from the query string using Flask?
  To collect data from the query string using Flask, you can use the request.args object, which is a dictionary-like object containing the query string
  parameters. You can access the values using the parameter names, like type = request.args.get('type').

- How do you collect data from the body of the request using Flask?
  To collect data from the body of the request using Flask, you can use the request.json object, which is a dictionary-like object containing the JSON 
  data sent in the request body.

- What is a cookie and what kinds of things are they commonly used for?
  A cookie is a small text file that a website places on a user's computer and uses to keep data such as the user's preferences, login status, and other 
  specifics. Cookies are frequently used for session management, user authentication, and personalisation.

- What is the session object in Flask?
  The session object in Flask is a dictionary-like object that allows the application to store user-specific data across multiple requests. It uses cookies 
  to store a session ID on the user's computer and stores the data on the server-side.

- What does Flask's `jsonify()` do?
  Flask's jsonify() function converts a Python dictionary to a JSON response object. It sets the Content-Type header to application/json and returns a 
  JSON-encoded response that can be consumed by other applications or JavaScript clients.
