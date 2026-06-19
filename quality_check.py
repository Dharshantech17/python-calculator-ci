import ast
import os
import sys

for root, dirs, files in os.walk("."):
    for file in files:
        if (
            file.endswith(".py")
            and file != "quality_check.py"
            and not file.startswith("test_")
        ):
            path = os.path.join(root, file)

            with open(path, "r") as f:
                lines = f.readlines()

            if len(lines) > 100:
                print(f"ERROR: {path} exceeds 100 lines")
                sys.exit(1)

            with open(path, "r") as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if ast.get_docstring(node) is None:
                        print(
                            f"ERROR: Function '{node.name}' "
                            f"in {path} has no docstring"
                        )
                        sys.exit(1)

print("Quality checks passed")
