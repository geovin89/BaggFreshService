from constructs import Construct
from aws_cdk import (
    Stage,
)
from bagg_fresh_service.infra.bagg_fresh_service_stack import BaggFreshServiceStack


class WebServiceStage(Stage):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        service = BaggFreshServiceStack(self, 'BaggFreshService')

        self.url_output = service.url_output

