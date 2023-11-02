from module import ViewpointModule
from dataset import ViewpointDataset
from torch.utils.data.dataloader import DataLoader
import torch
import numpy as np
from tqdm import tqdm
from pytorch_utils.scripts import Trainer

if __name__ == "__main__":
    trainer = Trainer("Viewpoint Estimator")
    trainer.add_argument("--dataset_path", required=True, type=str)
    trainer.add_argument("--batch_size", default=8, type=int)
    trainer.add_argument("--learning_rate", default=1e-4, type=float)
    trainer.add_argument("--lr_patience", default=10, type=int)
    trainer.add_argument("--factor", default=0.1, type=float)
    trainer.add_argument("--weight_decay", default=0.3, type=float)
    trainer.add_argument("--dropout", default=0.5, type=float)
    
    args = trainer.setup()
    
    torch.use_deterministic_algorithms(True)
    torch.set_float32_matmul_precision('medium')
    
    train_dataset = ViewpointDataset(args.dataset_path, "train")
    valid_dataset = ViewpointDataset(args.dataset_path, "valid")
        
    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True, num_workers=args.worker, persistent_workers=True)
    valid_loader = DataLoader(valid_dataset, batch_size=1, shuffle=False, num_workers=args.worker, persistent_workers=True)
    
    model = ViewpointModule(args)
    
    trainer.fit(model, train_dataloaders=train_loader, val_dataloaders=valid_loader)
            