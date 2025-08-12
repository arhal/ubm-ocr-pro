import os
import base64
import tempfile
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from mistralai import Mistral

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Configure upload settings
UPLOAD_FOLDER = '/tmp' if os.environ.get('VERCEL') else 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

# Create uploads directory only if not on Vercel
if not os.environ.get('VERCEL') and not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_pdf_ocr(pdf_path):
    """Process PDF using Mistral OCR from file path"""
    try:
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
        return process_pdf_ocr_from_bytes(pdf_bytes)
    except Exception as e:
        raise Exception(f"OCR processing failed: {str(e)}")

def process_pdf_ocr_from_bytes(pdf_bytes):
    """Process PDF using Mistral OCR from bytes"""
    try:
        b64 = base64.b64encode(pdf_bytes).decode()
        api_key = os.environ.get('MISTRAL_API_KEY', '97ZQlsV45YrDusgZRwjArWGbh3nerFPb')
        client = Mistral(api_key=api_key)
        
        resp = client.ocr.process(
            model="mistral-ocr-latest",
            document={
                "type": "document_url",
                "document_url": f"data:application/pdf;base64,{b64}"
            },
            include_image_base64=True,
        )
        
        # Combine all pages
        full_text = ""
        for page in resp.pages:
            full_text += page.markdown + "\n\n"
        
        return full_text.strip()
    
    except Exception as e:
        raise Exception(f"OCR processing failed: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        try:
            # For Vercel, process file directly from memory
            if os.environ.get('VERCEL'):
                # Process PDF directly from uploaded file object
                pdf_bytes = file.read()
                result = process_pdf_ocr_from_bytes(pdf_bytes)
            else:
                # Save uploaded file temporarily for local/other deployments
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                # Process OCR
                result = process_pdf_ocr(filepath)
                
                # Clean up uploaded file
                os.remove(filepath)
            
            return jsonify({
                'success': True,
                'result': result,
                'filename': file.filename
            })
            
        except Exception as e:
            # Clean up file if it exists (for non-Vercel deployments)
            if not os.environ.get('VERCEL') and 'filepath' in locals() and os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file type. Please upload a PDF file.'}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug, host='0.0.0.0', port=port)