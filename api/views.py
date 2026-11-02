from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health(request):
    """Simple health check used by the pipeline and the grader."""
    return Response({"status": "ok"})


@api_view(["GET"])
def hello(request):
    """Greets the caller. Optional ?name= query parameter."""
    name = request.query_params.get("name", "world")
    return Response({"message": f"Hello, {name}!", "course": "CSC 325"})
