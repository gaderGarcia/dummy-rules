import inspect
import ast
import typing
from rules import rule

def get_function_metadata(func):
    metadata=dict()
    # Get information about the function's parameters
    parameters = inspect.signature(func).parameters
    metadata["function_name"]=func.__qualname__
    
    param_info = {name: param.annotation.__name__ for name, param in parameters.items()}
    #print(param_info)
    # Get the docstring and parse it for type hints in comments
    docstring = inspect.getdoc(func)
    #print(docstring)
    if docstring:
        parsed_docstring = parse_parameters_section(docstring)
        #print(parsed_docstring)
        features=[]
        for param in parsed_docstring:
            newParam= dict(param)
            
            for key in param.copy():
                if key in param_info:
                    newParam["type"] = param_info[key] 
                    features.append(newParam)
        metadata["features"]=features
    else:
        raise Exception("You must provide doc section describing parameters and features relatioship")
                    

    return metadata

def parse_parameters_section(docstring):
    param_info = []

    # Split the docstring by lines
    lines = docstring.splitlines()

    # Flag to indicate when the "Parameters" section is found
    in_parameters_section = False

    # Iterate through lines
    for line in lines:
        line = line.strip()

        # Check if the line indicates the start of the "Parameters" section
        if line.lower().startswith("parameters:"):
            in_parameters_section = True
            continue

        # Check if we are currently in the "Parameters" section
        if in_parameters_section:
            # Check if the line starts with a dash and contains a colon
            if line.startswith("-") and ":" in line:
                parts = line.split(":")
                param_name = parts[0].strip("-").strip()
                param_type_hint = parts[1].strip()
                param_info.append({param_name: param_type_hint})

            # Check if we have reached the end of the "Parameters" section
            elif line.lower().startswith("returns:"):
                break

    return param_info

def parse_docstring(docstring):
    tree = ast.parse(docstring)
    type_comments = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for param in node.args.args:
                if isinstance(param.annotation, ast.Name):
                    # Extract type hint from annotation
                    type_comments[param.arg] = param.annotation.id
                elif isinstance(param.annotation, ast.Subscript):
                    # Handle cases like List[int], Tuple[str, int]
                    type_comments[param.arg] = ast.dump(param.annotation)

    return type_comments

# Example function


# Get metadata for the function
metadata_calcualate = get_function_metadata(rule.calculate_score)
# Print the retrieved metadata
print(metadata_calcualate)

metadata_calculate_pi = get_function_metadata(rule.calculate_pi)
print(metadata_calculate_pi)
