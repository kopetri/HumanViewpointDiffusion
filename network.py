import torch
from torch.nn.modules import Module

class ViewpointModel(Module):
    def __init__(self, repo='facebookresearch/dinov2', version='dinov2_vitl14', dropout=0.5):
        super().__init__()
        self.transformer = torch.hub.load(repo, version)
        self.version = version
        self.mlps = torch.nn.Sequential(
            torch.nn.Linear(1024, 1024),
            torch.nn.BatchNorm1d(1024), 
            torch.nn.ReLU(), 
            torch.nn.Dropout(dropout),
            torch.nn.Linear(1024, 512),
            torch.nn.BatchNorm1d(512), 
            torch.nn.ReLU(), 
            torch.nn.Dropout(dropout),
            torch.nn.Linear(512, 256),
            torch.nn.BatchNorm1d(256), 
            torch.nn.ReLU(), 
            torch.nn.Dropout(dropout),
            torch.nn.Linear(256, 128),
            torch.nn.BatchNorm1d(128), 
            torch.nn.ReLU(), 
            torch.nn.Linear(128, 64),
            torch.nn.BatchNorm1d(64), 
            torch.nn.ReLU(),
            torch.nn.Linear(64, 2)
        )
        
        print("Freezing encoder weights.")
        for name, param in self.transformer.named_parameters():
            param.requires_grad = False
        
    def forward(self, x):
        x = self.transformer(x)
        x = self.mlps(x)
        return x
        
        
if __name__ == "__main__":
    img = torch.zeros((4, 3, 224, 224)).cuda()
    model = ViewpointModel().cuda()
    
    y = model(img)
    print(y.shape)