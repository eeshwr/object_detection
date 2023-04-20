from torchvision.io.image import read_image, ImageReadMode  # type: ignore
from torchvision.models.detection import (
    fasterrcnn_resnet50_fpn_v2,
    FasterRCNN_ResNet50_FPN_V2_Weights,
)  # type: ignore
from torchvision.utils import draw_bounding_boxes  # type: ignore
from torchvision.transforms.functional import to_pil_image  # type: ignore
import os
import requests
import uuid


def detect_and_save(image_url, output_location):
    response = requests.get(image_url)
    image_extention = ".jpg"
    image_file_name = str(uuid.uuid4()) + image_extention
    with open(image_file_name, "wb") as f:
        f.write(response.content)

    img = read_image(image_file_name, mode=ImageReadMode.RGB)

    # Step 1: Initialize model with the best available weights
    weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
    model = fasterrcnn_resnet50_fpn_v2(weights=weights, box_score_thresh=0.9)
    model.eval()

    # Step 2: Initialize the inference transforms
    preprocess = weights.transforms()

    # Step 3: Apply inference preprocessing transforms
    batch = [preprocess(img)]

    # Step 4: Use the model and visualize the prediction
    prediction = model(batch)[0]
    labels = [weights.meta["categories"][i] for i in prediction["labels"]]
    box = draw_bounding_boxes(
        img,
        boxes=prediction["boxes"],
        labels=labels,
        colors="red",
        width=4,
        font_size=30,
    )
    im = to_pil_image(box.detach())
    im.save(os.path.join(output_location, "detected_" + image_file_name))
