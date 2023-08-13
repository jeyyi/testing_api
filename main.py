from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
# from PIL import Image, ImageDraw
# from io import BytesIO
from ultralytics import YOLO
# import os
# import base64
# import cv2

app = FastAPI()

model_url = 'best.pt'
model = YOLO(model_url)

output_folder = "test_folder"
@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": f"Welcome to FastAPI! {model}"}

# @app.get("/detect_objects/")
# async def detect_objects():
#     try:
#         # image_data = await file.read()

#         # buf = BytesIO(image_data)
#         # detected_objects, annotated_image = detect_objects_on_image(buf, model, output_folder)
#         # annotated_image_data = image_to_base64(annotated_image)

#         return JSONResponse(content={'hey': model})
#         # return JSONResponse(content={"detected_objects": detected_objects, "annotated_image": annotated_image_data})
#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)

# def detect_objects_on_image(buf, model, output_folder):
#     temp_image = Image.open(buf)
#     results = model.predict(temp_image)
#     result = results[0]
#     output = []
#     for box in result.boxes:
#         x1, y1, x2, y2 = [round(x) for x in box.xyxy[0].tolist()]
#         class_id = box.cls[0].item()
#         prob = round(box.conf[0].item(), 2)
#         output.append([x1, y1, x2, y2, result.names[class_id], prob])

#         cropped_image = temp_image.crop((x1, y1, x2, y2))
#         image_filename = f"{result.names[class_id]}_{prob}.jpg"
#         cropped_image.save(os.path.join(output_folder, image_filename))

#     image = temp_image.copy()
#     draw = ImageDraw.Draw(image)
#     for box in output:
#         x1, y1, x2, y2, _, _ = box
#         draw.rectangle([x1, y1, x2, y2], outline='red', width=2)

#     return output, image

# def image_to_base64(image):

#     buffered = BytesIO()
#     image.save(buffered, format="JPEG")
#     return base64.b64encode(buffered.getvalue()).decode()