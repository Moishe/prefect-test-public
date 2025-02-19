from prefect import flow

@flow
def my_flow():
    print("Hello world.")

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/Moishe/prefect-test-public.git",
        entrypoint="gh_no_block.py:my_flow",
    ).deploy(
        name="my-github-deployment",
        work_pool_name="my-docker-pool",
    )
