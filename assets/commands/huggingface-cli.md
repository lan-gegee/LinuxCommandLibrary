# TAGLINE

Hugging Face Hub 的命令行界面

# TLDR

**登录 Hugging Face**

```huggingface-cli login```

**下载模型**

```huggingface-cli download [model-name]```

**下载模型中的指定文件**

```huggingface-cli download [model-name] [config.json] [model.safetensors]```

**下载到本地目录**

```huggingface-cli download [model-name] --local-dir [path]```

**下载数据集**

```huggingface-cli download [dataset-name] --repo-type dataset```

**将文件夹上传到仓库**

```huggingface-cli upload [repo-id] [local_path] [path_in_repo]```

**扫描本地缓存**

```huggingface-cli scan-cache```

**显示当前登录的用户**

```huggingface-cli whoami```

# SYNOPSIS

**huggingface-cli** _command_ [_options_]

# SUBCOMMANDS

**login**
> 向 Hugging Face Hub 进行身份验证。

**logout**
> 退出 Hugging Face Hub 登录。

**whoami**
> 显示当前登录用户及其所属组织。

**download** _repo_ [_files_]
> 从 Hub 下载文件。

**upload** _repo_ [_local_path_] [_path_in_repo_]
> 将文件或文件夹上传到仓库。

**upload-large-folder** _repo_ _local_path_
> 以可断点续传的分块上传方式上传大型文件夹。

**repo create** _repo_
> 在 Hub 上创建新仓库。

**scan-cache**
> 扫描并报告本地缓存目录的情况。

**delete-cache**
> 以交互方式删除未使用的缓存版本。

**tag** _repo_ _tag_
> 为仓库打上版本标签。

**env**
> 显示环境和依赖库信息。

# PARAMETERS

**--token** _token_
> 使用指定的访问令牌。

**--repo-type** _type_
> 仓库类型：model、dataset 或 space（默认：model）。

**--local-dir** _path_
> 下载到指定的本地目录而不是缓存。

**--include** _pattern_
> 匹配要包含进下载内容的文件的 Glob 模式。

**--exclude** _pattern_
> 匹配要从下载中排除的文件的 Glob 模式。

**--revision** _rev_
> 要下载的特定版本（分支、tag 或提交哈希）。

**--quiet**
> 不显示进度输出。

# DESCRIPTION

**huggingface-cli** 是 Hugging Face Hub 的命令行界面，也可作为 **hf** 命令使用。它可以下载模型和数据集、管理仓库以及对本机进行认证。它是 huggingface_hub Python 软件包的一部分。较新的 **hf** CLI 采用资源-操作模式（例如 `hf auth login`、`hf download`）。默认缓存位置为 ~/.cache/huggingface，或由 HF_HOME 环境变量指定。

# INSTALL

```brew: brew install huggingface-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1)
