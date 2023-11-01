from torch.utils.data.dataset import Dataset
from PIL import Image
from torchvision.transforms import ToTensor, Resize
from pathlib import Path
import json
import torch

class ViewpointDataset(Dataset):
    def __init__(self, path, split) -> None:
        super().__init__()
        self.split = split
        self.path = Path(path)
        self.images = self.load_split()
        
    def load_split(self):
        datapoints = []
        with open(self.path/f"{self.split}.txt", "r") as txtfile:
            images = [l.strip() for l in txtfile.readlines()]
            for i in range(18):
                for img in images:
                    datapoints.append(f"{img}.off_camera_{i}")
        return datapoints
        
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, index):
        ID = self.images[index]
        image = self.path/f"{ID}.jpg"
        meta = self.path/f"{ID}.json"
        with open(meta, "r") as jsonfile:
            data = json.load(jsonfile)
            if isinstance(data, list): data=data[0]
            sphere_coords = data["sphere_coords"]
        image = Image.open(image).convert("RGB")
        image = Resize(224)(image)
        image = ToTensor()(image)
        label = torch.tensor([sphere_coords[0:2]]).squeeze(0)
        return image, label
        

if __name__ == "__main__":
    dataset = ViewpointDataset("E:/data/modelnet28", "train")
    img, coords = dataset.__getitem__(0)
    print(img.shape, coords.shape)