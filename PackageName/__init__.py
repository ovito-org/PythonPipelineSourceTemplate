from ovito.data import DataCollection
from ovito.pipeline import PipelineSourceInterface
# from traits.api import Range, observe

class PipelineSourceName(PipelineSourceInterface):
    '''
    # Parameter controlling the animation length (value can be changed by the user):
    duration = Range(low=1, value=10)

    def compute_trajectory_length(self, **kwargs):
        return self.duration

    # This is needed to notify the pipeline system whenever the duration is changed by the user:
    @observe("duration")
    def anim_duration_changed(self, event):
        self.notify_trajectory_length_changed()
    '''

    def create(self, data: DataCollection, *, frame: int, **kwargs):
        pass