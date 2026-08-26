# TAGLINE

Common Workflow Language 执行器

# TLDR

**运行 CWL 工作流**

```cwl-runner [workflow.cwl] [inputs.yml]```

**以指定的输入值运行**

```cwl-runner [workflow.cwl] --[input_name] [value]```

**禁用 Docker 运行**

```cwl-runner --no-container [workflow.cwl] [inputs.yml]```

**使用自定义输出目录运行**

```cwl-runner --outdir [/path/to/output] [workflow.cwl] [inputs.yml]```

**校验 CWL 文档**

```cwl-runner --validate [workflow.cwl]```

**并行运行**

```cwl-runner --parallel [workflow.cwl] [inputs.yml]```

# SYNOPSIS

**cwl-runner** [_options_] _workflow.cwl_ [_inputs_]

# PARAMETERS

**--validate**
> 只校验 CWL 文档而不运行。

**--outdir** _path_
> 结果的输出目录。

**--no-container**
> 禁用 Docker/容器执行。

**--parallel**
> 并行运行工作流步骤。

**--cachedir** _path_
> 缓存中间结果的目录。

**--tmpdir-prefix** _path_
> 临时目录的前缀。

**--debug**
> 启用调试输出。

**--quiet**
> 只打印警告和错误。

**--validate**
> 只校验 CWL 文档而不运行。

**--leave-tmpdir**
> 不删除临时目录。

**--version**
> 打印版本并退出。

**--make-template**
> 生成模板输入对象。

**--on-error** _action_
> 失败时的工作流行为（stop 或 continue）。

**--singularity**
> 使用 Singularity 容器运行时代替 Docker。

**--podman**
> 使用 Podman 容器运行时代替 Docker。

# DESCRIPTION

**cwl-runner** 执行以 Common Workflow Language（CWL）定义的工作流。CWL 是一项用于描述数据密集型科学中分析工作流的规范。CWL 工作流可在不同的执行环境间移植。

执行器接收 CWL 文档和输入参数，解析依赖关系，并按正确顺序执行工具。步骤可以在容器（Docker/Singularity）中运行以保证可复现性；如果工具已在本地安装，也可以原生运行。

输入参数可在 YAML/JSON 文件中指定，也可作为命令行参数传入。输出会被放入指定的输出目录，并附带一份描述结果的清单。

# INPUT FILE EXAMPLE

```yaml
# inputs.yml
fastq_file:
  class: File
  path: /data/sample.fastq
reference:
  class: File
  path: /data/reference.fa
threads: 8
```

# CAVEATS

默认实现（cwltool）在处理大型工作流时可能有性能局限。某些高级功能需要特定的运行器（toil-cwl-runner、arvados-cwl-runner）。容器需求需要安装 Docker 或 Singularity。输入中的文件路径必须能被执行器访问。

# HISTORY

Common Workflow Language 由社区于 **2014 年**开始协作开发，规范于 **2016 年**达到 **v1.0**。在 **Peter Amstutz** 和 **Michael Crusoe** 的带领下，CWL 源自生物信息学对可移植、可复现工作流的需求。**cwltool** 是其参考实现。CWL 已被众多科学平台采用，成为共享计算流程的标准。

# SEE ALSO

[snakemake](/man/snakemake)(1), [nextflow](/man/nextflow)(1)
