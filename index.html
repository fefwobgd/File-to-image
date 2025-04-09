<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File to Image Converter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #121212;
            color: #e0e0e0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        h1 {
            color: #ff9800;
        }
        .container {
            width: 80%;
            max-width: 600px;
            padding: 20px;
            background-color: #1f1f1f;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            border-radius: 8px;
            text-align: center;
        }
        #fileInput {
            margin: 10px 0;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #555;
            border-radius: 4px;
            background-color: #333;
            color: #e0e0e0;
        }
        .info {
            margin-top: 15px;
            color: #ddd;
        }
        .progress {
            width: 100%;
            background-color: #444;
            border-radius: 5px;
            margin-top: 10px;
        }
        .progress-bar {
            height: 20px;
            width: 0;
            background-color: #4caf50;
            border-radius: 5px;
        }
        #outputImage {
            margin-top: 20px;
            max-width: 100%;
            border-radius: 8px;
            display: none;
        }
        .btn {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 15px;
        }
        .btn:hover {
            background-color: #0056b3;
        }
        .warning {
            color: #ff5722;
            font-weight: bold;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>File to Image Converter</h1>
        <p>Select a file to convert it into an image. The file will be interpreted as raw data and rendered in a pixelated format.</p>
        <input type="file" id="fileInput" accept="*/*" />
        <div id="fileSize" class="info"></div>
        <div id="warningMessage" class="warning">
            <strong>Warning:</strong> Files may take a long time to process depending on their size. Larger files could cause performance issues.
        </div>
        <div class="progress" id="progressBarContainer" style="display:none;">
            <div id="progressBar" class="progress-bar"></div>
        </div>
        <img id="outputImage" alt="Converted Image" />
        <button class="btn" id="resetBtn" style="display:none;">Reset</button>
    </div>
    <script>
        document.getElementById('fileInput').addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (!file) {
                alert("No file selected.");
                return;
            }
            const fileSize = file.size;
            document.getElementById('fileSize').textContent = `File size: ${fileSize} bytes`;
            document.getElementById('warningMessage').style.display = 'block';
            const reader = new FileReader();
            reader.onloadstart = function() {
                document.getElementById('progressBarContainer').style.display = 'block';
            };
            reader.onprogress = function(e) {
                if (e.lengthComputable) {
                    const progress = (e.loaded / e.total) * 100;
                    document.getElementById('progressBar').style.width = progress + '%';
                }
            };
            reader.onload = function(e) {
                const data = new Uint8Array(e.target.result);
                const fileSize = data.length;
                const pixelCount = Math.ceil(fileSize / 4);
                const width = Math.floor(Math.sqrt(pixelCount));
                const height = Math.ceil(pixelCount / width);
                const paddedSize = width * height * 4;
                const paddedData = new Uint8Array(paddedSize);
                paddedData.set(data);
                const imgData = new ImageData(width, height);
                for (let i = 0; i < pixelCount; i++) {
                    const index = i * 4;
                    const pixelIndex = i * 4;
                    imgData.data[pixelIndex] = paddedData[index];
                    imgData.data[pixelIndex + 1] = paddedData[index + 1];
                    imgData.data[pixelIndex + 2] = paddedData[index + 2];
                    imgData.data[pixelIndex + 3] = 255;
                }
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');
                canvas.width = width;
                canvas.height = height;
                ctx.putImageData(imgData, 0, 0);
                const outputImage = document.getElementById('outputImage');
                outputImage.src = canvas.toDataURL();
                outputImage.style.display = 'block';
                document.getElementById('resetBtn').style.display = 'inline-block';
                document.getElementById('progressBarContainer').style.display = 'none';
            };
            reader.readAsArrayBuffer(file);
        });
        document.getElementById('resetBtn').addEventListener('click', function() {
            document.getElementById('fileInput').value = '';
            document.getElementById('fileSize').textContent = '';
            document.getElementById('outputImage').style.display = 'none';
            document.getElementById('resetBtn').style.display = 'none';
            document.getElementById('warningMessage').style.display = 'none';
        });
    </script>
</body>
</html>
