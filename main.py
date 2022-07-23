from elves.service import service
from elves.pipeline import pipelines


def main(request):
    response = [service(pipeline) for pipeline in pipelines.values()]

    print(response)
    return {"response": response}
