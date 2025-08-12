# 🔍 UBM OCR Pro

A modern, beautiful web application for PDF OCR processing using Mistral AI's advanced OCR capabilities.

![UBM OCR Pro](https://img.shields.io/badge/Status-Ready%20to%20Deploy-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 🔍 **Advanced OCR**: Powered by Mistral AI's latest OCR model
- 🎨 **Modern UI**: Beautiful design with dark/light theme support
- 📱 **Responsive Design**: Works perfectly on desktop and mobile
- 🎯 **Drag & Drop**: Intuitive file upload with drag and drop
- 📝 **Dual View**: View results in formatted markdown or raw text
- 💾 **Export Options**: Copy to clipboard or download results
- 🚀 **Fast Processing**: Efficient PDF processing and text extraction
- 🌐 **Easy Deployment**: Ready-to-deploy with multiple platform support

## 🚀 Quick Deploy

### Deploy to Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/your-template-id)

### Deploy to Render
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

### Deploy to Vercel
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/ubm-ocr-pro)

## 🛠️ Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ubm-ocr-pro.git
   cd ubm-ocr-pro
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables** (optional)
   ```bash
   export MISTRAL_API_KEY="your-api-key-here"
   export SECRET_KEY="your-secret-key"
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8080`

## 🐳 Docker Deployment

### Using Docker Compose
```bash
docker-compose up -d
```

### Using Docker directly
```bash
docker build -t ubm-ocr-pro .
docker run -p 8080:8080 -e MISTRAL_API_KEY="your-key" ubm-ocr-pro
```

## 🌐 Platform-Specific Deployment

### Railway
1. Fork this repository
2. Connect your GitHub account to Railway
3. Create a new project from your forked repo
4. Set environment variable: `MISTRAL_API_KEY`
5. Deploy automatically!

### Render
1. Fork this repository
2. Connect to Render
3. Create a new Web Service
4. Set environment variable: `MISTRAL_API_KEY`
5. Deploy!

### Vercel
1. Fork this repository
2. Import to Vercel
3. Set environment variable: `MISTRAL_API_KEY`
4. Deploy!

### Heroku
```bash
heroku create your-app-name
heroku config:set MISTRAL_API_KEY="your-key"
git push heroku main
```

## 📖 Usage

1. **Upload PDF**: Drag and drop a PDF file or click to browse
2. **Process**: Click "Process OCR" to start text extraction
3. **View Results**: Switch between formatted and raw text views
4. **Export**: Copy text to clipboard or download as markdown file

## ⚙️ Configuration

### Environment Variables
- `MISTRAL_API_KEY`: Your Mistral AI API key (required)
- `SECRET_KEY`: Flask secret key (auto-generated if not set)
- `PORT`: Port to run the application (default: 8080)
- `FLASK_ENV`: Set to 'production' for production deployment

### Application Settings
- **File Size Limit**: 16MB (configurable in `app.py`)
- **Supported Formats**: PDF files only
- **Upload Directory**: `uploads/` (auto-created)

## 🔒 Security

- Environment-based configuration
- Secure file handling with automatic cleanup
- Input validation and sanitization
- Production-ready security headers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/ubm-ocr-pro/issues) page
2. Create a new issue if needed
3. Provide detailed information about your problem

## 🙏 Acknowledgments

- [Mistral AI](https://mistral.ai/) for the powerful OCR API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- Modern CSS design system for the beautiful UI