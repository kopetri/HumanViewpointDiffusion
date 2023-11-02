from pytorch_utils.module import LightningModule
from network import ViewpointModel
import torch

class ViewpointModule(LightningModule):
    def __init__(self, opt=None, **kwargs):
        super().__init__(opt, **kwargs)
        self.network = ViewpointModel(dropout=self.opt.dropout)
        self.criterion = torch.nn.MSELoss()
        
    def forward(self, batch, batch_idx, split):
        x, y = batch
        B = x.shape[0]

        y_hat = self.network(x)
        loss = self.criterion(y_hat, y)
        self.log_value("loss", loss, split, B)
        return loss

    def configure_optimizers(self):
        optimizer = torch.optim.AdamW(self.network.parameters(), lr=self.opt.learning_rate, weight_decay=self.opt.weight_decay, betas=[0.9, 0.98], eps=1.0e-6)
        
        scheduler = {
                'scheduler': torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=self.opt.lr_patience, factor=self.opt.factor),
                'interval': 'epoch',
                'monitor': 'valid_loss',
                'frequency': 1,
                'strict': True,
            }
        return [optimizer], [scheduler]
   