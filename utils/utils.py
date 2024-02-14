def pretty_stringify_object(obj):
    return_string = f"{type(obj).__name__}: {{"
    for key, value in vars(obj).items():
        if type(value) is not type([]):
            return_string += f"{key}: {value}, "
        else:
            return_string += f"{key}: ["
            for item in value: 
                return_string += f"{item}, "
            if len(value) > 0:
                return_string = return_string[:-2] + "], "
            else:
                return_string += "], "
    return_string = return_string[:-2] + "}"
    return return_string