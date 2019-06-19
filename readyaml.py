import yaml
myfile = "config_global.yaml"
class readyaml:
    def readfile(self,conf):
        try:
            with open(conf) as ymal_data:
                ymaldata=yaml.load(ymal_data)
                yield ymaldata, True
        except e:
            yield e ,False
a = readyaml()
data = a.readfile(myfile)
for i in data:
    print(i)
    print(id(i))

