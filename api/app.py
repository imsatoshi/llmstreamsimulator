from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoTokenizer
import os
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 初始化 Mistral tokenizer
logger.info("正在加载 Mistral tokenizer...")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
logger.info("Mistral tokenizer 加载完成")

@app.route('/api/tokenize', methods=['POST'])
def tokenize():
    try:
        data = request.json
        if not data or 'text' not in data:
            return jsonify({'error': '缺少文本参数'}), 400

        text = data['text']
        tokens = tokenizer.tokenize(text)
        return jsonify({'tokens': tokens})
    except Exception as e:
        logger.error(f"Tokenization error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5001)))
