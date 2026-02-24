
#!torch.nn : These are the basic building blocks for graphs:
#!nn.Module :  is base class of all neural Network 

#! Sequential : 
model = nn.Sequential(nn.Conv2d(1, 20, 5), 
                      nn.ReLU(), 
                      nn.Conv2d(20, 64, 5), 
                      nn.ReLU()
                        )

#!Using Sequential with OrderedDict. This is functionally the same as the above code
model = nn.Sequential(
    OrderedDict(
        [
            ("conv1", nn.Conv2d(1, 20, 5)),
            ("relu1", nn.ReLU()),
            ("conv2", nn.Conv2d(20, 64, 5)),
            ("relu2", nn.ReLU()),
        ]
    )
)

#! Sequential.append(): if you have network already and need to add one layer at last
# example:
n = nn.Sequential(nn.Linear(1, 2), nn.Linear(2, 3))
n.append(nn.Linear(3, 4))
# result:
Sequential(
    (0): Linear(in_features=1, out_features=2, bias=True)
    (1): Linear(in_features=2, out_features=3, bias=True)
    (2): Linear(in_features=3, out_features=4, bias=True))

#! Sequential.extend(): add more bthan one layer at last in network if you already have 
# example:
n = nn.Sequential(nn.Linear(1, 2), nn.Linear(2, 3))
other = nn.Sequential(nn.Linear(3, 4), nn.Linear(4, 5))
n.extend(other)

# result
Sequential(
    (0): Linear(in_features=1, out_features=2, bias=True)
    (1): Linear(in_features=2, out_features=3, bias=True)
    (2): Linear(in_features=3, out_features=4, bias=True)
    (3): Linear(in_features=4, out_features=5, bias=True)
)

#! Sequential.insert() :  insert layer at any location in sequence here i have add at 0 th position 
n = nn.Sequential(nn.Linear(1, 2),
                  nn.Linear(2, 3))

n.insert(0, nn.Linear(3, 4))
# result:
Sequential(
    (0): Linear(in_features=3, out_features=4, bias=True)
    (1): Linear(in_features=1, out_features=2, bias=True)
    (2): Linear(in_features=2, out_features=3, bias=True)
)



#! ParameterList 
class MyModule(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.params = nn.ParameterList(
            [nn.Parameter(torch.randn(10, 10)) for i in range(10)]
        )

    def forward(self, x):
        # ParameterList can act as an iterable, or be indexed using ints
        for i, p in enumerate(self.params):
            x = self.params[i // 2].mm(x) + p.mm(x)
        return x
    
params_module = MyModule()

# example
tens = torch.randn(1,10).T
params_module(tens)

# or
tens = torch.randn(10,10)
params_module(tens)


#!ParameterDict
class MyModule(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.params = nn.ParameterDict(
            {
                "left": nn.Parameter(torch.randn(5, 10)),
                "right": nn.Parameter(torch.randn(5, 10)),
            }
        )

    def forward(self, x, choice):
        x = self.params[choice].mm(x)
        return x
    
module = MyModule()
# example
a = torch.randn(1,10).T  or torch.randn(5,10) 
module(a,'left') # because forward method has 2 params x and choice or
module(a,'right')

# ParameterDict.get()
module.params.get('left')

#ParameterDict.Item()
for item in model.params.items():
    print(item)



#! Conv1d : This required dim=2 or dim = 3 
input = torch.randn(15, 50) # herev 15 is channel 
m = nn.Conv1d(in_channels=15, out_channels=33, kernel_size=1, stride=1)
output = m(input)

# second example:
class Module(nn.Module):
    def __init__(self,in_channel=15,out_channel=30,kernel_size=2):
        super().__init__()
        self.conv1 = Conv1d(in_channels=in_channel,out_channels=out_channel,kernel_size=kernel_size,stride=1)

    def forward(self,x):
        return self.conv1(x)
    
#input
in_channel = input.shape[0]
out_channel =33
model = Module(in_channel,out_channel)

input = torch.rand(15,50)
print(model.forward(input).shape)


#^ M , W pattern double bottom W, double top M you can trade any time frame but daily is good for beginer











