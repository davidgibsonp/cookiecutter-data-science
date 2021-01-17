# {{cookiecutter.project_name}}

{{cookiecutter.description}}

### Setup Environment

This project uses [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually) for environment and dependency management. 

**Create Environment From Scratch**

```shell
# 1. create env
conda create --name env_name

# 2. activate env
conda activate env_name

# 3. install any dependencies using conda or pip

# 4. create environment file
conda env export > environment.yml
```

**Load Environment From YAML**

```shell
# 1. load env
conda env create --file environment.yml

# 2. activate env
conda activate env_name
```