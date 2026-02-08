# 基础镜像
FROM python:3.12.12-slim-trixie

# 取消缓冲，参考：https://docs.python.org/3/using/cmdline.html#cmdoption-u
ENV PYTHONUNBUFFERED=1

# 安装 uv，参考：https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=docker.io/astral/uv:0.9.25 /uv /uvx /bin/

# 编译字节码，参考：https://docs.astral.sh/uv/guides/integration/docker/#compiling-bytecode
ENV UV_COMPILE_BYTECODE=1

# uv 缓存，参考: https://docs.astral.sh/uv/guides/integration/docker/#caching
ENV UV_LINK_MODE=copy

# 忽略开发依赖
ENV UV_NO_DEV=1

# 改变工作目录到 `app` 目录
WORKDIR /app/

# 安装依赖，参考：https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

# 复制项目到镜像中，参考：https://fastapi.tiangolo.com/deployment/docker/#dockerfile
COPY ./pyproject.toml ./uv.lock /app/
COPY ./app /app/app

# 同步项目，参考：https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

# 使用虚拟环境，参考：https://docs.astral.sh/uv/guides/integration/docker/#using-the-environment
ENV PATH="/app/.venv/bin:$PATH"

# 运行 FastAPI 应用，参考：https://fastapi.tiangolo.com/deployment/docker/#dockerfile
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
