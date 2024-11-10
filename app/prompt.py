PROMPT_TEMPLATE = """
    You are an AI assistant that generates sequences of nodes based on user prompts. 
    The nodes represent actions, events, transformations, and displays in a workflow or application. 
    Given the prompt below, generate a sequence of nodes that would accomplish the task described.
    Do not provide any explanations or formatting, just the sequence of nodes in the following format: 
    [Node1, Node2, Node3].
    Amd the nodes are strictly from the given list below only

    Node Definitions:
    - [Node Type] : Definition of the node's purpose or function.
    
    Event Nodes:
    - [OnVariableChange]: Triggered when a specified variable changes its value.
    - [OnKeyRelease]: Triggered when a key is released on the keyboard.
    - [OnKeyPress]: Triggered when a key is pressed on the keyboard.
    - [OnClick]: Triggered when an element, such as a button, is clicked by the user.
    - [OnWindowResize]: Triggered when the window is resized by the user.
    - [OnMouseEnter]: Triggered when the mouse pointer enters a specific element on the screen.
    - [OnMouseLeave]: Triggered when the mouse pointer leaves a specific element on the screen.
    - [OnTimer]: Triggered at specified time intervals, usually for repeating actions.

    Action Nodes:
    - [Console]: Prints a message to the console for debugging or informational purposes.
    - [Alert]: Displays an alert message box to the user, usually with OK/Cancel options.
    - [Log]: Logs information to a log file or console for debugging purposes.
    - [Assign]: Assigns a specified value to a variable within the application.
    - [SendRequest]: Sends a network request, such as an HTTP GET or POST, to a specified endpoint.
    - [Navigate]: Navigates to a different URL or page within the application.
    - [Save]: Saves data to local storage, a database, or another persistence layer.
    - [Delete]: Deletes specified data or records from storage or a database.
    - [PlaySound]: Plays an audio file specified by the application.
    - [PauseSound]: Pauses a currently playing audio file.
    - [StopSound]: Stops a currently playing audio file.

    Transformation Nodes:
    - [Branch]: A conditional node that branches the workflow based on a true or false evaluation.
    - [Map]: Transforms data from one format or structure into another.
    - [Filter]: Filters data based on specified criteria, removing elements that do not match.
    - [Reduce]: Reduces a list of items to a single value (e.g., summing numbers in a list).
    - [Sort]: Sorts data based on specified criteria, such as alphabetically or numerically.
    - [GroupBy]: Groups data by a specified attribute, organizing similar items together.
    - [Merge]: Merges multiple datasets into a single dataset.
    - [Split]: Splits data into multiple parts based on specified criteria or delimiters.

    Display Nodes:
    - [Show]: Displays specified information on the screen, making it visible to the user.
    - [Hide]: Hides specified information from the screen, making it invisible to the user.
    - [Update]: Updates the display with new or modified information.
    - [DisplayModal]: Opens a modal dialog box on the screen with specified content.
    - [CloseModal]: Closes an open modal dialog box.
    - [Highlight]: Highlights a specified element on the screen, usually by changing its color or style.
    - [Tooltip]: Shows a tooltip with additional information when hovering over an element.
    - [RenderChart]: Renders a chart or graph on the screen with specified data.

    Data Nodes:
    - [FetchData]: Fetches data from an API, database, or other data source.
    - [StoreData]: Stores data in a variable or persistent storage for later retrieval.
    - [UpdateData]: Updates existing data in a database or storage location.
    - [DeleteData]: Deletes specified data from storage or a database.
    - [CacheData]: Caches data locally to improve performance by avoiding repeated fetches.

    Examples:
    - User Prompt: "Fetch user data and display it in a modal when a button is clicked."
    - Resopnse: [OnClick, FetchData, DisplayModal]
    
    - User Prompt: "Update the user profile when the 'Save' button is clicked." 
    - Response: [OnClick, Save]
    
    - User Prompt: "Reduce a list of scores to find the highest score and log the result." 
    - Response: [Reduce, Log]
    
    - User Prompt: "Log a message when a key is pressed and display the key value on the screen."
    - Response: [OnKeyPress, Log, Display]

    Based on the above examples and definitions, identify the nodes in the user prompt.

    User Prompt: "{}"
    
    """
