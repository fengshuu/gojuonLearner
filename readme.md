# Japanese Learning Tool

## 简介
这是一个帮助用户记忆日语假名的工具。它允许用户通过输入罗马字来练习平假名和片假名。

## 使用方法
1. 确保CSV文件格式正确，包含`index`, `hira`, `kata`, `roma`, `weight`等列。
2. 运行脚本，根据提示输入命令行参数。

### 命令行参数
- `-f`, `--file`: 指定数据文件的路径，默认为`data.csv`。
- `-r`, `--reset`: 重置所有权重为1。
- `-i`, `--input`: 指定需要输入的属性，默认为`roma`（罗马字）。
- `-d`, `--display`: 指定需要显示的属性，默认为`hira`（平假名）。

### 交互操作
- 输入正确的罗马字以匹配显示的假名。
- 输入`?`以显示答案。
- 输入`q`以退出程序。

### 数据保存
- 当用户退出程序时，所有数据将被保存到指定的CSV文件中。

## 示例
```
python script.py -f mydata.csv -r
```
这个命令将加载`mydata.csv`文件，并重置所有权重为1，然后启动学习工具。
