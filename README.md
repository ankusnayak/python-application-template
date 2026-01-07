### Running Locally

docker compose -f docker/docker-compose.yml up --build

## CI/CD Fail Reason:
ci/cd fails because there is still placeholder like __PROJECT_NAME__ and __PROJECT_DESCRIPTION__ etc. We need to change that by running the command:

```shell
    chmod +x scripts/bootstrap.sh
    ./scripts/bootstrap.sh
```
