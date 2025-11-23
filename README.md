
<h3>Building Intelligent, Factual Applications with LangChain and RAG</h3>
</div>

<div align="center">
<img src="https://img.shields.io/badge/Project%20Status-Ready%20for%20Deployment-brightgreen" alt="Project Status"/>
<img src="https://img.shields.io/github/last-commit/vidhi-sys/LangChain_and_RAG?color=blue" alt="Last Commit"/>
<img src="https://img.shields.io/github/repo-size/vidhi-sys/LangChain_and_RAG?color=orange" alt="Repo Size"/>
<img src="https://img.shields.io/badge/Python-3.8%252B-yellowgreen" alt="Python 3.8+"/>
<img src="https://img.shields.io/badge/Framework-LangChain-ff69b4" alt="LangChain Version"/>
![AI Demos Hackathon](https://img.shields.io/badge/AI%20Demos-Hackathon%20Nov%202025-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.0.346-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red)
</div>


2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Add your Google PaLM API key to .env
```

## Configuration

Add your Google PaLM API key to the `.env` file:
```
GOOGLE_PALM_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run src/ui/streamlit_app.py
```

2. Open your browser and navigate to the provided local URL

## Technology Stack

- **Google PaLM LLM**: Core AI model for generating responses
- **LangChain**: Framework for building AI applications
- **Streamlit**: Web application framework
- **Pinecone**: Vector storage 
- **Python**: Backend programming language

## Development

### Running Tests
```bash
pytest tests/ -v
```

### Code Formatting
```bash
black src/ tests/
```

### Code Linting
```bash
flake8 src/ tests/
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Codebasics for inspiring this project
- Google PaLM for the LLM capabilities
- LangChain for the AI framework
- AI Demos Monthly Hackathon for the platform

## Support

For support, please open an issue in the GitHub repository or contact the development team.

---


