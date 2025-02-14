import uvicorn

import config

if __name__ == "__main__":
    uvicorn.run("api.main:app", host="127.0.0.1", port=config.API_PORT, reload=True)

