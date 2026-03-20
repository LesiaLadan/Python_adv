import inspect
import importlib


def analyze_module(module_name: str) -> None:
    """
    Analyze python module and print its functions and classes
    """
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Module '{module_name}' not found")
        return

    func = []
    clss = []

    for name, obj in inspect.getmembers(module):
        if name.startswith("__"):
            continue
        if inspect.isfunction(obj) or inspect.isbuiltin(obj):
            try:
                sign = str(inspect.signature(obj))
                sign = sign.replace(", /", "").replace("/", "")
            except ValueError:
                sign = "()"
            func.append(f"{name}{sign}")
        elif inspect.isclass(obj):
            clss.append(f"{name}")

    print("Functions:\n")
    if func:
        print("\n".join(func), "\n")
    else:
        print(f"No functions {module_name}")

    print("Classes:\n")
    if clss:
        print("\n".join(clss), "\n")
    else:
        print(f"No classes in module {module_name}")


if __name__ == "__main__":
    analyze_module("sys")
    analyze_module("math")
    analyze_module("json")
    analyze_module("collections")
    analyze_module("collect")
