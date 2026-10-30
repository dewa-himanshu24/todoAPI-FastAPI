GPUShaderModule.exports = {
  apps: [
    {
      name: "fastapp",
      script: "uvicorn",
      args: "index:app --host 0.0.0.0 --port 8000",
      interpreter: false,
      watch: false,
      env: {}
    }

  ]
}