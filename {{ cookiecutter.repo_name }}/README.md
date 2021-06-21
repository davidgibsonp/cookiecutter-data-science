# {{cookiecutter.project_name}}

{{cookiecutter.description}}

### Setup Environment

This project uses [conda](https://docs.conda.io/projects/conda/en/latest/index.html) for environment and dependency management. 

**Create Env from YAML**

```sh
# 1. load env
conda env create --file environment.yml

# 2. activate env
conda activate env_{{ cookiecutter.repo_name }}

# 3. install any dependencies using conda or pip

# 4. update environment file
conda env export > environment.yml

# 5. deactivate 
conda deactivate
```
