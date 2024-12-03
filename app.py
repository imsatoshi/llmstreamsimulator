from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoTokenizer
import os
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# 初始化 Mistral tokenizer
logger.info("正在加载 Mistral tokenizer...")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2", use_auth_token="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")
logger.info("Mistral tokenizer 加载完成")

@app.route('/tokenize', methods=['POST'])
def tokenize():
    try:
        data = request.json
        text = data.get('text', '')
        logger.info(f"收到分词请求，文本长度: {len(text)} 字符")
        
        # 使用 Mistral tokenizer
        tokens = tokenizer.tokenize(text)
        logger.info(f"分词完成，token 数量: {len(tokens)}")
        
        return jsonify({
            'tokens': tokens,
            'token_count': len(tokens)
        })
    except Exception as e:
        logger.error(f"分词过程发生错误: {str(e)}", exc_info=True)
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    logger.info("Flask 服务启动在端口 5000...")
    app.run(host='0.0.0.0', port=5001)
