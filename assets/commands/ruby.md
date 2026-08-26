# TAGLINE

Ruby 编程语言解释器

# TLDR

**启动交互式 Ruby 会话**（IRB）

```ruby```

**执行 Ruby 脚本**

```ruby [script.rb]```

**从命令行执行 Ruby 代码**

```ruby -e "[puts 'Hello, World!']"```

**只检查语法而不执行**

```ruby -c [script.rb]```

**启用警告运行**

```ruby -w [script.rb]```

**执行表达式并打印结果**

```ruby -e "p [1, 2, 3].sum"```

**逐行处理输入**

```ruby -n -e "puts $_.upcase" [file.txt]```

**就地编辑文件**

```ruby -i -pe "gsub(/old/, 'new')" [file.txt]```

# SYNOPSIS

**ruby** [_options_] [**-e** _command_] [_programfile_] [_arguments_]

# PARAMETERS

**-e** _command_
> 将 command 作为一行脚本执行

**-c**
> 只检查语法，不执行

**-w**
> 启用警告

**-W** _level_
> 设置警告级别（0=静默，1=中等，2=详细）

**-d**, **--debug**
> 启用调试模式

**-v**, **--verbose**
> 打印版本并启用详细模式

**--version**
> 打印版本并退出

**-n**
> 将脚本包裹在 while gets() ... end 循环中

**-p**
> 类似 -n，但每次迭代后打印 $_

**-a**
> 自动分割模式（需配合 -n 或 -p），会设置 $F

**-i** [_ext_]
> 就地编辑模式（若给定扩展名则以该扩展名创建备份）

**-I** _dir_
> 将目录加入加载路径

**-r** _library_
> 执行前 require 指定的库

**-S**
> 在 PATH 中搜索脚本

**-x** [_dir_]
> 从消息中提取脚本并切换到指定目录

# DESCRIPTION

**ruby** 是 Ruby 编程语言的解释器。它可以执行 Ruby 脚本或运行交互式会话，为通用编程提供一个动态的面向对象环境。

Ruby 以优雅的语法强调程序员的幸福感和生产力。一切皆对象，这门语言支持多种编程范式：面向对象、函数式和命令式。

**-e** 选项允许在不创建文件的情况下快速执行单行代码。结合 **-n** 或 **-p** 使用时，Ruby 就成为类似 awk 或 perl 的强大文本处理工具。

要进行交互式探索，可以使用 **irb**（Interactive Ruby），或使用提供增强 REPL 功能的 **pry**。

# CONFIGURATION

**RUBYLIB**
> 以冒号分隔的目录列表，会被添加到默认加载路径（$LOAD_PATH）之前。

**RUBYOPT**
> 应用于每次 ruby 调用的默认命令行选项（例如用于警告的 -w）。

**GEM_HOME**
> gem 的安装目录，会覆盖默认的 gem 路径。

**GEM_PATH**
> 以冒号分隔的目录列表，用于搜索已安装的 gem。

**BUNDLE_GEMFILE**
> Bundler 所用 Gemfile 的路径，覆盖自动检测的结果。

# CAVEATS

不同 Ruby 版本之间可能有显著差异。请使用 **rbenv** 或 **rvm** 等版本管理器来管理多个 Ruby 安装。

gem 依赖应使用 Bundler 管理。运行脚本时使用 **bundle exec** 以确保 gem 版本正确。

Ruby 的全局解释器锁（GIL/GVL）限制了线程真正的并行能力。对于 CPU 密集型并行任务，请使用多进程或专门的库。

# HISTORY

Ruby 由日本的 **Yukihiro "Matz" Matsumoto**（松本行弘）创建，首次公开发布于 **1995 年**。Matz 设计 Ruby 的目标是比 Perl 更强大、比 Python 更面向对象。随着 **2004 年** Ruby on Rails Web 框架的发布，Ruby 获得了世界范围的流行。

# INSTALL

```apt: sudo apt install ruby```

```dnf: sudo dnf install ruby```

```pacman: sudo pacman -S ruby```

```apk: sudo apk add ruby```

```zypper: sudo zypper install ruby```

```brew: brew install ruby```

```nix: nix profile install nixpkgs#ruby```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[irb](/man/irb)(1), [gem](/man/gem)(1), [bundle](/man/bundle)(1), [rake](/man/rake)(1), [rails](/man/rails)(1)
