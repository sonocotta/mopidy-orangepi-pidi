import pkg_resources
from importlib.metadata import entry_points

print ("Starting...")

for entry_point in pkg_resources.iter_entry_points("pidi.plugin.display"):
    try:
        plugin = entry_point.load()
        print(
            f"plugin name: {plugin.option_name}, module: {entry_point.module_name}, name: {entry_point.name} from {entry_point.dist.location}"
        )
    except (ImportError) as err:
        print(
            f"Error loading display plugin {entry_point}: {err}"
        )