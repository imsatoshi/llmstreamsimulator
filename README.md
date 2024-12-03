# LLM Stream Output Simulator

这是一个用于模拟 LLM（大语言模型）流式输出效果的工具。它允许用户输入文本，将其分词，然后以流式方式显示这些 tokens，模拟 LLM 的实时输出效果。

## 功能特点

- 使用 Mistral tokenizer 进行文本分词
- 可自定义 token 显示间隔时间
- 可设置初始等待时间
- 实时显示 token 数量
- 美观的 token 显示效果
- 支持跨域请求

## 系统要求

- Python 3.11+
- 现代浏览器（支持 ES6+ 和 Fetch API）

## 安装步骤

1. 克隆项目到本地
2. 安装所需的 Python 包：
```bash
pip install flask flask-cors transformers
```
3. 设置 Hugging Face 访问令牌：
   - 在项目根目录创建 `.env` 文件
   - 添加你的 Hugging Face token：
```
HF_TOKEN=你的_huggingface_token
```

## 使用方法

1. 启动后端服务：
```bash
python app.py
```
服务将在 http://localhost:5001 启动

2. 在浏览器中打开 `index.html` 文件

3. 使用界面：
   - 在文本框中输入要处理的文本
   - 设置 token 间隔时间（毫秒）
   - 设置初始等待时间（秒）
   - 点击"开始流式输出"按钮

## 界面说明

- **文本输入框**：输入要进行分词和显示的文本
- **Token 间隔时间**：控制每个 token 显示之间的时间间隔（10-1000毫秒）
- **初始等待时间**：设置开始显示前的等待时间（0-10秒）
- **Token 数量**：实时显示文本的 token 数量
- **输出区域**：以格式化方式显示 tokens

## 技术架构

### 后端 (app.py)
- Flask 服务器提供 REST API
- 使用 Mistral tokenizer 进行分词
- 支持 CORS 跨域请求
- 包含详细的日志记录

### 前端 (index.html)
- 纯原生 JavaScript 实现
- 响应式设计
- 防抖处理避免频繁 API 调用
- 优雅的错误处理和用户提示

## API 说明

### POST /tokenize
将文本转换为 tokens

请求格式：
```json
{
    "text": "要分词的文本"
}
```

响应格式：
```json
{
    "tokens": ["token1", "token2", ...],
    "token_count": 数量
}
```

## 常见问题

1. **无法连接到后端服务**
   - 确保 Python 服务器正在运行
   - 检查端口 5001 是否被占用
   - 确认浏览器控制台中的错误信息

2. **分词结果不正确**
   - 确保 HF_TOKEN 环境变量正确设置
   - 检查 Mistral tokenizer 是否成功加载

3. **显示卡顿**
   - 尝试增加 token 间隔时间
   - 减少输入文本长度

## 开发说明

- 后端日志位于控制台输出
- 前端调试信息可在浏览器控制台查看
- 所有错误都会通过弹窗提示给用户

## 注意事项

- 需要有效的 Hugging Face 访问令牌
- 首次运行时需要下载模型文件
- 建议使用现代浏览器以获得最佳体验
