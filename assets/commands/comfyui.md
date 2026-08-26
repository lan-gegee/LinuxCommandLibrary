# TAGLINE

基于节点工作流系统的 Stable Diffusion 图像生成工具

# TLDR

**启动 ComfyUI 服务器**

```python [main.py]```

**在指定端口上启动**

```python [main.py] --port [8188]```

**仅使用 CPU 启动**

```python [main.py] --cpu```

**启动时不自动打开浏览器**

```python [main.py] --disable-auto-launch```

**使用指定 GPU**

```python [main.py] --cuda-device [0]```

**以低显存模式运行**

```python [main.py] --lowvram```

**通过 API 执行工作流**

```curl -X POST http://localhost:8188/prompt -H "Content-Type: application/json" -d @[workflow.json]```

# SYNOPSIS

**python** _main.py_ [_options_]

**comfyui** [_options_]

# PARAMETERS

**--port** _PORT_
> 服务器端口（默认：8188）。

**--listen** _ADDR_
> 监听地址（默认：127.0.0.1，网络访问用 0.0.0.0）。

**--cpu**
> 仅在 CPU 上运行。

**--cuda-device** _ID_
> CUDA GPU 设备索引。

**--lowvram**
> 面向显存有限 GPU 的低显存模式。

**--dont-print-server**
> 不输出服务器日志。

**--output-directory** _DIR_
> 自定义输出目录。

**--temp-directory** _DIR_
> 自定义临时目录。

**--auto-launch**
> 启动时自动打开浏览器。

**--disable-auto-launch**
> 禁止自动打开浏览器。

# DESCRIPTION

**ComfyUI** 是一个面向 Stable Diffusion 和 Flux 图像生成的节点式工作流系统。它既提供可视化图编辑器（Web UI），也提供 REST API 供程序化调用。

工作流通过连接节点来构建：模型加载器、采样器、VAE 解码器、提示词编码器等。复杂的管道（img2img、局部重绘、ControlNet、LoRA 叠加）都可以无需编码、以可视方式搭建。

API 接受工作流 JSON，可实现无头批量生成以及与脚本的集成。Web UI 中创建的工作流可以导出并通过 API 运行。

庞大的自定义节点生态提供了更多能力：视频生成、人脸修复、超分辨率放大、IP-Adapter 等。自定义节点安装到 `custom_nodes/` 目录中。

可通过 comfy-cli 安装（pip install comfy-cli && comfy install），或克隆仓库并安装依赖。模型放置在 `models/` 目录树中。

# CAVEATS

Web UI 需要现代浏览器。强烈建议使用 GPU。自定义节点之间可能冲突。模型文件很大（每个 2-10+ GB）。需要 Python 3.10+。复杂的工作流可能消耗大量显存。

# HISTORY

**ComfyUI** 由 **comfyanonymous** 于 **2023 年**创建，作为 Automatic1111 Web UI 的模块化替代方案。其节点式设计吸引了需要灵活且可复现生成管线的高级用户。它已成为最受欢迎的 Stable Diffusion 界面之一，拥有大量构建自定义节点的社区成员。

# INSTALL

```aur: yay -S comfyui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sd-cli](/man/sd-cli)(1), [mflux](/man/mflux)(1), [convert](/man/convert)(1)
