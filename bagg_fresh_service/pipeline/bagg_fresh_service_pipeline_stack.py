from constructs import Construct
from aws_cdk import (
    Stack,
)
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep

from bagg_fresh_service.pipeline.webservice_stage import WebServiceStage


class BaggFreshServicePipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = CodePipeline(self, 'Pipeline',
                                pipeline_name='BaggFreshServicePipeline',
                                synth=ShellStep("Synth",
                                                input=CodePipelineSource.git_hub("geovin89/BaggFreshService", "main"),
                                                commands=["npm install -g aws-cdk",
                                                          "python -m pip install -r requirements.txt",
                                                          "cdk synth"]
                                                )
                                )
        pipeline.add_stage(WebServiceStage(self, 'Dev', env={
            'account': '141984737041',
            'region': 'us-west-2'
        }))
