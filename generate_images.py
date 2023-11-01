from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
from diffusers.utils import load_image
import torch
import cv2
from PIL import Image
import numpy as np

def image_grid(imgs, rows, cols):
    assert len(imgs) == rows * cols

    w, h = imgs[0].size
    grid = Image.new("RGB", size=(cols * w, rows * h))
    grid_w, grid_h = grid.size

    for i, img in enumerate(imgs):
        grid.paste(img, box=(i % cols * w, i // cols * h))
    return grid

controlnet = ControlNetModel.from_single_file("E:/projects/stable-diffusion-webui/extensions/sd-webui-controlnet/models/controlnetPreTrained_cannyV10.safetensors")
pipe = StableDiffusionControlNetPipeline.from_single_file(
    "E:/projects/stable-diffusion-webui/models/Stable-diffusion/dreamshaper_8.safetensors", controlnet=controlnet, scheduler=14
)

pipe.enable_model_cpu_offload()
pipe.enable_xformers_memory_efficient_attention()

image = Image.open("E:\\data\\modelnet28\\airplane\\test\\airplane_0001.off_camera_0.jpg")


image = np.array(image)

low_threshold = 100
high_threshold = 200

image = cv2.Canny(image, low_threshold, high_threshold)
image = image[:, :, None]
image = np.concatenate([image, image, image], axis=2)
canny_image = Image.fromarray(image)
canny_image.show()


prompt = "Create a photorealistic image of an {} airplane soaring majestically through a clear blue sky."
prompt = [prompt.format(t) for t in ["red", "green", "black", "yellow"]]
generator = [torch.Generator(device="cpu").manual_seed(2) for i in range(len(prompt))]

output = pipe(
    prompt,
    canny_image,
    negative_prompt=["Watermark, Text, censored, deformed, bad anatomy, disfigured, poorly drawn face, mutated, extra limb, ugly, poorly drawn hands, missing limb, floating limbs, disconnected limbs, disconnected head, malformed hands, long neck, mutated hands and fingers, bad hands, missing fingers, cropped, worst quality, low quality, mutation, poorly drawn, huge calf, bad hands, fused hand, missing hand, disappearing arms, disappearing thigh, disappearing calf, disappearing legs, missing fingers, fused fingers, abnormal eye proportion, Abnormal hands, abnormal legs, abnormal feet, abnormal fingers"] * len(prompt),
    generator=generator,
    num_inference_steps=20,
)

result = image_grid(output.images, 2, 2)
result.show()
