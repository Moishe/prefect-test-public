from prefect import flow

@flow
def my_flow():
    print("Hello world.")

if __name__ == "__main__":
    gitlab_repo = "https://gitlab.com/org/my-public-repo.git"

    flow.from_source(
        source=gitlab_repo,
        entrypoint="gl_no_block.py:my_flow"
    ).deploy(
        name="my-gitlab-deployment",
        work_pool_name="my_pool",
    )
