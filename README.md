# DeepSeekR1-PDFAssistant

DeepSeekR1-PDFAssistant is an advanced AI-powered assistant that allows users to query and extract insights from PDF documents. The project leverages the DeepSeek-R1 family of models, providing precise and efficient document analysis capabilities.

## Features
- Upload and process PDF files to extract relevant information.
- Ask questions directly related to the uploaded PDF.
- Supports multiple DeepSeek-R1 models with varying resource requirements.
- Interactive and user-friendly interface built with Gradio.

## Getting Started

### Prerequisites
To run this project, ensure you have the following installed:
- Python 3+
- Pip
- Virtual environment (optional but recommended)
- **Ollama** (required to run DeepSeek models locally) – Download from [here](https://ollama.com/download)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mushaid01/DeepSeekR1-PDFAssistant.git
   cd DeepSeekR1-PDFAssistant
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Ollama:
   download it manually from [Ollama's official site](https://ollama.com/download).

4. Pull the required DeepSeek models from Ollama:
   ```bash
   ollama pull deepseek-r1:1.5b
   ollama pull deepseek-r2:3b
   ollama pull deepseek-r3:7b
   ollama pull deepseek-r1:67b
   ollama pull deepseek-r1:70b
   ```

5. Launch the application:
   ```bash
   python ui.py
   ```

6. Access the application in your web browser at `http://127.0.0.1:7860/`.

## Usage
1. Upload a PDF file using the "Upload PDF" button.
2. Choose a model from the dropdown menu based on your resource constraints:
   - **DeepSeek-R1:1.5B**: Suitable for environments with limited resources.
   - **DeepSeek-R2:3B**: Requires moderate resources.
   - **DeepSeek-R3:7B**: Ideal for high-performance setups.
   - **DeepSeek-R1:671B & 70B**: Requires high-end GPU resources for extensive document analysis.
3. Enter your question in the text box and click "Submit".
4. View the AI-generated response in the "Answer" section.

## Choosing the Right Model
- **DeepSeek-R1:1.5B**: Lightweight and fast, perfect for testing or when resources are constrained.
- **DeepSeek-R2:3B**: A balanced option, suitable for most applications with moderate resources.
- **DeepSeek-R3:7B**: High accuracy and comprehensive analysis, recommended for setups with high-end GPUs.
- **DeepSeek-R1:70B & 671B**: Designed for high-performance environments requiring extensive document analysis.

## Contributing
We welcome contributions to improve DeepSeekR1-PDFAssistant. Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [LangChain](https://github.com/hwchase17/langchain) for document processing.
- [Gradio](https://github.com/gradio-app/gradio) for creating the user interface.
- [Ollama](https://ollama.com) for enabling local model execution.
- DeepSeek-R1 model family for powering the AI capabilities.

## Contact
For questions or support, please reach out to **mir786mushaid@gmail.com**.
