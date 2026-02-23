## 开发指南

配置环境：创建示例环境文件的副本
- Windows (Command Prompt):
```bash
copy .env.example .env
```
- macOS/Linux/Windows (PowerShell):
```bash
cp .env.example .env
```

## Docker 指南

构建 Docker 镜像
```bash
docker build -t admin-py .
```

查看 Docker 镜像内容
```bash
docker run -it --rm --entrypoint /bin/sh admin-py:latest
```

启动 Docker 容器
- Windows (PowerShell):
```bash
docker run -d --name admin-py -p 80:80 `
    -e "MYSQL_HOST=host.docker.internal" `
    -e "MYSQL_PORT=3306" `
    -e "MYSQL_USERNAME=root" `
    -e "MYSQL_PASSWORD=123456" `
    -e "MYSQL_DATABASE=example" `
    admin-py:latest
```
- Windows (Command Prompt):
```bash
docker run -d --name admin-py -p 80:80 ^
    -e "MYSQL_HOST=host.docker.internal" ^
    -e "MYSQL_PORT=3306" ^
    -e "MYSQL_USERNAME=root" ^
    -e "MYSQL_PASSWORD=123456" ^
    -e "MYSQL_DATABASE=example" ^
    admin-py:latest
```
