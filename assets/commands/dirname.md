# TAGLINE

目录路径提取工具

# TLDR

**获取**目录路径

```dirname [/path/to/file.txt]```

一次处理**多个**路径

```dirname [/path/one/file1] [/path/two/file2]```

以 **NUL 分隔**输出（用于脚本）

```dirname -z [/path/to/file]```

# SYNOPSIS

**dirname** _path_...

# DESCRIPTION

**dirname** 提取路径名的目录部分，移除最后一个组成部分。它常用于 Shell 脚本中查找文件或脚本所在的目录。

该命令是 basename 的互补命令。

# PARAMETERS

**-z**, **--zero**
> 用 NUL 而非换行符分隔输出

# BEHAVIOR

给定 `/path/to/file.txt`：
- **dirname** 返回 `/path/to`

给定 `/path/to/`：
- **dirname** 返回 `/path`

给定 `file.txt`：
- **dirname** 返回 `.`

给定 `/`：
- **dirname** 返回 `/`

# WORKFLOW

```bash
# Get directory
dirname /usr/local/bin/command
# Output: /usr/local/bin

# Get parent of current script
SCRIPT_DIR=$(dirname "$0")

# Get absolute path to script directory
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

# Multiple files
dirname /path/to/file1 /path/to/file2

# In scripts
cd "$(dirname "$0")"  # Change to script's directory
```

# COMMON USES

**脚本所在目录：**
```bash
#!/bin/bash
SCRIPT_DIR=$(dirname "$0")
source "$SCRIPT_DIR/config.sh"
```

**父目录：**
```bash
parent=$(dirname "/path/to/file")
```

**多级上溯：**
```bash
# Go up two directories
grandparent=$(dirname "$(dirname "/path/to/file")")
```

# CAVEATS

不解析符号链接（请用 readlink）。不检查路径是否存在。末尾斜杠会影响输出。不能处理所有边缘情况（空字符串等）。路径无需实际存在。

# HISTORY

**dirname** 自 Unix 早期便已存在，与 basename 一起被纳入 POSIX 标准。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[basename](/man/basename)(1), [realpath](/man/realpath)(1), [readlink](/man/readlink)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/coreutils/)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html)```

<!-- verified: 2026-07-11 -->
