# TAGLINE

机器学习 Web 界面构建工具

# TLDR

**运行 Gradio 应用**并启用热重载（文件变更时重启）

```gradio [app.py]```

**直接用 Python 运行**（无自动重载）

```python [app.py]```

**将当前目录部署**为 Hugging Face Space

```gradio deploy```

**使用自定义标题**和入口文件部署

```gradio deploy --title [my-app] --app-file [app.py]```

**打印 Gradio 环境信息**用于缺陷报告

```gradio environment```

**运行时启用调试输出**

```GRADIO_DEBUG=1 python [app.py]```

# SYNOPSIS

**gradio** _file_ [**--demo-name** _name_] [**--watch-dirs** _dirs_]

**gradio** **deploy** [**--title** _title_] [**--app-file** _file_]

**gradio** **environment**

# PARAMETERS

_file_
> 包含 Gradio 应用的 Python 文件。运行 **gradio file.py** 会以自动重载方式启动它，等同于 **python file.py**，但会在文件被编辑时重启。

**deploy**
> 子命令：将当前目录上传到 Hugging Face Spaces，遵循 **.gitignore** 规则。

**environment**
> 子命令：打印 Gradio、Python 和操作系统的版本信息，便于提交 issue。

**--title** _title_
> （**deploy**）为 Hugging Face Space 命名。

**--app-file** _file_
> （**deploy**）入口 Python 文件的路径（默认：**app.py**）。

**--demo-name** _name_
> 脚本中 demo 变量的名称（默认：**demo**）。

**--watch-dirs** _dirs_
> 热重载时要额外监听的目录。

# ENVIRONMENT

**GRADIO_SERVER_PORT**
> 要绑定的端口（默认：**7860**）。

**GRADIO_SERVER_NAME**
> 要绑定的网络接口。使用 **0.0.0.0** 可监听所有接口。

**GRADIO_DEBUG**
> 设为 **1** 可保持主线程存活并打印堆栈跟踪（在 Colab 中很有用）。

**GRADIO_TEMP_DIR**
> 临时文件（如上传的媒体）的存放目录。

# DESCRIPTION

**Gradio** 是一个用于构建机器学习演示和 Web UI 的 Python 库，附带一个轻量级配套 CLI。**gradio** 命令包装 **python** 来以实时重载方式运行脚本——只要被监听的文件发生变化，服务器就会重启、浏览器也会自动刷新，这是开发阶段使用 **gradio app.py** 而非 **python app.py** 的主要原因。

该 CLI 还提供 **gradio deploy**，它会打包工作目录并推送到 **Hugging Face Spaces** 进行托管；另有 **gradio environment** 用于打印诊断信息。端口、主机、分享链接和身份验证等服务器设置通常通过 Python 脚本内 **demo.launch()** 的参数配置，或通过 **GRADIO_*** 环境变量设置。

# PYTHON EXAMPLE

```python
import gradio as gr

def greet(name):
    return f"Hello, {name}!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
```

# CAVEATS

**gradio** CLI 非常精简：大多数配置发生在 Python 脚本内的 **demo.launch(...)** 中，而不是通过命令行标志。用 **share=True** 创建的分享链接 72 小时后过期，且流量经由 Gradio 基础设施隧道转发。**gradio deploy** 需要 Hugging Face 令牌（通过 **huggingface-cli login** 获取）。新版本要求 Python 3.10+。

# HISTORY

Gradio 由 **Abubakar Abid** 及其团队创建，于 **2022 年**被 **Hugging Face** 收购。它让不具备 Web 开发经验的研究者也能创建交互式界面，从而革新了机器学习演示的制作方式。

# SEE ALSO

[streamlit](/man/streamlit)(1), [python](/man/python)(1), [flask](/man/flask)(1), [uvicorn](/man/uvicorn)(1), [huggingface-cli](/man/huggingface-cli)(1)
