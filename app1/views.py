from django.views.generic import View
from django.http.response import JsonResponse
from app1.tasks import sample_task


class SampleView(View):
    def get(self, *args, **kwargs):
        # Call our sample_task asynchronously with
        # our Celery Worker!
        sample_task.delay("Our printed value!")

        return JsonResponse(dict(status=200))