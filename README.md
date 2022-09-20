# FastAPI and Mongodb - Base Project Generator 🔥
![docker build](https://github.com/khanh41/fastapi-mongodb-base-project/actions/workflows/docker-image.yml/badge.svg)
![codeQL](https://github.com/khanh41/fastapi-mongodb-base-project/actions/workflows/codeql-analysis.yml/badge.svg)

## How to use it ❓
Go to the directory where you want to create your project and run:
```bash
pip install cookiecutter
cookiecutter --checkout base-api https://github.com/khanh41/fastapi-mongodb-base-project
```

### Generate passwords ⛏
You will be asked to provide passwords and secret keys for several components. Open another terminal and run:
```bash
openssl rand -hex 32
# Outputs something like: 99d3b1f01aa639e4a76f4fc281fc834747a543720ba4c8a8648ba755aef9be7f
```

Copy the contents and use that as password / secret key. And run that again to generate another secure key.


### Input variables 💬
The generator (cookiecutter) will ask you for some data, you might want to have at hand before generating the project.

The input variables, with their default values (some auto generated) are:

* `project_name`: The name of the project
* `project_slug`: The development friendly name of the project. By default, based on the project name
* `host`: IP host running
* `port`: Port running
* `super_username`: The first superuser generated, with it you will be able to create more users, etc. By default, based on the domain.
* `super_password`: First superuser password. Use the method above to generate it.

## License 💂

This project is licensed under the terms of the MIT license.
