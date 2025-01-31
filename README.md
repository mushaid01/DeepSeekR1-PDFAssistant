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

3. Launch the application:
   ```bash
   python ui.py
   ```

4. Access the application in your web browser at `http://127.0.0.1:7860/`.

## Usage
1. Upload a PDF file using the "Upload PDF" button.
2. Choose a model from the dropdown menu based on your resource constraints:
   - **DeepSeek-R1:1.5B**: Suitable for environments with limited GPU resources.
   - **DeepSeek-R2:3B**: Requires moderate GPU resources.
   - **DeepSeek-R3:7B**: Ideal for high-performance GPUs, providing the most accurate results.
3. Enter your question in the text box and click "Submit".
4. View the AI-generated response in the "Answer" section.

## Choosing the Right Model
- **DeepSeek-R1:1.5B**: Lightweight and fast, perfect for testing or when resources are constrained.
- **DeepSeek-R2:3B**: A balanced option, suitable for most applications with a decent GPU.
- **DeepSeek-R3:7B**: High accuracy and comprehensive analysis, recommended for setups with high-end GPUs.

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
- DeepSeek-R1 model family for powering the AI capabilities.

## Contact
For questions or support, please reach out to **mir786mushaid@gmail.com**.
