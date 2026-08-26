# TAGLINE

将笔记本保存为纯 Python 文件的响应式 Python 笔记本工具

# TLDR

**创建新笔记本**

```marimo edit [notebook.py]```

**打开已有笔记本**

```marimo edit [notebook.py]```

**以应用方式运行笔记本**

```marimo run [notebook.py]```

**使用自定义端口运行**

```marimo run --port [8080] [notebook.py]```

**转换 Jupyter 笔记本**

```marimo convert [notebook.ipynb] > [notebook.py]```

**导出为 HTML**

```marimo export html [notebook.py] > [output.html]```

**用模板创建新笔记本**

```marimo new```

**显示版本**

```marimo --version```

# SYNOPSIS

**marimo** [_edit_] [_run_] [_convert_] [_export_] [_options_] [_notebook.py_]

# PARAMETERS

**edit** _FILE_
> 在浏览器中编辑笔记本。

**run** _FILE_
> 将笔记本作为交互式应用运行。

**convert** _FILE_
> 从 Jupyter 转换为 marimo。

**export** _FORMAT_ _FILE_
> 导出笔记本（html、md、script）。

**new**
> 从模板创建新笔记本。

**--port** _PORT_
> 服务器端口。

**--host** _HOST_
> 服务器主机。

**--headless**
> 不打开浏览器。

**--watch**
> 监视文件变化。

**--sandbox**
> 在沙盒环境中运行。

**--version**
> 显示版本。

**--help**
> 显示帮助。

# DESCRIPTION

**marimo** 是一个响应式 Python 笔记本工具，它把笔记本存储为纯 Python 文件。与 Jupyter 不同，当依赖发生变化时单元格会自动重新执行。

笔记本本身就是 Python 脚本，因此可以用 Git 进行版本控制而不会出现 JSON 合并冲突。各个单元格定义的函数和变量构成一张依赖图。

响应式执行模型确保了一致性。修改变量会自动更新所有依赖它的单元格。传统笔记本中的隐藏状态和执行顺序问题由此被消除。

run 模式可将笔记本部署为交互式 Web 应用。用户与组件交互，Python 后端负责计算。

从 Jupyter 的转换会保留代码和 markdown 单元格。对于依赖执行顺序的笔记本，其响应式结构可能需要调整。

# CAVEATS

与 Jupyter 的思维模型不同——不保证线性执行顺序。部分 Jupyter magic 命令不受支持。大型笔记本的响应式更新可能带来性能影响。

# HISTORY

**marimo** 由 **Akshay Agrawal** 和 **Myles Scolnick** 于 **2023 年**在斯坦福创建。它通过响应式编程使执行具有确定性，从而解决传统笔记本的可复现性问题。

# INSTALL

```nix: nix profile install nixpkgs#marimo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jupyter](/man/jupyter)(1), [ipython](/man/ipython)(1), [streamlit](/man/streamlit)(1), [python](/man/python)(1)
