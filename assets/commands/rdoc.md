# TAGLINE

从源代码生成 Ruby 文档

# TLDR

**生成文档**

```rdoc [file.rb]```

**为目录生成文档**

```rdoc [lib/]```

**带标题生成文档**

```rdoc --title "[Project Name]" [lib/]```

**输出到目录**

```rdoc -o [doc/] [lib/]```

**显示类的帮助**

```ri [Array]```

# SYNOPSIS

**rdoc** [_options_] [_files_...]

# PARAMETERS

**-o**, **--output** _dir_
> 输出目录。

**--title** _text_
> 文档标题。

**-f**, **--format** _format_
> 输出格式（html、ri）。

**-m**, **--main** _file_
> 主页面文件。

**-x**, **--exclude** _pattern_
> 排除文件。

**-a**, **--all**
> 包含所有方法。

# DESCRIPTION

**RDoc** 从 Ruby 源文件生成文档。它解析注释和代码结构，创建 HTML 文档或 ri 数据文件。

# EXAMPLES

```bash
# Generate HTML docs
rdoc lib/

# With options
rdoc --title "My Gem" --main README.md lib/

# Generate ri data
rdoc -f ri lib/

# Exclude tests
rdoc -x test lib/

# View with ri
ri String#split
ri Array
```

# DOCUMENTATION FORMAT

```ruby
# Main description of class
#
# == Usage
#   obj = MyClass.new
#
# @param name [String] the name
# @return [Boolean] success status
class MyClass
  # Method description
  def my_method(name)
  end
end
```

# CAVEATS

属于 Ruby 标准库的一部分。若需增强功能可考虑 YARD。

# HISTORY

RDoc 由 **Dave Thomas** 为 Ruby 文档创建，自 Ruby 1.8 起随 Ruby 一同提供。

# INSTALL

```apt: sudo apt install ruby```

```dnf: sudo dnf install ruby```

```pacman: sudo pacman -S ruby```

```apk: sudo apk add ruby-rdoc```

```zypper: sudo zypper install ruby```

```brew: brew install ruby```

```nix: nix profile install nixpkgs#ruby```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ri](/man/ri)(1), [yard](/man/yard)(1), [ruby](/man/ruby)(1)
