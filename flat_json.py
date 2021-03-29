import json
import sys


def main():
    """
    Takes a JSON object as input or a file path to several JSON objects as a command line argument
    and outputs a flattened version(s) of the JSON object(s), with keys as the path to every
    terminal value in the JSON structure.
    Prints valid JSON(s).
    :return: a list of all the JSON(s)
    """
    # if there are no command line args, run as normal with the input from stdin
    if len(sys.argv) == 1:
        json_string = "".join(sys.stdin)
        hierarchical_jsons = [load_json(json_string)]
    # if there are command line args, run using the first argument as a file path to a file with
    # correctly formatted test json values
    else:
        with open(sys.argv[1]) as file:
            hierarchical_jsons = json.load(file)

    flattened_jsons = []

    #   for all the jsons given, in the non-test case there will only be one
    for hierarchical_json in hierarchical_jsons:
        # flatten the json object
        flat_json = flatten_json(hierarchical_json)
        # print the prettied json to stdout
        json_string = json.dumps(flat_json, indent=4)
        flattened_jsons.append(json_string)
        print(json_string)

    return flattened_jsons


def load_json(json_string):
    """
    Given a json object as a string, returns a dict object with the contents of the json object.

    :param json_string: the json object as a string
    :return: a dict object representing the contents of the json object passed in.
    """
    return json.loads(json_string)


def flatten_json(json_object):
    """
    Given a json object, returns a version of the json that is flattened.

    :param json_object: the json object ot flatten
    :return: a json object that is the flattened version of the passed in json object.
    """
    flat_json = {}
    # Check that either an element is already flat, or flatten it
    for key in json_object.keys():
        # if the element is not flat, flatten it recursively
        if isinstance(json_object[key], dict):
            flat_sub_json = flatten_json(json_object[key])
            # add each newly flattened value to the result json
            for sub_key in flat_sub_json.keys():
                flat_json[key + "." + sub_key] = flat_sub_json[sub_key]
        # if the element is flat, add it to the result
        else:
            flat_json[key] = json_object[key]
    return flat_json


if __name__ == '__main__':
    main()

