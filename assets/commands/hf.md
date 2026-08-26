# TAGLINE

Hugging Face Hub 官方命令行界面

# TLDR

**登录 Hugging Face** Hub

```hf auth login```

从 Hub **下载模型**

```hf download [gpt2]```

从模型中**下载指定文件**

```hf download [meta-llama/Llama-2-7b] [config.json] [model.safetensors]```

将文件夹**上传到 Hub**

```hf upload [username/my-model] [./models] [.]```

**列出热门模型**

```hf models ls```

在 GPU 基础设施上**运行作业**

```hf jobs run --flavor [a10g-small] [pytorch/pytorch:2.6.0-cuda12.4-cudnn9-devel] [python train.py]```

**查看缓存占用**

```hf cache ls```

# SYNOPSIS

**hf** _command_ [_subcommand_] [_options_]

# COMMANDS

**auth login**
> 使用访问令牌登录 Hugging Face Hub。

**auth logout**
> 登出并移除已保存的令牌。

**auth whoami**
> 显示当前用户和组织。

**download** _repo_id_ [_files_]
> 将 Hub 上的文件下载到本地缓存。

**upload** _repo_id_ _local_path_ _path_in_repo_
> 将文件或文件夹上传到仓库。

**repo create** _repo_id_
> 在 Hub 上创建新仓库。

**repo delete** _repo_id_
> 删除仓库。

**cache ls**
> 列出已缓存的仓库及其大小。

**cache rm** _repo_id_
> 移除缓存的文件。

**jobs run** _image_ _command_
> 在 Hugging Face 基础设施上运行计算作业。

**jobs ps**
> 列出正在运行和最近的作业。

**models ls**
> 列出并搜索 Hub 上的模型。

**datasets ls**
> 列出并搜索数据集。

**spaces ls**
> 列出并搜索 Spaces。

**endpoints ls**
> 列出推理端点（Inference Endpoints）。

**collections ls**
> 列出 Hub 上的合集。

**env**
> 打印用于调试的环境信息。

**version**
> 打印已安装的 hf 版本。

# PARAMETERS

**--repo-type** _type_
> 仓库类型：model、dataset 或 space。

**--revision** _ref_
> 指定修订版本（分支、标签或提交哈希）。

**--local-dir** _path_
> 下载到指定的本地目录而不是缓存。

**--include** _pattern_
> 仅包含匹配 glob 模式的文件。

**--exclude** _pattern_
> 排除匹配 glob 模式的文件。

**--token** _token_
> 用于私有仓库的身份验证令牌。

**--quiet**
> 抑制详细输出，只打印最终结果。

**--flavor** _hardware_
> 作业使用的硬件：cpu-basic、t4-small、a10g-small、a100-large 等。

**--timeout** _duration_
> 作业超时时间，需带单位：30m、2h、1d。

**--format** _mode_
> 输出格式：auto（默认）、human、agent、json 或 quiet。

**--json**
> --format json 的快捷方式；打印结构化输出以便脚本处理。

**-q**, **--quiet**
> --format quiet 的快捷方式；仅打印 ID，每行一个。

**--no-truncate**
> 表格中显示完整值，而不是用 "..." 截断长值。

**--help**
> 显示任意命令的帮助信息。

# DESCRIPTION

**hf**（前身为 **huggingface-cli**）是 Hugging Face Hub 的官方命令行界面。它让你可以直接在终端下载模型和数据集、上传文件、管理仓库、运行计算作业，并与这个机器学习社区平台交互。

该 CLI 采用统一的 **hf resource action**（资源 动作）模式。文件会被智能去重并缓存到本地 **~/.cache/huggingface/hub/** 目录。**download** 命令支持通过 **--include/--exclude** 模式进行部分下载，且传输可断点续传。

**hf jobs** 支持在 Hugging Face 基础设施上运行代码，包括 GPU（T4、A10G、A100）和 TPU，命令风格类似 Docker。作业支持环境变量、密钥、定时执行，以及适用于自包含 Python 任务的 UV 脚本。

身份验证通过 **hf auth login** 管理，令牌保存在本地。脚本场景下也可以通过 **HF_TOKEN** 环境变量设置令牌。

# CAVEATS

部分功能需要 Hugging Face Pro 订阅或组织成员资格，包括用于获取算力的 **hf jobs**。大型模型的下载可能需要大量磁盘空间和带宽。私有仓库需要身份验证。

# HISTORY

Hugging Face Hub CLI 最初作为 **huggingface_hub** Python 包的一部分推出，用于以编程方式访问模型仓库。**2025 年 7 月**，为求简洁，CLI 从 **huggingface-cli** 更名为 **hf**，并将命令重组为更清晰的 **resource action** 结构。旧命令仍可使用，但会出现弃用警告。

# INSTALL

```brew: brew install hf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ollama](/man/ollama)(1), [git-lfs](/man/git-lfs)(1), [docker](/man/docker)(1)

# RESOURCES

```[Source code](https://github.com/huggingface/huggingface_hub)```

```[Homepage](https://huggingface.co)```

```[Documentation](https://huggingface.co/docs/huggingface_hub/en/guides/cli)```

<!-- verified: 2026-07-19 -->
