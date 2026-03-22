import os,importlib.util

class PluginSystemv2:
    def __init__(self,app):
        self.app=app
        self.plugins={}

    def load(self):
        folder="plugins"
        os.makedirs(folder,exist_ok=True)

        for file in os.listdir(folder):
            if not file.endswith(".class"):continue

            path=os.path.join(folder,file)
            name=file[:-3]

            spec=importlib.util.spec_from_file_location(name,path)
            mod=importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)

            pname=getattr(mod,"name",name)
            protected=getattr(mod,"protected",False)

            if hasattr(mod,"run"):
                mod.run(self.app)
                self.plugins[pname]={"module":mod,"protected":protected}