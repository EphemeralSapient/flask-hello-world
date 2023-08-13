from flask import Flask, request, jsonify
import base64
import json
import os
import face_recognition

app = Flask(__name__)

@app.route("/")
def idk():
    return "home page lol"

@app.route('/upload', methods=['POST'])
def upload_images():
    try:
        data = request.get_json()
        if 'images' in data:
            images_data = data['images']
            uploaded_images = []

            for idx, image_data in enumerate(images_data):
                base64_image = image_data.get('image', '')
                if base64_image:
                    image_bytes = base64.b64decode(base64_image)
                    
                    # Save the image to a local directory
                    image_filename = f'image_{idx}.png'
                    image_path = os.path.join('uploads', image_filename)
                    with open(image_path, 'wb') as f:
                        f.write(image_bytes)

                    uploaded_images.append({'status': 'uploaded', 'filename': image_filename})

            return jsonify({'message': 'Images uploaded successfully', 'uploaded_images': uploaded_images}), 200
        else:
            print("wat, no images?")
            return jsonify({'error': 'No images found in request'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
