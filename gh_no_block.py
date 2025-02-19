from prefect import flow
import numpy as np

@flow(log_prints=True)
def my_flow():
    print(np.add(1.0, 4.0))

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/Moishe/prefect-test-public.git",
        entrypoint="gh_no_block.py:my_flow",
    ).deploy(
        name="my-github-deployment",
        work_pool_name="my-docker-pool",
    )
